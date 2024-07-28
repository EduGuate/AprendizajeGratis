from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import json

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        header = QLabel('Bienvenido a FreeLearning')
        header.setObjectName("header")
        layout.addWidget(header)

        content_label = QLabel('Contenido de Aprendizaje')
        content_label.setObjectName("subheader")
        layout.addWidget(content_label)

        # Add charts in a scroll area to prevent stretching
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        charts_widget = QWidget()
        chart_layout = QGridLayout()
        chart_layout.setSpacing(20)

        user_chart = self.create_pie_chart("Distribución de Usuarios", {"Activos": 80, "Inactivos": 20})
        chart_layout.addWidget(user_chart, 0, 0)

        content_chart = self.create_bar_chart("Contenido por Categoría", self.load_content_data())
        chart_layout.addWidget(content_chart, 0, 1)

        charts_widget.setLayout(chart_layout)
        scroll_area.setWidget(charts_widget)

        layout.addWidget(scroll_area)
        self.setLayout(layout)

    def create_pie_chart(self, title, data):
        series = QPieSeries()
        for key, value in data.items():
            series.append(key, value)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        chartview.setMinimumSize(400, 300)
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
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_y = QValueAxis()
        axis_y.setTitleText("Cantidad")

        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        chartview.setMinimumSize(400, 300)
        chartview.setStyleSheet("padding: 10px; border: 1px solid #bdc3c7; border-radius: 5px;")
        return chartview

    def load_content_data(self):
        try:
            with open('data/contents.json', 'r') as f:
                contents = json.load(f)
        except FileNotFoundError:
            contents = []

        categories = [
            "Letras", "Números", "Colores", "Animales",
            "Cuerpo Humano", "Familia y Amigos", "Profesiones",
            "Naturaleza y Medio Ambiente", "Frutas y Vegetales",
            "Educación Vial", "Juegos y Ejercicios"
        ]
        content_data = {category: 0 for category in categories}
        for content in contents:
            category = content['category']
            if category in content_data:
                content_data[category] += 1

        return content_data
