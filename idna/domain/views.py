from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import TestData
from .serializers import TestSerializer
from django.http import JsonResponse

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
    
def idnaDomain(request):
    print('Hello')
    return render(request, 'domain/index.html')


def apiOverview(request):
    return JsonResponse("API BASE POINT" , safe=False)