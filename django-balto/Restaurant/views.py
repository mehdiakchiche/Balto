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
    if request.method != "POST":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    table_id = request.POST.get("table_id")

    if not table_id:
        return JsonResponse({"error": "table_id manquant"}, status=400)

    commande = Commande.objects.create(
        table_id=table_id,
        statut="EN_COURS"
    )

    return JsonResponse({"commande_id": commande.id})

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

@csrf_exempt
def retirer_plat(request):
    if request.method != "POST":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    commande_id = request.POST.get("commande_id")
    produit_id = request.POST.get("produit_id")

    if not commande_id or not produit_id:
        return JsonResponse({"error": "Paramètres manquants"}, status=400)

    try:
        ligne = LigneCommande.objects.get(
            commande_id=commande_id,
            produit_id=produit_id
        )
        ligne.quantite -= 1
        if ligne.quantite <= 0:
            ligne.delete()
        else:
            ligne.save()

        return JsonResponse({"success": True})

    except LigneCommande.DoesNotExist:
        return JsonResponse({"error": "Produit non trouvé"}, status=404)


@csrf_exempt
def valider_commande(request):
    if request.method != "POST":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    commande_id = request.POST.get("commande_id")
    table_id = request.POST.get("table_id")

    if not commande_id or not table_id:
        return JsonResponse({"error": "Paramètres manquants"}, status=400)

    try:
        commande = Commande.objects.get(id=commande_id)
        commande.table_id = table_id
        commande.statut = "EN_CUISINE"
        commande.save()

        return JsonResponse({"success": True})

    except Commande.DoesNotExist:
        return JsonResponse({"error": "Commande introuvable"}, status=404)