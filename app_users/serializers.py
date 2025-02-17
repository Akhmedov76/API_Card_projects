from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'role', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['id', 'is_staff']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "password")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "phone_number", "is_active")


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
