from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QListWidget, QListWidgetItem, QMessageBox, QInputDialog
)
from api import (
    get_tables, get_produits,
    creer_commande, ajouter_plat,
    retirer_plat, valider_commande
)


class ServeurWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serveur")

        self.table_selectionnee = None
        self.commande_id = None
        self.commande_validee = False
        self.commande_locale = {}

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Table"))
        self.init_tables()

        self.layout.addWidget(QLabel("Menu"))
        self.init_produits()

        self.layout.addWidget(QLabel("Commande en cours"))
        self.liste = QListWidget()
        self.layout.addWidget(self.liste)

        btn_ret = QPushButton("➖ Retirer")
        btn_ret.clicked.connect(self.retirer_selection)
        self.layout.addWidget(btn_ret)

        btn_val = QPushButton("✅ Valider commande")
        btn_val.clicked.connect(self.valider)
        self.layout.addWidget(btn_val)

        self.setLayout(self.layout)

    def init_tables(self):
        for table in get_tables():
            btn = QPushButton(f"Table {table['numero']}")
            btn.clicked.connect(lambda _, t=table: self.select_table(t))
            self.layout.addWidget(btn)

    def select_table(self, table):
        if self.commande_id:
            QMessageBox.warning(self, "Erreur", "Commande déjà en cours")
            return

        self.table_selectionnee = table
        result = creer_commande(table['id'])

        if "commande_id" not in result:
            QMessageBox.critical(self, "Erreur", "Impossible de créer la commande")
            return

        self.commande_id = result["commande_id"]

    def init_produits(self):
        self.produits = get_produits()
        for p in self.produits:
            btn = QPushButton(p['nom'])
            btn.clicked.connect(lambda _, prod=p: self.ajouter(prod))
            self.layout.addWidget(btn)

    def ajouter(self, produit):
        if not self.commande_id:
            QMessageBox.warning(
                self,
                "Erreur",
                "Veuillez sélectionner une table avant de commander"
            )
            return

        pid = produit['id']
        self.commande_locale[pid] = self.commande_locale.get(pid, 0) + 1
        ajouter_plat(self.commande_id, pid, 1)
        self.refresh()

    def retirer_selection(self):
        item = self.liste.currentItem()
        if not item:
            return

        nom = item.text().split(" x")[0]
        for p in self.produits:
            if p['nom'] == nom:
                pid = p['id']
                retirer_plat(self.commande_id, pid)
                self.commande_locale[pid] -= 1
                if self.commande_locale[pid] <= 0:
                    del self.commande_locale[pid]
                break
        self.refresh()

    def valider(self):
        if not self.commande_locale:
            QMessageBox.warning(self, "Erreur", "Commande vide")
            return

        tables = get_tables()
        items = [f"Table {t['numero']}" for t in tables]

        choix, ok = QInputDialog.getItem(
            self,
            "Choisir une table",
            "Table pour cette commande :",
            items,
            0,
            False
        )

        if not ok:
            return

        table = tables[items.index(choix)]

        QMessageBox.information(
            self,
            "Commande validée",
            f"Commande envoyée pour la table {table['numero']}"
        )

        self.commande_validee = True
        QMessageBox.information(self, "OK", "Commande envoyée en cuisine")

    def refresh(self):
        self.liste.clear()
        for pid, qte in self.commande_locale.items():
            nom = next(p['nom'] for p in self.produits if p['id'] == pid)
            self.liste.addItem(f"{nom} x{qte}")

    