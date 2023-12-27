from django.urls import path

from .views import ProjectViews

urlpatterns = [
    path("", ProjectViews.projects_view),
]
