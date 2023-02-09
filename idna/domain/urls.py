from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf import settings
from .views import *

# Creating a router

router = routers.DefaultRouter()

router.register(r'test', TestViewSet)

urlpatterns = [
    path('', views.getData),
    path('api-auth/', include('rest_framework.urls')),
    path('post/', views.postData),
    path('idna/',views.idnaDomain,name='idnaDomain'),
    path('api/', views.apiOverview , name="api-overview")
]
