from rest_framework import generics, permissions
from rest_framework.response import Response

from app_users.models import User
from app_users.serializers import UserSerializer, RegisterSerializer, UserDetailSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user_id': user.pk,
            'email': user.email,
        })

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LoginSerializer
        return RegisterSerializer
