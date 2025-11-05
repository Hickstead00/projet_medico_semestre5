from django.db import models

class Consultation(models.Model):
    patient_nom = models.CharField(max_length=40,null=False)
    patient_prenom = models.CharField(max_length=30,null=False)
    patient_genre = models.CharField(max_length=20,null=False)
    patient_age = models.IntegerField(null=False)
    description = models.TextField(null=False)
    date_consultation = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"Nom : {self.patient_nom}, Prenom : {self.patient_prenom}, Date de consultation : {self.date_consultation} "
    
class Traitement(models.Model):
    medicament = models.CharField(max_length=40,null=False)
    quantite = models.IntegerField(null=False)
    contenant = models.CharField(max_length=40,null=False)
    duree_en_jours = models.IntegerField(null=False)
    dosage = models.IntegerField(null=False)
    instructions_utilisations = models.TextField(null=False)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nom du medicament : {self.medicament}, Nombre de boite : {self.quantite}, Contenant : {self.contenant}, Durée du traitement : {self.duree_en_jours}, Dosage : {self.dosage}, Instructions d'utilisation : {self.instructions_utilisations}, Consultation : {self.consultation}"
    

class BlackMarketItem(models.Model):
    nom_item = models.CharField(max_length=40,null=False)
    prix = models.FloatField(null=False)
    image_url = models.URLField(null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f"Nom : {self.nom_medicament}, Prix : {self.prix}, Description : {self.description}"


