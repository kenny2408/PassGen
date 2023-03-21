from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


def set_dark_theme(app):
    # Set style
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Base, QColor(15, 15, 15))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(193, 29, 29))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(134, 157, 180).lighter())
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)


def set_fonts(widget):
    # Set fonts
    font = QFont()
    font.setPointSize(16)

    widget.length_label.setFont(font)
    widget.generate_button.setFont(font)

    font.setPointSize(20)
    widget.password_label.setFont(font)
