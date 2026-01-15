from django.db import models
from Restaurant.models import Table, Commande # Importation des modèles de l'application Restaurant

# Création des modèles de facturations


# 1) Modèle des comptes d'entreprise
class ClientEntreprise(models.Model):
    nom_entreprise = models.CharField(max_length=150) # Nom de l'entreprise 
    plafond_mensuel = models.DecimalField(max_digits=10, decimal_places=2) # Plafond mensuel des commandes de l'entreprise dans le restaurant

    def __str__(self):
        return self.nom_entreprise


# 2) Modèle de carte de paiement
class CarteRFID(models.Model):
    uid = models.CharField(max_length=50, unique=True) # Identifiant
    client_entreprise = models.ForeignKey(
        ClientEntreprise,
        on_delete=models.CASCADE # Entreprise liée à la carte / lié au modèle 1
    )

    def __str__(self):
        return self.uid


# 3) Modèle de facture
class Facture(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE) # Facture liée à la table / lié au modèle 1 de l'appli Restaurant
    commandes = models.ManyToManyField(Commande) # Commandes liées à la facture / relation ManyToMany = pour lier plusieurs éléments à une entrée
    date = models.DateTimeField(auto_now_add=True) # Date de la facture
    total = models.DecimalField(max_digits=10, decimal_places=2) # Total de la facture
    payee = models.BooleanField(default=False)
    client_entreprise = models.ForeignKey(
        ClientEntreprise,
        on_delete=models.SET_NULL, # Entreprise liée à la facture 
        null=True,
        blank=True
    )


# 4) Modèle de paiement
class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE) # facture liée au paiement / lié au modèle 3
    carte_rfid = models.ForeignKey(CarteRFID, on_delete=models.SET_NULL, null=True) # carte liée au paiement / lié au modèle 2
    montant = models.DecimalField(max_digits=10, decimal_places=2) # montant du paiement
    date = models.DateTimeField(auto_now_add=True) # date du paiement




