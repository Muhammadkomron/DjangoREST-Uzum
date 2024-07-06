from rest_framework import routers

from api.v1.product.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet, basename='product')
urlpatterns = router.urls
