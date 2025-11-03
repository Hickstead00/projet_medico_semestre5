from django.urls import path
from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("consultations/<int:consultation_id>/", views.consultation, name="consultation"),
    path("consultations", views.consultations, name="consultations"),
]