from rest_framework import routers

from api.v1.order.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet, basename='order')
urlpatterns = router.urls
