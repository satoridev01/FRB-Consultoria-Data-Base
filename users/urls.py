from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<uuid:user_id>/", views.UsersDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
