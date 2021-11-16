from .models import PersonInfo, Vocation
from .serializers import VocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from index.permissions import IsAdminUserOrReadOnly


class VocationClass(APIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request):
        q = Vocation.objects.all().order_by('id')
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        # serializer = MySerializer(instance=p, many=True)
        serializer = VocationSerializer(instance=p, many=True)
        return Response(serializer.data)

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
