import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QStackedWidget, QWidget, QHBoxLayout, \
    QScrollArea, QMessageBox
from PyQt5.QtGui import QIcon
from home import Home
from learning import Learning
from admin import Admin
from register import Register
from admin_dashboard import AdminDashboard, AddContentForm
from user_login import UserLogin
from category_page import CategoryPage
from styles import load_stylesheet


def initialize_root_user():
    try:
        with open('data/users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    root_user = {"username": "root", "password": "mami12345", "role": "admin"}
    if root_user not in users:
        users.append(root_user)
        with open('data/users.json', 'w') as f:
            json.dump(users, f)


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FreeLearning Dashboard')
        self.setGeometry(100, 100, 800, 600)
        self.setObjectName("centralWidget")
        self.setStyleSheet(load_stylesheet())
        self.user_role = None
        self.initUI()

    def initUI(self):
        self.sidebar = QVBoxLayout()
        self.sidebar.setSpacing(10)

        self.btn_home = QPushButton("Inicio")
        self.btn_home.setIcon(QIcon("icons/home.png"))
        self.btn_home.clicked.connect(lambda: self.display(0))
        self.sidebar.addWidget(self.btn_home)

        self.btn_learning = QPushButton("Aprendizaje")
        self.btn_learning.setIcon(QIcon("icons/learning.png"))
        self.btn_learning.clicked.connect(lambda: self.display(1))
        self.sidebar.addWidget(self.btn_learning)

        self.btn_admin = QPushButton("Admin")
        self.btn_admin.setIcon(QIcon("icons/admin.png"))
        self.btn_admin.clicked.connect(lambda: self.display(2))
        self.sidebar.addWidget(self.btn_admin)

        self.btn_register = QPushButton("Registro")
        self.btn_register.setIcon(QIcon("icons/register.png"))
        self.btn_register.clicked.connect(lambda: self.display(3))
        self.sidebar.addWidget(self.btn_register)

        self.btn_user = QPushButton("Usuario")
        self.btn_user.setIcon(QIcon("icons/user.png"))
        self.btn_user.clicked.connect(lambda: self.display(5))
        self.sidebar.addWidget(self.btn_user)

        self.btn_logout = QPushButton("Logout")
        self.btn_logout.setIcon(QIcon("icons/logout.png"))
        self.btn_logout.clicked.connect(self.logout)
        self.sidebar.addWidget(self.btn_logout)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(Home())
        self.stack.addWidget(Learning())
        self.stack.addWidget(Admin(self.stack, self.navigate_to_learning, self.set_user_role))
        self.stack.addWidget(Register())
        self.stack.addWidget(AdminDashboard(self.open_add_content_form))  # Admin dashboard page
        self.stack.addWidget(UserLogin(self.navigate_to_learning))  # User login page

        self.sidebar_widget = QWidget()
        self.sidebar_widget.setLayout(self.sidebar)
        self.sidebar_widget.setFixedWidth(200)  # Anchura fija para el sidebar

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.stack)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.sidebar_widget)
        main_layout.addWidget(scroll_area)

        container = QWidget()
        container.setObjectName("centralWidget")
        container.setLayout(main_layout)

        self.setCentralWidget(container)
        self.resizeEvent(None)  # Adjust layout initially

    def resizeEvent(self, event):
        if self.width() < 600:  # Adjust width threshold as needed
            self.sidebar_widget.setFixedWidth(100)
            self.sidebar.setSpacing(5)
        else:
            self.sidebar_widget.setFixedWidth(200)
            self.sidebar.setSpacing(10)
        if event:
            event.accept()

    def display(self, index):
        if index == 4 and self.user_role != "admin":
            QMessageBox.warning(self, 'Acceso Denegado', 'Solo los administradores pueden acceder a esta página.')
            return
        self.stack.setCurrentIndex(index)

    def navigate_to_learning(self):
        self.display(1)

    def set_user_role(self, role):
        self.user_role = role

    def logout(self):
        self.user_role = None
        self.display(0)

    def open_add_content_form(self, category=None):
        self.add_content_form = AddContentForm(self.refresh_categories)
        if category:
            index = self.add_content_form.category_input.findText(category)
            if index != -1:
                self.add_content_form.category_input.setCurrentIndex(index)
        self.add_content_form.show()

    def refresh_categories(self):
        # Refresh category pages after adding new content
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            if isinstance(widget, CategoryPage):
                widget.initUI()


def main():
    initialize_root_user()
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
