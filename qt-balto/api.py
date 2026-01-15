import requests

BASE_URL = "http://127.0.0.1:8000"

def get_tables():
    return requests.get(f"{BASE_URL}/restaurant/tables/").json()

def get_produits():
    return requests.get(f"{BASE_URL}/restaurant/produits/").json()

def creer_commande(table_id):
    r = requests.post(
        f"{BASE_URL}/restaurant/commande/",
        data={"table_id": table_id}
    )
    return r.json()

def ajouter_plat(commande_id, produit_id, quantite):
    requests.post(
        f"{BASE_URL}/restaurant/ajout-plat/",
        json={
            'commande_id': commande_id,
            'produit_id': produit_id,
            'quantite': quantite
        }
    )

def retirer_plat(commande_id, produit_id):
    r = requests.post(
        f"{BASE_URL}/restaurant/retirer-plat/",
        data={
            "commande_id": commande_id,
            "produit_id": produit_id
        }
    )
    try:
        return r.json()
    except ValueError:
        return {"error": "Réponse invalide du serveur"}


def valider_commande(commande_id, table_id):
    return requests.post(
        f"{BASE_URL}/restaurant/valider-commande/",
        data={
            "commande_id": commande_id,
            "table_id": table_id
        }
    ).json()