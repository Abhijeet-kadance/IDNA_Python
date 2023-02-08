from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import TestData
from .serializers import TestSerializer

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = TestData.objects.all()
    serializer_class = TestSerializer
    
    
def getData(request):
    data = TestData.objects.all()
    print(data)
    return Response()

def postData(request):
    print('Hello')
    
