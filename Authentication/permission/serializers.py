"""
Import packages
"""
from rest_framework import serializers

from .models import PermissionModel


class PermissionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = PermissionModel
        fields = ('id', 'name', 'description')
