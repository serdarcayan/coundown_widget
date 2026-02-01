import requests
from lxml import html


class Scraper:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath

    def get_data(self):
        """
        Sayfadan XPath ile veri çeker
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.5993.118 Safari/537.36"
        }

        try:
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            return f"Hata: {e}"

        tree = html.fromstring(response.content)

        # XPath ile seç
        result = tree.xpath(self.xpath)
        if result:
            return (
                result[0].strip()
                if isinstance(result[0], str)
                else result[0].text_content().strip()
            )
        else:
            return "Veri bulunamadı"
