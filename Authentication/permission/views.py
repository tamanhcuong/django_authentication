"""
Import packages
"""
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

from .models import PermissionModel
from .serializers import PermissionSerializer
# Create your views here.


class PermissionView(APIView):
    def get(self, request):
        musics = PermissionModel.objects.all()
        serializer = PermissionSerializer(musics, many=True)
        res = {
            'status': 200,
            'msg': 'Successfully',
            'data': serializer.data
        }
        return Response(res)

    def post(self, request, format=None):
        serializer = PermissionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                res = {
                    'status': 200,
                    'msg': 'Successfully',
                    'data': serializer.data
                }
                return Response(res)
            else:
                res = {
                    'status': 400,
                    'msg': serializer.errros
                }
                return Response(res)
        except Exception as err:
            res = {
                'status': 400,
                'msg': str(err)
            }
            return Response(res)

    def put(self, request, id):
        try:
            body = request.data
            saved = PermissionModel.objects.get(id=id)
            # data = serializers.serialize('json', [saved, ])
            # struct = json.loads(data)
            # data = json.dumps(struct[0])

            serializer = PermissionSerializer(
                instance=saved, data=body, partial=True)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                res = {
                    'status': 200,
                    'msg': 'Successfully',
                    'data': serializer.data
                }
                return Response(res)
            else:
                res = {
                    'status': 400,
                    'msg': serializer.errors
                }
                return Response(res)
        except Exception as err:
            res = {
                'status': 400,
                'msg': str(err)
            }
            return Response(res)

    def delete(self, request, id):
        try:
            saved = PermissionModel.objects.get(id=id)
            saved.delete()
            res = {
                'status': 200,
                'msg': 'Successfully'
            }
            return Response(res)

        except Exception as err:
            res = {
                'status': 400,
                'msg': str(err)
            }
            return Response(res)
