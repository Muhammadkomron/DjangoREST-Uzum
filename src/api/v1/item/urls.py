from rest_framework import routers

from api.v1.item.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'', ItemViewSet, basename='item')
urlpatterns = router.urls
