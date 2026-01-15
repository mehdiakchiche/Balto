from django.http import JsonResponse
from .models import Facture
from Restaurant.models import Commande

def facture_table(request, table_id):
    commandes = Commande.objects.filter(table_id=table_id, statut='TERMINEE')
    total = sum(
        lc.produit.prix * lc.quantite
        for c in commandes
        for lc in c.lignecommande_set.all()
    )

    facture = Facture.objects.create(
        table_id=table_id,
        total=total
    )
    facture.commandes.set(commandes)

    return JsonResponse({'facture_id': facture.id, 'total': total})