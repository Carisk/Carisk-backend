from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .viewsets import (
    CarView
)

# router = DefaultRouter()
# router.register(r'', CarViewSet)

appname = 'cars'

urlpatterns = [
    path('predict/', CarView.as_view())
]