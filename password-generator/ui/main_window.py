from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QApplication

from gen_pass.password_generator import PasswordGenerator
from validation.validation import validate_password_length

from ui.styles import set_dark_theme, set_fonts


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setMinimumSize(400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.length_label = QLabel('Password length:')
        layout.addWidget(self.length_label)

        self.length_input = QLineEdit()
        layout.addWidget(self.length_input)

        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.password_label = QLabel()
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.password_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set styles and fonts
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        set_dark_theme(app)
        set_fonts(self)

    def generate_password(self):
        length_str = self.length_input.text()
        error_message = validate_password_length(length_str)
        if error_message:
            QMessageBox.warning(self, 'Invalid input', error_message)
            return
        length = int(length_str)
        generator = PasswordGenerator(length)
        password = generator.generate()
        self.password_label.setText(password)
