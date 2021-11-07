from .models import PersonInfo, Vocation
from .serializers import VocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


class VocationClass(APIView):
    def get(self, request):
        q = Vocation.objects.all()
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        # serializer = MySerializer(instance=p, many=True)
        serializer = VocationSerializer(instance=p, many=True)
        return Response(serializer.data)
