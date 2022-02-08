
from email.mime import base
from django import views
from django.contrib import admin
from django.urls import path, include
from scoring.views import EmployeesViewSet
from rest_framework import routers
from scoring.views import *

router = routers.DefaultRouter()
router.register("employees", EmployeesViewSet, basename= "Employees")
#router.register("teste", django_view, basename= "Teste")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("send", EmployeesViewSet.django_view)
]
