from django.contrib import admin
from .models import Table, Categorie, Produit, Commande, LigneCommande

admin.site.register(Table)
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(LigneCommande)