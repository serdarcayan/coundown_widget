import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

class DesktopWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Widget davranışı
        self.setWindowFlags(
            Qt.FramelessWindowHint |          # çerçevesiz
            Qt.Tool |                         # taskbar / alt-tab yok
            Qt.WindowDoesNotAcceptFocus       # focus alma
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(700, 40, 220, 70)

        # İçerik
        self.label = QLabel("Widget Çalışıyor", self)
        self.label.setStyleSheet("""
            QLabel {
                background: rgba(0, 0, 0, 140);
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 12px;
            }
        """)
        self.label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DesktopWidget()
    w.show()
    sys.exit(app.exec_())
