from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets, filters, generics, mixins, status


# Create your views here.

class SplViewSet(viewsets.ModelViewSet):
    lookup_field = 'join_code'
    queryset = models.Spl.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.SplSerializer


class TeamViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = models.Team.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.TeamSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = models.Project.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.ProjectSerializer
