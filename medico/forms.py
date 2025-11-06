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
        fields= ["medicament","quantite","contenant","duree_en_jours","dosage","instructions_utilisations","objet_special"]
        labels ={
            "medicament" : "Médicament",
            "quantite":"Quantité",
            "contenant":"Contenant",
            "duree_en_jours":"Durée en jours",
            "dosage":"Dosage journalier",
            "instructions_utilisations":"Instructions d'utilisations",
            "objet_special":"Objet Black‑Market (optionnel)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limiter la liste aux items dont le stock > 0
        try:
            disponibles = BlackMarketItem.objects.filter(inventory__quantite__gt=0).order_by('nom_item')
            self.fields['objet_special'].queryset = disponibles
            self.fields['objet_special'].empty_label = "— Aucun —"
            # Afficher le stock dans les libellés via widget choices si besoin
            # Laisser queryset + label_from_instance simple pour rester générique
        except Exception:
            # En cas de migration incomplète, ne pas casser le formulaire
            pass
