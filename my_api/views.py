from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Book,Fanlar,Yunalishlar,Unversitetlar
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerilizer
class FanViewSet(viewsets.ModelViewSet):
    queryset = Fanlar.objects.all().order_by("id")
    serializer_class = FanlarSerilizer

class YunalishViewSet(viewsets.ModelViewSet):
    queryset = Yunalishlar.objects.all().order_by("id")
    serializer_class = YunalishSerilizer
class UnversityViewSet(viewsets.ModelViewSet):
    queryset = Unversitetlar.objects.all().order_by("id")
    serializer_class = UnversitySerilizer




