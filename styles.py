def load_stylesheet():
    return """
    QWidget#centralWidget {
        background-color: #ecf0f1;
    }

    QLabel {
        font-family: 'Arial', sans-serif;
    }

    QPushButton {
        font-family: 'Arial', sans-serif;
        padding: 10px;
        border-radius: 5px;
    }

    QPushButton#btn_primary {
        background-color: #3498db;
        color: white;
        border: none;
    }

    QPushButton#btn_secondary {
        background-color: #2ecc71;
        color: white;
        border: none;
    }

    QPushButton#btn_warning {
        background-color: #e74c3c;
        color: white;
        border: none;
    }

    QVBoxLayout {
        margin: 20px;
    }

    QFormLayout {
        margin: 20px;
    }

    QLabel#header {
        font-size: 24px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
        text-align: center;
    }

    QLabel#subheader {
        font-size: 18px;
        color: #34495e;
        margin-bottom: 10px;
        text-align: center;
    }

    QChartView {
        padding: 10px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
    }

    QScrollArea {
        border: none;
    }

    QLineEdit {
        padding: 8px;
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        font-family: 'Arial', sans-serif;
    }
    """
