from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.ClientsView.as_view()),
    path("clients/<uuid:client_id>/", views.ClientsDetailView.as_view()),
]
