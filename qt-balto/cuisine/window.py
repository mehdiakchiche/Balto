from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class CuisineWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cuisine")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Plats en attente (affichage minimal)"))

        self.setLayout(layout)