from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt


class DesktopWidget(QWidget):
    def __init__(self, text="Widget Çalışıyor"):
        super().__init__()

        # Widget davranışı
        self.setWindowFlags(
            Qt.FramelessWindowHint  # çerçevesiz
            | Qt.Tool  # taskbar / alt-tab yok
            | Qt.WindowStaysOnTopHint  # opsiyonel: her zaman üstte
            | Qt.WindowDoesNotAcceptFocus  # focus alma
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(1920 - 240 - 40, 40, 240, 80)  # sağ üst köşe

        # İçerik
        self.label = QLabel(text, self)
        self.label.setStyleSheet(
            """
            QLabel {
                background: rgba(50, 50, 50, 180);  /* yarı şeffaf koyu arka plan */
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 14px;
                border-radius: 15px;  /* yuvarlatılmış köşeler */
            }
            """
        )
        self.label.adjustSize()
