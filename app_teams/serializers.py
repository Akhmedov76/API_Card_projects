from .models import Team, JoinRequest
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            "id",
            "user",
            "name",
            "members",
            "created_at"
        ]
        read_only_fields = ("id", "created_at")

    
class JoinRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JoinRequest
        fields = [
            "id",
            "user",
            "team",
            "time",
            "status"
        ]
        read_only_fields = ["id", "time", "status"]