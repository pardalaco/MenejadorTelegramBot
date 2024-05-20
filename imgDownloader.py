import requests
import os
from datetime import datetime
import time
import numpy as np
import cv2


def descargar_imagen(url):
    try:
        # Definir un User-Agent personalizado
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Realizar la solicitud GET a la URL con el User-Agent personalizado
        respuesta = requests.get(url, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # print("Imagen descargada exitosamente")

            return respuesta.content
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

def imagen_to_cv2(content):
    try:
        # Convertir los datos de la imagen en un array de bytes
        nparr = np.frombuffer(content, np.uint8)
        
        # Decodificar la imagen utilizando OpenCV
        imagen = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        return imagen
    except Exception as e:
        print("Ocurrió un error al procesar la imagen:", str(e))
