import requests
import os
from datetime import datetime
import time
import numpy as np
import cv2
import yolo_object_detector.yolo_detector_function as yl
import shutil

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

def guardar_imagen_cv2(imagen_cv2, carpeta_base='./img/'):
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    

    
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta_base):
        os.makedirs(carpeta_base)
    
    # Obtener la hora actual
    hora_actual = datetime.now().strftime("%H-%M")
    
    # Crear el nombre del archivo con la hora actual
    nombre_archivo = f"{fecha_actual+"_"+hora_actual}.jpg"
    
    # Crear el nombre completo del archivo con la ruta de la carpeta
    nombre_archivo_completo = os.path.join(carpeta_base, nombre_archivo)
    
    # Guardar la imagen en formato JPG
    cv2.imwrite(nombre_archivo_completo, imagen_cv2)

def obtener_imagen_cv(ruta_carpeta="./img"):
    # Lista para almacenar los nombres de archivo de las imágenes
    imagenes = []
    
    # Verificar si la ruta proporcionada es un directorio
    if os.path.isdir(ruta_carpeta):
        # Recorrer todos los archivos en la carpeta
        for archivo in os.listdir(ruta_carpeta):
            # Verificar si el archivo es una imagen (extensión común)
            if archivo.endswith(".jpg") or archivo.endswith(".jpeg") or archivo.endswith(".png") or archivo.endswith(".gif"):
                # Agregar el nombre del archivo a la lista de imágenes
                imagenes.append(archivo)
    else:
        print("La ruta proporcionada no es un directorio válido.")
    
    if imagenes is None:
        return
    
    imagenes.sort()

    imagen_cv = cv2.imread(len(imagenes)-1)

    return imagen_cv

def borrar_contenido_carpeta(ruta_carpeta="./img/"):
    # Verificar si la ruta proporcionada es un directorio
    if os.path.isdir(ruta_carpeta):
        # Recorrer todos los elementos dentro de la carpeta
        for elemento in os.listdir(ruta_carpeta):
            ruta_elemento = os.path.join(ruta_carpeta, elemento)
            # Verificar si es un archivo
            if os.path.isfile(ruta_elemento):
                # Borrar el archivo
                os.unlink(ruta_elemento)
            # Si es un directorio
            elif os.path.isdir(ruta_elemento):
                # Borrar el directorio y su contenido recursivamente
                shutil.rmtree(ruta_elemento)
    else:
        print("La ruta proporcionada no es un directorio válido.")



while True:  # Bucle infinito para ejecutar continuamente
    # Cargar la imagen con OpenCV
    image = descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
    image = imagen_to_cv2(image)


    if(image is None):
        time.sleep(60)
        pass

    fecha_descarga = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Imagen descargada ({fecha_descarga}).", end="\r")

    image_yl = yl.detect_objects(image)
    image = image_yl[0]
    labels = image_yl[1]

    # Verificar si hay algo en labels antes de enviar el mensaje
    if 'person' in labels:
        borrar_contenido_carpeta()
        guardar_imagen_cv2(image)
        print()
        print(f"Imagen guardada ({fecha_descarga}).")


    # Esperar un tiempo antes de la siguiente iteración para evitar sobrecargar el sistema
    time.sleep(60)  # Esperar 1 minuto antes de la próxima ejecución