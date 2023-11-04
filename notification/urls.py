from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api import NotificationViewSet
from notification.views import ShowNotifications


router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
urlpatterns = [
    path('', ShowNotifications, name='show-notifications'),
]