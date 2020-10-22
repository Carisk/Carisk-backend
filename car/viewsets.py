import random

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import (
    permissions, mixins, 
    filters, generics, status,
    viewsets, filters,
)
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

# from .models import Car

# from .serializers import (
#     AccidentRiskSerializer
# )


# Create your views here.
class CarView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'suck': 'my balls'
        }
        return Response(data, status=status.HTTP_200_OK)

