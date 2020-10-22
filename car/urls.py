from django.urls import path

from .viewsets import (
    CarView
)

# router = DefaultRouter()
# router.register(r'', CarViewSet)

appname = 'cars'

urlpatterns = [
    path('predict/', CarView.as_view())
]