from django.db import models

class Consultation(models.Model):
    patient_nom = models.CharField(max_length=40,null=False)
    patient_prenom = models.CharField(max_length=30,null=False)
    patient_genre = models.CharField(max_length=20,null=False)
    patient_age = models.IntegerField(null=False)
    description = models.TextField(null=False)
    date_consultation = models.DateField(null=False)


    def __str__(self):
        return f"Nom : {self.patient_nom}, Prenom : {self.patient_prenom}, Date de consultation : {self.date_consultation} "


