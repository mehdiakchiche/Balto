from django.db import models


# Création des modèles ici


# 1 Modèle de la Table
class Table(models.Model):
    numero = models.IntegerField(unique=True) # Numéro de la table
    capacite = models.IntegerField() # Nombres de places de la table
    position_x = models.IntegerField() # Position horizontale de la table sur ma page
    position_y = models.IntegerField() # Position verticale de ma table sur ma page

    def __str__(self):
        return f"Table {self.numero}" # Nom de l'instance. ex : "Table 6"
    

# 2 Modèle de la catégorie du produit
class Categorie(models.Model):
    nom = models.CharField(max_length=100) # Type de catégorie du plat

    def __str__(self):
        return self.nom # Nom de l'instance. ex : "Menu" , "Boisson"


# 3 Modèle du produit
class Produit(models.Model):
    nom = models.CharField(max_length=150) # Nom du produit 
    prix = models.DecimalField(max_digits=6, decimal_places=2) # Prix du produit
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE) # Catégorie du produit / lié au modèle 2
    stock = models.IntegerField() # stock du produit
    disponible = models.BooleanField(default=True) # disponibilité du produit

    def __str__(self):
        return self.nom


# 4 Modèle de gestion de la commande
class Commande(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE) # Numéro de table associé à la commande / lié au modèle 1
    date = models.DateTimeField(auto_now_add=True) # Date de la commande 

    STATUT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('EN_PREPARATION', 'En préparation'), # Choix du statut de la commande (en cuisine)
        ('TERMINEE', 'Terminée'),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES) # Statut final de la commande (en cuisine)

    def __str__(self):
        return("Commande {}".format(self.table))


# 5 Modèle du contenu de la commande 
class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE) # Commande associé à son contenu / lié au modèle 4
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE) # Produit associé à la commande / lié au modèle 3
    quantite = models.IntegerField() # Quantité de la commande

    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'), # Choix du statut de la commande (en caisse)
        ('PRET', 'Prêt'),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES) # Statut final de la commande (en caisse)

    def __str__(self):
        return f"{self.produit.nom} - Table {self.commande.table.numero}"



