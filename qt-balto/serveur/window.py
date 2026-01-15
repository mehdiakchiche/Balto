from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from api import get_tables, get_produits, creer_commande, ajouter_plat

class ServeurWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serveur")

        layout = QVBoxLayout()
        self.commande_id = None

        for table in get_tables():
            btn = QPushButton(f"Table {table['numero']}")
            btn.clicked.connect(lambda _, t=table: self.select_table(t))
            layout.addWidget(btn)

        self.setLayout(layout)

    def select_table(self, table):
        self.commande_id = creer_commande(table['id'])['commande_id']

        for produit in get_produits():
            btn = QPushButton(produit['nom'])
            btn.clicked.connect(
                lambda _, p=produit: ajouter_plat(
                    self.commande_id, p['id'], 1
                )
            )
            self.layout().addWidget(btn)