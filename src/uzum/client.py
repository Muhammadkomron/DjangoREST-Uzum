from typing import Optional, Any

import requests
from django.conf import settings

from uzum.connection import Connection


class ApiClient(Connection):
    """Performs requests to the Uzum Checkout API"""

    def __init__(self, terminal_id: str = settings.UZUM_TERMINAL_ID, api_key: str = settings.UZUM_API_KEY,
                 content_language: str = 'ru-RU', base_url: str = settings.UZUM_URL) -> None:
        """
        :param terminal_id: Идентификатор терминала
          Если подпись окажется не валидной, Uzum checkout вернет ответ с errorCode=1000.
        :param content_language: Уникальный ключ, который используется для аутентификации запросов.
        :param api_key: Уникальный ключ, который используется для аутентификации запросов.
        :param base_url: URL-адрес API.
        """
        self.terminal_id = terminal_id
        self.api_key = api_key
        self.content_language = content_language
        self.headers = {
            'Content-Language': self.content_language,
            'X-Terminal-Id': self.terminal_id,
            'X-API-Key': self.api_key,
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
        }
        self.base_url = base_url
        self.session = requests.Session()

        Connection.__init__(self, self.session, self.headers)

    def register(self,
                 amount: Optional[float],
                 client_id: str,
                 currency: int,
                 order_number: str,
                 payment_details: Optional[str] = None,
                 success_url: Optional[str] = None,
                 failure_url: Optional[str] = None,
                 view_type: str = 'REDIRECT',
                 merchant_params: Optional[dict[dict[str, Any]]] = None,
                 session_timeout_secs: int = 600,
                 **kwargs) -> dict:
        """
        Запрос регистрации одностадийного платежа.

        :param amount: Сумма платежа (в тийинах, без комиссии)
        :param client_id: Идентификатор клиента в системе мерчанта. Используется для создания привязок и мапинга платежей между Uzum Checkout и системой мерчанта.
        :param currency: Валюта платежа. Необходимо указать по стандарту ISO 4217 код. Например: российский рубль - RUB - 643; а узбекский сум - UZS - 860.
        :param order_number: Идентификатор заказа на стороне мерчанта
        :param payment_details: Детали платежа
        :param success_url: URL для редиректа, если платеж пройдет успешно
        :param failure_url: URL для редиректа, если платеж завершится ошибкой
        :param view_type: Тип отображения платежной страницы
        :param merchant_params: Дополнительные параметры мерчанта
        :param session_timeout_secs: Максимальная продолжительность сессии в секундах
        :param kwargs:
        """
        url = f'{self.base_url}payment/register'

        data = {
            'amount': amount,
            'clientId': client_id,
            'currency': currency,
            'paymentDetails': payment_details,
            'orderNumber': order_number,
            'successUrl': success_url,
            'failureUrl': failure_url,
            'viewType': view_type,
            'merchantParams': merchant_params,
            'sessionTimeoutSecs': session_timeout_secs,
            'paymentParams': {'payType': 'ONE_STEP'},
        }

        return self._request_model(url, data={**data, **kwargs})

    def merchant_pay(self, process_data: dict[dict[str, Any]], order_id: str) -> dict:
        """
        Этот метод используют мерчанты Server to Server. Это метод оплаты биндом.

        :param process_data: Данные способа оплаты
        :param order_id: Идентификатор заказа
        """
        url = f"{self.base_url}payment/merchantPay"
        data = {
            'processData': process_data,
            'orderId': order_id,
        }

        return self._request_model(url, data=data)

    def get_order_status(self, order_id: str) -> dict:
        """
        Получение информации о статусе платежа.

        :param order_id: Идентификатор заказа
        """
        url = f"{self.base_url}payment/getOrderStatus"
        data = {
            'orderId': order_id,
        }

        return self._request_model(url, data=data)

    def complete(self, order_id: str, amount: int) -> dict:
        """
        Подтверждение двухстадийного платежа

        :param order_id: Идентификатор заказа
        :param amount: Сумма для комплита в тийинах
        """
        url = f"{self.base_url}acquiring/complete"
        data = {
            'orderId': order_id,
            'amount': amount,
        }

        return self._request_model(url, data=data)

    def reverse(self, order_id: str, amount: int) -> dict:
        """
        Метод используется для отмены оплаты заказа. Это метод для расхолдирования средств на счету.
        Отмену можно выполнить, когда платёж находится в статусе "AUTHORIZED".

        :param order_id: Идентификатор заказа
        :param amount: Сумма для комплита в тийинах
        """
        url = f"{self.base_url}acquiring/reverse"
        data = {
            'orderId': order_id,
            'amount': amount,
        }

        return self._request_model(url, data=data)

    def get_bindings(self, client_id: str) -> dict:
        """
        Метод получения списка привязок пользователя
        https://www.inplat-tech.ru/docs/checkout/#tag/acquiring/operation/get_bindings_api_v1_acquiring_getBindings_post

        :param client_id: Метод получения списка привязок пользователя
        """
        url = f"{self.base_url}acquiring/getBindings"
        data = {
            'clientId': client_id,
        }

        return self._request_model(url, data=data)

    def __repr__(self) -> str:
        return '<Uzum Payments Client>'
