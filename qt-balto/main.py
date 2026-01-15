import sys
from PySide6.QtWidgets import QApplication

# On Choisit UNE interface à lancer
from serveur.window import ServeurWindow
from cuisine.window import CuisineWindow
from caisse.window import CaisseWindow

def main():
    app = QApplication(sys.argv)

    # A CHANGER POUR CHANGER D'INTERFACE
    window = ServeurWindow()
    #window = CuisineWindow()
    #window = CaisseWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()