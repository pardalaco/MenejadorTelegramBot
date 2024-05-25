import imgTools
import time
from datetime import datetime
import yolo_object_detector.yolo_detector_function as yl

while True:  # Bucle infinito para ejecutar continuamente
    # Cargar la imagen con OpenCV
    image = imgTools.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
    image = imgTools.imagen_to_cv2(image)


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
        imgTools.borrar_contenido_carpeta()
        imgTools.guardar_imagen_cv2(image)
        print()
        print(f"Imagen guardada ({fecha_descarga}).")


    # Esperar un tiempo antes de la siguiente iteración para evitar sobrecargar el sistema
    time.sleep(60)  # Esperar 1 minuto antes de la próxima ejecución