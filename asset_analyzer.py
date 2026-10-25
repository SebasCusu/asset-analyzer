import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_db:str, nombre_tabla:str):
        self.nombre_db = nombre_db
        self.nombre_tabla = nombre_tabla
        
    def crear_tabla(self):
        conn = sqlite3.connect(self.nombre_db)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS datos_fn (
                periodo TEXT,
                ticker TEXT,
                precio_maximo REAL,
                precio_minimo REAL,
                promedio REAL,
                volatilidad REAL
            )
        """)
        conn.commit()
        return conn,cur
    
    
class AssetAnalyzer:
    def __init__(self, ticker:str, fecha_inicio:str, fecha_fin:str):
        self.ticker = ticker
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin 
        
    def descargar_datos(self):
        df = yf.download(self.ticker, self.fecha_inicio, self.fecha_fin)
        if df.empty:
            print(f"{self.ticker} no encontrado")
            return None
        else:
            df_cierre = df["Close"]
            return df_cierre
        
    def analizar_datos(self,precios_cierre : int|float):
        precio_maximo = np.max(precios_cierre)
        precio_minimo = np.min(precios_cierre)
        precio_promedio = np.mean(precios_cierre)
        volatilidad = np.std(precios_cierre)
        return precio_maximo,precio_minimo,precio_promedio,volatilidad
    
    def guardar_datos(self,maximo,minimo,promedio,volatilidad):
        db = BaseDeDatos('my_db','datos_fn')
        conn, cur = db.crear_tabla()
        periodo = f"{self.fecha_inicio} - {self.fecha_fin}"
        cur.execute("""
            INSERT INTO datos_fn (periodo, ticker, precio_maximo, precio_minimo, promedio, volatilidad)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (periodo, self.ticker, maximo, minimo, promedio, volatilidad))
        conn.commit()
        
        cur.execute('SELECT * FROM datos_fn')
        datos = cur.fetchall()
        for row in datos:
            print(row)
        

def main():
    ticker = "TSLA"
    fecha_inicio = '2025-1-1'
    fecha_fin = '2026-1-1'
    asset1 = AssetAnalyzer(ticker, fecha_inicio, fecha_fin)
    datos = asset1.descargar_datos()
    if datos is not None:
        maximo, minimo, promedio, volatilidad = asset1.analizar_datos(datos)
        print(asset1.guardar_datos
        (round(maximo,2),round(minimo,2),round(promedio,2),round(volatilidad, 2)))
    else:
        print(asset1.descargar_datos())
        
if __name__ == "__main__":
    main()
