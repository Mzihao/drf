from django.urls import path
from .views import *

urlpatterns = [
    path('', VocationClass.as_view(), name='myClass')
]