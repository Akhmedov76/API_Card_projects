from .models import Team, JoinRequest
from .serializers import TeamSerializer, JoinRequestSerializer
from app_users.permissions import IsTeacher
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ListCreateTeamView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsTeacher]

    def get_queryset(self):
        return self.request.user.user_teams.all()
    

class JoinTeamView(APIView):
    serializer_class = JoinRequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.join_requests.exists():
            return Response(
                {"message": "There is a pending request"},
                status = status.HTTP_403_FORBIDDEN
            )
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListRequests(APIView):
    permission_classes = [IsTeacher]
    serializer_class = JoinRequestSerializer

    def get(self, request, team_id, *args, **kwargs):
        user = request.user
        team = Team.objects.filter(user=user, id=team_id).first()

        if team:
            data = team.requests.filter(status="PENDING")
            serializer = self.serializer_class(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message":"Team not found!"},
            status=status.HTTP_404_NOT_FOUND
        )
    

class ManageRequestsView(APIView):
    permission_classes = [IsTeacher]
    
    def post(self, request):
        request_id = request.data.get("request_id")
        action = request.data.get("action")  

        if (not request_id) or (action not in ["approve", "reject"]):
            return Response({"error": "Invalid data provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            join_request = JoinRequest.objects.get(id=request_id)
        except JoinRequest.DoesNotExist:
            return Response({"error": "Join request not found"}, status=status.HTTP_404_NOT_FOUND)

        if action == "approve":
            join_request.status = "APROVED"
            join_request.team.members.add(join_request.user)
        else:
            join_request.status = "REJECTED"
        
        join_request.save()
        return Response({"message": f"Request {action}d successfully"}, status=status.HTTP_200_OK)