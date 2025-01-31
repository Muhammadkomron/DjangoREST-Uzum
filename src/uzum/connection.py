import json
from typing import Optional, Union

import requests

from uzum import exceptions


class Connection:
    def __init__(self, session: Optional[requests.Session], headers: dict):
        self.session = session
        self.headers = headers

    def close(self):
        return self.session.close()

    @staticmethod
    def _raise_for_status(resp: Optional[requests.Response], text: str) -> dict:
        try:
            data = json.loads(text)

        except json.JSONDecodeError:
            raise json.JSONDecodeError

        error_code = data.get('errorCode')
        status_code = resp.status_code

        if not error_code and status_code == 200:
            return data

        raise_error(data, error_code, status_code)

    def _request(self, url: str, data: dict = None, method: str = 'POST') -> dict:
        try:
            with self.session.request(url=url, method=method, headers=self.headers, json=data) as resp:
                return self._raise_for_status(resp, resp.text)
        except requests.Timeout:
            raise exceptions.NotResponding
        except requests.ConnectionError:
            raise exceptions.NetworkError

    def _request_model(self, url: str, data: dict = None):
        return self._request(url, data)


def raise_error(data: dict, error_code: Union[int, None], status_code: int) -> None:
    if status_code == 400:
        raise exceptions.BadRequest(data, error_code)
    elif status_code == 401:
        raise exceptions.SignatureError(data, error_code)
    elif status_code == 403:
        raise exceptions.FingerprintError(data, error_code)
    elif status_code == 422:
        raise exceptions.ValidationError(data, error_code)
    elif status_code == 500:
        raise exceptions.InternalServerError(data, error_code)

    if error_code >= 5000:
        raise exceptions.InternalError(data, error_code)
    elif error_code >= 3000:
        raise exceptions.PaymentErrors(data, error_code)
    elif error_code >= 2000:
        raise exceptions.ValidationError(data, error_code)
    elif error_code >= 1000:
        raise exceptions.AuthenticationError(data, error_code)

    raise exceptions.UnexpectedError(data, error_code)
