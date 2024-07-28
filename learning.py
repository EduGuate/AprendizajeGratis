import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame, QSizePolicy, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Learning(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        header = QLabel('Categorías de Aprendizaje')
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(header)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.load_categories()

        layout.addLayout(self.grid)
        self.setLayout(layout)

    def load_categories(self):
        categories = [
            {"name": "Letras y Alfabeto", "description": "Aprende las letras y el alfabeto.", "image": "images/letras.png"},
            {"name": "Números y Contar", "description": "Aprende los números y a contar.", "image": "images/numeros.png"},
            {"name": "Colores y Formas", "description": "Aprende los colores y las formas.", "image": "images/colores.png"},
            {"name": "Animales", "description": "Conoce diferentes animales.", "image": "images/animales.png"},
            {"name": "Cuerpo Humano", "description": "Descubre las partes del cuerpo humano.", "image": "images/cuerpo.png"},
            {"name": "Familia y Amigos", "description": "Aprende sobre la familia y los amigos.", "image": "images/familia.png"},
            {"name": "Profesiones", "description": "Conoce diferentes profesiones.", "image": "images/profesiones.png"},
            {"name": "Naturaleza y Medio Ambiente", "description": "Explora la naturaleza y el medio ambiente.", "image": "images/naturaleza.png"},
            {"name": "Frutas y Vegetales", "description": "Aprende sobre frutas y vegetales.", "image": "images/frutas.png"},
            {"name": "Educación Vial", "description": "Conoce las señales de tráfico y la educación vial.", "image": "images/vial.png"},
            {"name": "Juegos y Ejercicios", "description": "Diviértete con juegos y ejercicios.", "image": "images/juegos.png"}
        ]

        for index, category in enumerate(categories):
            category_widget = self.create_category_widget(category)
            self.grid.addWidget(category_widget, index // 2, index % 2)

    def create_category_widget(self, category):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout = QVBoxLayout()

        # Image
        image_label = QLabel()
        pixmap = QPixmap(category["image"])
        image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        # Name
        name_label = QLabel(category["name"])
        name_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px;")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)

        # Description
        description_label = QLabel(category["description"])
        description_label.setStyleSheet("font-size: 12px; margin-top: 5px;")
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(description_label)

        frame.setLayout(layout)
        frame.mousePressEvent = lambda event, cat=category["name"]: self.open_category(cat)
        return frame

    def open_category(self, category):
        QMessageBox.information(self, 'Categoría', f'Abrir categoría: {category}')
