"""
Import packages
"""
from rest_framework import serializers
from .models import UserModel
from .models import RoleModel


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    role = serializers.PrimaryKeyRelatedField(
        many=True, queryset=RoleModel.objects.all())

    class Meta:
        model =  UserModel
        fields = ('id', 'username', 'password', 'email', 'role')
