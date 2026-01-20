from django.db import models
from Restaurant.models import Table # importation du modèle de Table de mon application Restaurant

# Création des modèles de l'application de réservation

class Reservation(models.Model):
    nom = models.CharField(max_length=100) # Nom associé à la réservation
    email = models.EmailField() # Email associé à la réservation
    date = models.DateTimeField() # Date associée à la réservation
    nombre_personnes = models.IntegerField() # Nombre de personne associée à la réservation
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True) # Nombre de tables associées à la réservation
