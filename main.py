import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from widget.ui import DesktopWidget
from widget.fetcher import Scraper

# Site ve XPath
URL = "https://www.osym.gov.tr/TR,8797/takvim.html"
XPATH = "/html/body/form/div[3]/div/div[2]/div/div[31]/div[3]"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DesktopWidget("Yükleniyor...")
    widget.show()

    scraper = Scraper(URL, XPATH)

    def update():
        data = scraper.get_data()
        widget.label.setText(data)
        widget.label.adjustSize()

    update()  # açılışta hemen veri çek
    timer = QTimer()
    timer.timeout.connect(update)
    timer.start(60000)  # 60 saniye

    sys.exit(app.exec_())
