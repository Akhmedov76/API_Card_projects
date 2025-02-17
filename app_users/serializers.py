from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'level', 'is_active', 'is_staff']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'birth_date', 'phone_number', 'role',
                  'preferred_language', 'language_level', 'bio']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'level', 'is_active', 'is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
