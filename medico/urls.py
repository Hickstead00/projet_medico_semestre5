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
    path('modifier_traitement/<int:traitement_id>/',views.modifier_traitement,name="modifier_traitement"),
    path('black_market_confirm/', views.black_market_confirm, name='black_market_confirm'),
    path('black-market/', views.black_market, name='black_market'),
    path('black-market/panier/', views.panier, name='panier'),
    path('black-market/panier/ajouter/<int:item_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('black-market/panier/retirer-un/<int:item_id>/', views.retirer_un_du_panier, name='retirer_un_du_panier'),
    path('black-market/panier/ajouter-un/<int:item_id>/', views.ajouter_un_au_panier, name='ajouter_un_au_panier'),
    path('black-market/panier/retirer/<int:item_id>/', views.retirer_du_panier, name='retirer_du_panier'),
    path('black-market/panier/vider/', views.vider_panier, name='vider_panier'),
    path('black-market/panier/valider/', views.valider_achat, name='valider_achat'),
]