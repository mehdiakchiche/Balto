from django.urls import path
from . import views

# Urls pour mon application restaurant

urlpatterns = [
    path('tables/', views.tables),
    path('produits/', views.produits),
    path('commande/', views.creer_commande),
    path('ajout-plat/', views.ajouter_plat),
    path('retirer-plat/', views.retirer_plat),
    path('valider-commande/', views.valider_commande),
]