import yfinance as yf
import numpy as np
import sqlite3

conn = sqlite3.connect('my_db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS datos_ticker (
        ticker TEXT,
        maximo REAL,
        minimo REAL,
        promedio REAL,
        volatilidad REAL
    )
''')
conn.commit()

class Asset:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def descargar_datos(self, start_date:int, end_date:int) -> float:
        datos = yf.download(self.nombre, start=start_date, end=end_date)
        if datos.empty:
            return None
        
        else:
            precios_cierre = datos["Close"].to_numpy().flatten()
            return precios_cierre
        
    def analizar_datos(self,precios):
        maximo = np.max(precios)
        minimo = np.min(precios)
        promedio = np.mean(precios)
        volatilidad = np.std(precios)
        return maximo,minimo,promedio,volatilidad
    
    def insertar_datos(self,maximo,minimo,promedio,volatilidad):
        cur.execute('''INSERT INTO datos_ticker
                    (ticker, maximo, minimo, promedio, volatilidad) VALUES (?, ?, ?, ?, ?)''',
                    (self.nombre, round(maximo,2), round(minimo,2), round(promedio,2), round(volatilidad,2)))
        conn.commit()
        
    def observar_datos(self):
        contenido = cur.execute('SELECT * FROM datos_ticker')
        if not contenido:
            print("No hay datos")
        else:
            datos = contenido.fetchall()
            for dato in datos:
                print(dato)
                

def main():
    asset1 = Asset("TSLA")
    precios = asset1.descargar_datos("2025-1-1","2026-1-1")
    if precios is not None:
        datos = asset1.analizar_datos(precios)
        maximo,minimo,promedio,volatilidad = datos
        asset1.insertar_datos(maximo,minimo,promedio,volatilidad)
        print(asset1.observar_datos())

    else:
        print("Hubo un error")

if __name__ == "__main__":
    main()