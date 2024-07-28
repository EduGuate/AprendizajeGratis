from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
import json


class CategoryPage(QWidget):
    def __init__(self, category):
        super().__init__()
        self.category = category
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        title = QLabel(f'Contenido de {self.category}')
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(title)

        contents = self.load_contents()

        for content in contents:
            content_title = QLabel(content['title'])
            content_title.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 10px;")
            layout.addWidget(content_title)

            content_body = QLabel(content['content'])
            content_body.setWordWrap(True)
            layout.addWidget(content_body)

        self.setLayout(layout)

    def load_contents(self):
        try:
            with open('data/contents.json', 'r') as f:
                contents = json.load(f)
                return [content for content in contents if content['category'] == self.category]
        except FileNotFoundError:
            return []
