"""
Import packages
"""
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

from .models import RoleModel
from .serializers import RoleSerializer
# Create your views here.


class RoleView(APIView):
    def get(self, request):
        musics = RoleModel.objects.all()
        serializer = RoleSerializer(musics, many=True)
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
            saved = RoleModel.objects.get(id=id)
            # data = serializers.serialize('json', [saved, ])
            # struct = json.loads(data)
            # data = json.dumps(struct[0])

            serializer = RoleSerializer(
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
            saved = RoleModel.objects.get(id=id)
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
