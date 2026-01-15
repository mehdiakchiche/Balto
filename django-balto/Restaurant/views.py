from django.http import JsonResponse # Importation du module Json (Pour transférer des données entre serveur et app Web)
from .models import Table, Produit, Commande, LigneCommande # Importation des modèles 
from django.views.decorators.csrf import csrf_exempt
import json

def tables(request):
    data = list(Table.objects.values())
    return JsonResponse(data, safe=False)

def produits(request):
    data = list(
        Produit.objects.filter(disponible=True)
        .values('id', 'nom', 'prix', 'stock')
    )
    return JsonResponse(data, safe=False)

@csrf_exempt
def creer_commande(request):
    data = json.loads(request.body)
    commande = Commande.objects.create(
        table_id=data['table_id'],
        statut='EN_COURS'
    )
    return JsonResponse({'commande_id': commande.id})

@csrf_exempt
def ajouter_plat(request):
    data = json.loads(request.body)

    LigneCommande.objects.create(
        commande_id=data['commande_id'],
        produit_id=data['produit_id'],
        quantite=data['quantite'],
        statut='EN_ATTENTE'
    )

    return JsonResponse({'status': 'ok'})