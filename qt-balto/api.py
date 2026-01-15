import requests

BASE_URL = "http://127.0.0.1:8000"

def get_tables():
    return requests.get(f"{BASE_URL}/restaurant/tables/").json()

def get_produits():
    return requests.get(f"{BASE_URL}/restaurant/produits/").json()

def creer_commande(table_id):
    return requests.post(
        f"{BASE_URL}/restaurant/commande/",
        json={'table_id': table_id}
    ).json()

def ajouter_plat(commande_id, produit_id, quantite):
    requests.post(
        f"{BASE_URL}/restaurant/ajout-plats/",
        json={
            'commande_id': commande_id,
            'produit_id': produit_id,
            'quantite': quantite
        }
    )