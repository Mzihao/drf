from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import PersonInfo, Vocation
from .serializers import VocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAdminUser
from index.permissions import IsAdminUserOrReadOnly


class VocationClass(APIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUserOrReadOnly]

    @swagger_auto_schema(tags=['info'], operation_summary='查询员工信息')
    def get(self, request):
        q = Vocation.objects.all().order_by('id')
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        # serializer = MySerializer(instance=p, many=True)
        serializer = VocationSerializer(instance=p, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        # required=['phone'],
        properties={'job': openapi.Schema(type=openapi.TYPE_STRING),
                    'title': openapi.Schema(type=openapi.TYPE_STRING),
                    'payment': openapi.Schema(type=openapi.TYPE_INTEGER),
                    # 'info': openapi.Schema(type=openapi.TYPE_ARRAY({
                    #     'name': openapi.Schema(type=openapi.TYPE_STRING),
                    #     'age': openapi.Schema(type=openapi.TYPE_INTEGER),
                    #     'hireDate': openapi.Schema(type=openapi.TYPE_STRING),
                    # })),
                    }
    ), operation_summary='新增员工信息', tags=['info'])
    def post(self, request):
        data = request.data
        if not data:
            return Response({'msg': 'hello Martin', 'code': 200, 'tip': '你没有填信息哦'}, status=200)
        id = request.data.get('id', 0)  # 3
        operation = Vocation.objects.filter(id=id).first()
        # 数据验证
        serializer = VocationSerializer(data=request.data)
        if serializer.is_valid():
            # 是否存在，更新？新增
            if operation:
                serializer.updata(request.data)
            else:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=404)
