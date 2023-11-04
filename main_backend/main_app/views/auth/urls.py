from django.urls import path

from .views import AuthViews

urlpatterns = [
    path("signUp", AuthViews.sign_up_view)
]
