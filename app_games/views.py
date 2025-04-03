from .models import *
from rest_framework import generics
from . import serializers

class MiniGameListAPIView(generics.ListAPIView):
    queryset = MiniGame.objects.all()
    serializer_class = serializers.MiniGameSerialize


class MiniGameListCreateAPIView(generics.ListCreateAPIView):
    queryset = MiniGame.objects.all()
    serializer_class = serializers.MiniGameSerialize


class MiniGameUpdateAPIView(generics.UpdateAPIView):
    queryset = MiniGame.objects.all()
    serializer_class = serializers.MiniGameUpdateSerialize
    http_method_names = ("patch", 'put')


class MiniGameRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MiniGame.objects.all()
    serializer_class = serializers.MiniGameSerialize


class MiniGameDeleteAPIView(generics.DestroyAPIView):
    queryset = MiniGame.objects.all()
    serializer_class = serializers.MiniGameSerialize

