from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from .views import UserViewSet, GroupViewSet


router = routers.DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path("api-auth/",include('rest_framework.urls',namespace='rest-framework')),

]

