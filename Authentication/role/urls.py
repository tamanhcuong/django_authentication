"""
Import packages
"""
from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path('/role', views.RoleView.as_view()),
    path('/role/<str:id>',  views.RoleView.as_view())
]
