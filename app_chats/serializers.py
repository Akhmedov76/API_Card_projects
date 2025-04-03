from .models import *
from rest_framework import serializers


class ChatSerialize(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def validate(self, attrs):
        return attrs
