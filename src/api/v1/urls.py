from django.urls import include, path

app_name = 'v1'
urlpatterns = [
    path(r'item/', include('api.v1.item.urls')),
    path(r'order/', include('api.v1.order.urls')),
    path(r'product/', include('api.v1.product.urls')),
]
