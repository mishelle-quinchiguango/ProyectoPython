from scraping.extractor import Scraper
from analysis.processor import DataProcessor
from utils.decorators import tiempo_ejecucion

@tiempo_ejecucion
def obtener_datos_y_analizar(url, num_paginas):
    all_data = []
    for i in range(1, num_paginas + 1):
        pag_url = f"{url}_Desde_{i*48}"
        scraper = Scraper(pag_url)
        data = scraper.extraer_datos()
        all_data.extend(data)

    processor = DataProcessor(all_data)
    df = processor.crear_dataframe()
    processor.guardar_datos(df, "ProductosMercadoLibre.xlsx")
    df_cargado = processor.cargar_datos("ProductosMercadoLibre.xlsx")
    print(df_cargado)

# URL base y número de páginas a extraer
base_url = "https://listado.mercadolibre.com.ec/hogar-muebles-jardin-cocina/"
num_paginas = 5

obtener_datos_y_analizar(base_url, num_paginas)
