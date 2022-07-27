from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('spl', views.SplViewSet)
router.register('projects', views.ProjectViewSet)
router.register('teams', views.TeamViewSet)
app_name = 'splManager'

urlpatterns = [
    path('', include(router.urls)),

]
