"""
Import packages
"""
from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path('/user', views.UserView.as_view()),
    path('/user/<str:id>',  views.UserView.as_view())
]
