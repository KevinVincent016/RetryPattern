import random
import requests
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

# Función con Retry Pattern mejorado
@retry(
    stop=stop_after_attempt(5), 
    wait=wait_exponential_jitter(1, 5),
    retry=retry_if_exception_type((requests.exceptions.RequestException, Exception))
)
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Simula una API que podría fallar
    # url = "https://api.ejemplo.com/data"  # Simula una API que podría fallar
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error en la solicitud: {response.status_code}")
    
    return response.json()

# Llamar la función
if __name__ == "__main__":
    try:
        data = fetch_data()
        print("✅ Datos obtenidos:", data)
    except Exception as e:
        print("❌ No se pudo obtener datos después de varios intentos:", e)
