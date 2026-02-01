import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from widget.ui import DesktopWidget
from widget.fetcher import Scraper

URL = "https://example.com"
XPATH = '//*[@id="price"]'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DesktopWidget("Yükleniyor...")
    widget.show()

    scraper = Scraper(URL, XPATH)

    def update():
        data = scraper.get_data()
        widget.label.setText(data)
        widget.label.adjustSize()

    # İlk veri çekme
    update()

    # 60 saniye aralıklarla güncelle
    timer = QTimer()
    timer.timeout.connect(update)
    timer.start(60_000)  # 60.000 ms = 60 saniye

    sys.exit(app.exec_())
