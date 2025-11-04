from django.urls import path
from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("consultations/<int:consultation_id>/", views.consultation, name="consultation"),
    path("consultations", views.consultations, name="consultations"),
    path("nouvelle_consultation",views.nouvelle_consultation,name="nouvelle_consultation"),
    path("effacer_consultation/<int:consultation_id>/",views.effacer_consultation,name="effacer_consultation"),
    path("changer_consultation/<int:consultation_id>/",views.changer_consultation, name="changer_consultation"),
    path('', views.accueil, name="accueil"),
    path('nouveau_traitement/<int:consultation_id>/',views.nouveau_traitement,name="nouveau_traitement"),
    path('supprimer_traitement/<int:traitement_id>/',views.supprimer_traitement,name="supprimer_traitement"),
    path('modifier_traitement/<int:traitement_id>/',views.modifier_traitement,name="modifier_traitement")
]