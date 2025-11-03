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
