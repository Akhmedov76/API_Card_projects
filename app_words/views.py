from rest_framework import generics, permissions
from .models import WordCard, PrivateCard
from . import serializers

# ======================= WORD CARD =======================

class WordCardListAPIView(generics.ListAPIView):
    queryset = WordCard.objects.all()
    serializer_class = serializers.WordCardSerializer


class WordCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = WordCard.objects.all()
    serializer_class = serializers.WordCardSerializer


class WordCardUpdateAPIView(generics.UpdateAPIView):
    queryset = WordCard.objects.all()
    serializer_class = serializers.WordCardSerializer
    http_method_names = ("patch",)


class WordCardRetrieveAPIView(generics.RetrieveAPIView):
    queryset = WordCard.objects.all()
    serializer_class = serializers.WordCardSerializer


class WordCardDeleteAPIView(generics.DestroyAPIView):
    queryset = WordCard.objects.all()
    serializer_class = serializers.WordCardSerializer

# ======================= PRIVATE CARD =======================

class PrivateCardListAPIView(generics.ListAPIView):
    serializer_class = serializers.PrivateCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PrivateCard.objects.filter(user=self.request.user)


class PrivateCardListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.PrivateCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # foydalanuvchini avtomatik biriktiradi

    def get_queryset(self):
        return PrivateCard.objects.filter(user=self.request.user)


class PrivateCardUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.PrivateCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PrivateCard.objects.filter(user=self.request.user)

    http_method_names = ("patch",)


class PrivateCardRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.PrivateCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PrivateCard.objects.filter(user=self.request.user)


class PrivateCardDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.PrivateCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PrivateCard.objects.filter(user=self.request.user)
