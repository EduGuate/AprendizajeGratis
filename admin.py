from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout
from PyQt5.QtCore import Qt
import json

class Admin(QWidget):
    def __init__(self, stack, navigate_to_learning, set_user_role):
        super().__init__()
        self.stack = stack
        self.navigate_to_learning = navigate_to_learning
        self.set_user_role = set_user_role
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        header = QLabel('Inicio de Sesión de Admin')
        header.setObjectName("header")
        main_layout.addWidget(header)

        form_layout = QFormLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        form_layout.addRow(QLabel('Nombre de usuario:'), self.username_input)
        form_layout.addRow(QLabel('Contraseña:'), self.password_input)

        login_button = QPushButton("Iniciar sesión")
        login_button.setObjectName("btn_primary")
        login_button.clicked.connect(self.login)
        form_layout.addRow(login_button)

        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            with open('data/users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        for user in users:
            if user['username'] == username and user['password'] == password and user['role'] == "admin":
                self.set_user_role("admin")
                self.navigate_to_learning()
                return

        QMessageBox.warning(self, 'Error', 'Nombre de usuario o contraseña incorrectos.')
