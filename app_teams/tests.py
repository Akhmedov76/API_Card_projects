from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from app_users.models import User
from app_teams.models import Team, JoinRequest
from django.urls import reverse

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="teacher@example.com", password="pass")
        self.client.force_authenticate(user=self.user)
        self.team = Team.objects.create(user=self.user, name="Test Team")
    
    def test_list_teams(self):
        response = self.client.get(reverse("team-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        data = {"name": "New Team"}
        response = self.client.post("/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class JoinRequestTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="student@example.com", password="pass")
        self.team_owner = User.objects.create_user(email="teacher@example.com", password="pass")
        self.team = Team.objects.create(user=self.team_owner, name="Test Team")
        self.client.force_authenticate(user=self.user)
    
    def test_create_join_request(self):
        data = {"team": self.team.id}
        response = self.client.post("/teams/join/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_duplicate_join_request(self):
        JoinRequest.objects.create(user=self.user, team=self.team, status="PENDING")
        response = self.client.post("/teams/join/", {"team": self.team.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ManageRequestsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.teacher = User.objects.create_user(email="teacher@example.com", password="pass")
        self.student = User.objects.create_user(email="student@example.com", password="pass")
        self.team = Team.objects.create(user=self.teacher, name="Test Team")
        self.join_request = JoinRequest.objects.create(user=self.student, team=self.team, status="PENDING")
        self.client.force_authenticate(user=self.teacher)
    
    def test_approve_request(self):
        data = {"request_id": self.join_request.id, "action": "approve"}
        response = self.client.post("/teams/manage-requests/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.join_request.refresh_from_db()
        self.assertEqual(self.join_request.status, "APROVED")
    
    def test_reject_request(self):
        data = {"request_id": self.join_request.id, "action": "reject"}
        response = self.client.post("/teams/manage-requests/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.join_request.refresh_from_db()
        self.assertEqual(self.join_request.status, "REJECTED")
