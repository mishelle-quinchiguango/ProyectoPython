import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def extraer_datos(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            productos = soup.find_all("div", class_="ui-search-layout--grid item-search") 
            data = []
            if productos:
                for producto in productos:
                    try:
                        nombre = producto.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link').text.strip()
                        precio = producto.find("span", class_="andes-money-amount__fraction").text.strip()
                        disponibilidad = 'Disponible'
                        data.append([nombre, precio, disponibilidad])
                    except AttributeError:
                        continue
            return data
        else:
            raise Exception(f"Error al hacer la solicitud: {response.status_code}")
