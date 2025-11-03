from django.urls import path
from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("consultations/<int:consultation_id>/", views.consultation, name="consultation"),
    path("consultations", views.consultations, name="consultations"),
    path("nouvelle_consultation",views.nouvelle_consultation,name="nouvelle_consultation"),
    path("effacer_consultation/<int:consultation_id>/",views.effacer_consultation,name="effacer_consultation"),
    path("changer_consultation/<int:consultation_id>/",views.modifier_consultation, name="changer_consultation")
]