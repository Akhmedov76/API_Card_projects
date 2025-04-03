from .models import *
from rest_framework import serializers


class MiniGameSerialize(serializers.ModelSerializer):
    class Meta:
        model = MiniGame
        fields = '__all__'

    def validate(self, attrs):
        return attrs


class MiniGameUpdateSerialize(serializers.ModelSerializer):
    class Meta:
        model = MiniGame
        fields = '__all__'

    def validate(self, attrs):
        return attrs
