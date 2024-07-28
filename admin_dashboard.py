from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QFormLayout, QLineEdit, QTextEdit, \
    QComboBox, QMessageBox, QScrollArea
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSeries, QBarSet, QBarCategoryAxis
from PyQt5.QtCore import Qt
import json


class AdminDashboard(QWidget):
    def __init__(self, open_add_content_form):
        super().__init__()
        self.open_add_content_form = open_add_content_form
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        title = QLabel('Admin Dashboard')
        title.setObjectName("header")
        main_layout.addWidget(title)

        # Add content button
        self.btn_add_content = QPushButton("Agregar Contenido")
        self.btn_add_content.setObjectName("btn_primary")
        self.btn_add_content.clicked.connect(self.open_add_content_form)
        main_layout.addWidget(self.btn_add_content)

        # Example grid with charts and add content button
        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)

        # Charts
        user_chart = self.create_pie_chart("Usuarios", {"Activos": 80, "Inactivos": 20})
        grid_layout.addWidget(user_chart, 0, 0)

        content_chart = self.create_bar_chart("Contenido", {"Letras": 10, "Números": 15, "Colores": 8})
        grid_layout.addWidget(content_chart, 0, 1)

        main_layout.addLayout(grid_layout)

        # Scroll area for categories
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        category_widget = QWidget()
        category_layout = QGridLayout()
        category_layout.setSpacing(20)

        categories = [
            "Letras", "Números", "Colores", "Animales",
            "Cuerpo Humano", "Familia y Amigos", "Profesiones",
            "Naturaleza y Medio Ambiente", "Frutas y Vegetales",
            "Educación Vial", "Juegos y Ejercicios"
        ]

        for index, category in enumerate(categories):
            button = QPushButton(category)
            button.setObjectName("btn_secondary")
            button.clicked.connect(lambda _, c=category: self.open_category(c))
            category_layout.addWidget(button, index // 2, index % 2)

        category_widget.setLayout(category_layout)
        scroll_area.setWidget(category_widget)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def create_pie_chart(self, title, data):
        series = QPieSeries()
        for key, value in data.items():
            series.append(key, value)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chartview = QChartView(chart)
        chartview.setStyleSheet("padding: 10px; border: 1px solid #bdc3c7; border-radius: 5px;")
        return chartview

    def create_bar_chart(self, title, data):
        series = QBarSeries()
        bar_set = QBarSet(title)
        categories = []

        for key, value in data.items():
            bar_set.append(value)
            categories.append(key)

        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        chartview = QChartView(chart)
        chartview.setStyleSheet("padding: 10px; border: 1px solid #bdc3c7; border-radius: 5px;")
        return chartview

    def open_category(self, category):
        self.open_add_content_form(category)


class AddContentForm(QWidget):
    def __init__(self, refresh_categories):
        super().__init__()
        self.setWindowTitle('Agregar Contenido')
        self.setGeometry(300, 300, 400, 300)
        self.refresh_categories = refresh_categories
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.title_input = QLineEdit()
        self.category_input = QComboBox()
        self.category_input.addItems([
            "Letras", "Números", "Colores", "Animales",
            "Cuerpo Humano", "Familia y Amigos", "Profesiones",
            "Naturaleza y Medio Ambiente", "Frutas y Vegetales",
            "Educación Vial", "Juegos y Ejercicios"
        ])
        self.content_input = QTextEdit()

        form_layout.addRow(QLabel('Título del Contenido:'), self.title_input)
        form_layout.addRow(QLabel('Categoría:'), self.category_input)
        form_layout.addRow(QLabel('Contenido:'), self.content_input)

        add_button = QPushButton("Agregar")
        add_button.setObjectName("btn_primary")
        add_button.clicked.connect(self.add_content)
        form_layout.addRow(add_button)

        layout.addLayout(form_layout)
        self.setLayout(layout)

    def add_content(self):
        title = self.title_input.text()
        category = self.category_input.currentText()
        content = self.content_input.toPlainText()

        if not title or not content:
            QMessageBox.warning(self, 'Error', 'El título y el contenido son requeridos.')
            return

        new_content = {
            "title": title,
            "category": category,
            "content": content
        }

        try:
            with open('data/contents.json', 'r') as f:
                contents = json.load(f)
        except FileNotFoundError:
            contents = []

        contents.append(new_content)
        with open('data/contents.json', 'w') as f:
            json.dump(contents, f)

        QMessageBox.information(self, 'Éxito', 'Contenido agregado exitosamente.')
        self.refresh_categories()
        self.close()
