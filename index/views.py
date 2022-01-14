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
from utils import response_json


class VocationClass(APIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUserOrReadOnly]

    @response_json
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description='编号', type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('page', openapi.IN_QUERY, description='页数', type=openapi.TYPE_INTEGER, required=False),
        openapi.Parameter('pageSize', openapi.IN_QUERY, description='size', type=openapi.TYPE_INTEGER, required=False)
    ], tags=['info'], operation_summary='查询员工信息', responses={200: VocationSerializer(many=True)})
    def get(self, request, **kwargs):
        print(kwargs)
        q = Vocation.objects.all().order_by('id')
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        # serializer = MySerializer(instance=p, many=True)
        serializer = VocationSerializer(instance=p, many=True)
        return serializer.data
        # return Response(serializer.data)

    # @response_json
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['job', 'title', 'payment'],
        properties={'job': openapi.Schema(type=openapi.TYPE_STRING, description='部门'),
                    'title': openapi.Schema(type=openapi.TYPE_STRING, description='岗位名称'),
                    'payment': openapi.Schema(type=openapi.TYPE_INTEGER, description='薪资', default=2000),
                    'info': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        required=['name', 'age', 'hireDate'],
                        properties={
                            'name': openapi.Schema(type=openapi.TYPE_STRING, description='姓名'),
                            'age': openapi.Schema(type=openapi.TYPE_INTEGER, description='年龄'),
                            'hireDate': openapi.Schema(type=openapi.TYPE_STRING, description='入职时间'),
                        })
                    }),
        operation_summary='新增员工信息',
        tags=['info'],
        operation_description="这里是描述！",
        responses={200: VocationSerializer(many=True)})
    def post(self, request, **kwargs):
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
