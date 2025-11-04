from django.forms import ModelForm
from medico.models import *
from django import forms

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ["patient_nom","patient_prenom","patient_genre","patient_age","description"]
        labels = {
            "patient_nom" : "Nom patient",
            "patient_prenom" : "Prénom patient",
            "patient_genre" : "Genre du patient",
            "patient_age" : "Age du patient",
            "description" : "Description",
        }

class TraitementForm(ModelForm):
    class Meta:
        model= Traitement
        fields= ["medicament","quantite","contenant","duree_en_jours","dosage","instructions_utilisations"]
        labels ={
            "medicament" : "Médicament",
            "quantite":"Quantité",
            "contenant":"Contenant",
            "duree_en_jours":"Durée en jours",
            "dosage":"Dosage",
            "instructions_utilisations":"Instructions d'utilisations"
        }
