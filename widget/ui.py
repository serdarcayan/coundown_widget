from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt


class DesktopWidget(QWidget):
    def __init__(self, text="Widget Çalışıyor"):
        super().__init__()

        # Widget davranışı
        self.setWindowFlags(
            Qt.FramelessWindowHint  # çerçevesiz
            | Qt.Tool  # taskbar / alt-tab yok
            | Qt.WindowDoesNotAcceptFocus  # focus alma
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry((1920 - 220 - 40), 40, 500, 300)

        # İçerik
        self.label = QLabel(text, self)
        self.label.setStyleSheet(
            """
            QLabel {
                background: rgba(200, 200, 230, 50);
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 12px;
            }
        """
        )
        self.label.adjustSize()
