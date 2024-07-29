import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def crear_dataframe(self):
        df = pd.DataFrame(self.data, columns=['Nombre', 'Precio', 'Disponibilidad'])
        # Limpiar y transformar los datos si es necesario
        df['Precio'] = df['Precio'].str.extract(r'(\d+,\d+|\d+)')
        #df['Precio'] = df['Precio'].str[3:]
        df['Precio'] = df['Precio'].str.replace(',', '.').astype(float)
        df = df.sort_values(by='Precio', ascending=False)
        return df

    def guardar_datos(self, df, filename):
        
        df.to_excel(filename, index=False, engine='openpyxl')
        #print(f"Datos guardados en {filename}")

    def cargar_datos(self, filename):
        return pd.read_excel(filename, engine='openpyxl')

