from django.urls import path
from . import views

urlpatterns = [
    path('minigame-list/', views.MiniGameListAPIView.as_view()),
    path('minigame-create/', views.MiniGameListCreateAPIView.as_view()),
    path('minigame-update/<int:pk>/', views.MiniGameUpdateAPIView.as_view()),
    path('minigame-retrieve/<int:pk>/', views.MiniGameRetrieveAPIView.as_view()),
    path('minigame-delete/<int:pk>/', views.MiniGameDeleteAPIView.as_view()),
]