import os
import requests

def consultar_servicio():
    # REQUERIMIENTO C: Uso de variables de entorno (Sin hardcoding)
    api_key = os.getenv('API_KEY_NASA') 
    
    # Validación por si la variable no está configurada
    if not api_key:
        print("Error: La variable de entorno API_KEY_NASA no está configurada.")
        return

    # Corrección: Uso de la variable api_key en lugar de la llave en texto plano
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        # REQUERIMIENTO C: Manejo robusto de errores
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lanza error si es 4xx o 5xx
        
        data = response.json()
        
        # REQUERIMIENTO C: Procesar ≥3 campos
        titulo = data.get('title', 'N/A')
        fecha = data.get('date', 'N/A')
        explicacion = data.get('explanation', 'N/A')[:100] # Primeros 100 caracteres
        
        print(f"--- REPORTE TÉCNICO ---")
        print(f"Título: {titulo}")
        print(f"Fecha: {fecha}")
        print(f"Resumen: {explicacion}...")

    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de Conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Error de Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error desconocido: {err}")

if __name__ == "__main__":
    consultar_servicio()