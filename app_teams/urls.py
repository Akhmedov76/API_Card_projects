from django.urls import path
from .views import *

urlpatterns = [
    path('teams/', ListCreateTeamView.as_view(), name='team-list'),
    path('teams/join/', JoinTeamView.as_view(), name='team-join'),
    path('teams/<int:team_id>/requests/', ListRequests.as_view(), name='team-requests'),
    path('teams/manage-requests/', ManageRequestsView.as_view(), name='team-manage-requests'),
]
