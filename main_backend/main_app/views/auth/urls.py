from django.urls import path

from .views import AuthViews

urlpatterns = [
    path("signUp", AuthViews.sign_up_view),
    path("login", AuthViews.login_view)
]
