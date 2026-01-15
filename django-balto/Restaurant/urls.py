from django.urls import path
from . import views

# Urls pour mon application restaurant

urlpatterns = [
    path('tables/', views.tables),
    path('produits/', views.produits),
    path('commande/', views.creer_commande),
    path('produits/', views.ajouter_plat),
]