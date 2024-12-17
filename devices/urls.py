from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, PayloadViewSet, DeviceListView

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'payloads', PayloadViewSet, basename='paylaod')

#urls to access api endpoint and listview 
urlpatterns = [
    path('api/', include(router.urls)),
    path('devices/', DeviceListView.as_view(), name='device_list'),
]
