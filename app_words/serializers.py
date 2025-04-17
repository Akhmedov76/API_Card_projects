from rest_framework import serializers
from .models import WordCard, PrivateCard


class WordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCard
        fields = ('id', 'word', 'translation', 'example', 'team', 'created_at')

    def validate_word(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("So‘z kamida 2 ta belgidan iborat bo‘lishi kerak.")
        return value

    def validate_translation(self, value):
        if not value:
            raise serializers.ValidationError("Tarjima bo‘sh bo‘lishi mumkin emas.")
        return value

    def validate_example(self, value):
        if not value:
            raise serializers.ValidationError("Misol bo‘sh bo‘lishi mumkin emas.")
        return value


#----------------------------------------------------------------------------
class PrivateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateCard
        fields = ('id', 'word', 'translation', 'description', 'status', 'user')

    def validate_word(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("So‘z kamida 2 ta belgidan iborat bo‘lishi kerak.")
        return value

    def validate_translation(self, value):
        if not value:
            raise serializers.ValidationError("Tarjima bo‘sh bo‘lishi mumkin emas.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Tavsif (description) bo‘sh bo‘lishi mumkin emas.")
        return value
