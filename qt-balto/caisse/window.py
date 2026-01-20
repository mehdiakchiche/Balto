from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class CaisseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caisse")

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Encaisser table"))

        self.setLayout(layout)