from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout
from PyQt5.QtCore import Qt
import json

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("registerWidget")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        header = QLabel('Registro de Usuario')
        header.setObjectName("header")
        main_layout.addWidget(header)

        form_layout = QFormLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        form_layout.addRow(QLabel('Nombre de usuario:'), self.username_input)
        form_layout.addRow(QLabel('Contraseña:'), self.password_input)

        register_button = QPushButton("Registrar")
        register_button.setObjectName("btn_primary")
        register_button.clicked.connect(self.register)
        form_layout.addRow(register_button)

        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, 'Error', 'El nombre de usuario y la contraseña son requeridos.')
            return

        try:
            with open('data/users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        if any(user['username'] == username for user in users):
            QMessageBox.warning(self, 'Error', 'El nombre de usuario ya existe.')
            return

        users.append({"username": username, "password": password, "role": "user"})
        with open('data/users.json', 'w') as f:
            json.dump(users, f)

        QMessageBox.information(self, 'Éxito', 'Usuario registrado exitosamente.')
        self.username_input.clear()
        self.password_input.clear()
