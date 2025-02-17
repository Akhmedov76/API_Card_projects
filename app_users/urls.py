from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, UserUpdateView, LoginView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
]
