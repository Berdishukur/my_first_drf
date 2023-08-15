from django.contrib.auth.models import User,Group
from rest_framework import routers, serializers, viewsets
from .models import Book,Fanlar,Yunalishlar,Unversitetlar

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
class YunalishSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Yunalishlar
        fields="__all__"

class FanlarSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Fanlar
        fields="__all__"

class UnversitySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Unversitetlar
        fields="__all__"


