"""
Import packages
"""
from rest_framework import serializers
from .models import PermissionModel
from .models import RoleModel


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    email = serializers.CharField()
    permissions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=PermissionModel.objects.all())

    class Meta:
        model = RoleModel
        fields = ('id', 'name', 'description', 'permissions')
