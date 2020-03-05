"""
Import packages
"""
from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path('/permission', views.PermissionView.as_view()),
    path('/permission/<str:id>',  views.PermissionView.as_view())
]
