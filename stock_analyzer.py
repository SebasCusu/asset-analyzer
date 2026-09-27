import numpy as np
import yfinance as yf

def obtener_datos_yf(ticker, fecha_inicio, fecha_fin):
    ticker_data = yf.download(ticker, start=fecha_inicio, end=fecha_fin)
    precios = ticker_data['Close'].values
    if not precios.any():
        return None
    else:
        return precios
    

def sacar_datos(precios):
    maximo = np.max(precios)
    minimo = np.min(precios)
    promedio = np.mean(precios)
    volatilidad = np.std(precios)
    return maximo, minimo, promedio, volatilidad


def main():
    ticker = input("Escribe el Ticker de el Activo Que Quieres Buscar: ").strip().upper()
    fecha_inicio = input("Escribe la Fecha de Inicio: ")
    fecha_fin = input("Escribe la Fecha de Fin: ")
    data = obtener_datos_yf(ticker, fecha_inicio, fecha_fin)

    maximo, minimo, promedio, volatilidad = sacar_datos(data)
    
    if data is None:
        print("Activo No Encontrado")
        
    else:
        print(f"Maximo: {maximo:.2f} USD")
        print(f"Minimo: {minimo:.2f} USD")
        print(f"Promedio: {round(promedio,2):.2f} USD") 
        print(f"Volatilidad: {volatilidad:.2f}%")
        
if __name__ == "__main__":
    main()