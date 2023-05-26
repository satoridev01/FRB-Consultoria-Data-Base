from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<uuid:user_id>/", views.UsersDetailView.as_view()),
    path("users/login/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair")
]
