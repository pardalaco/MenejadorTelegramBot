import os

def obtener_ultimo_video_grabado(ruta_carpeta):

    # Verificar si la carpeta existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)


    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)

    # Filtrar solo los archivos con extensión .mp4
    videos = [archivo for archivo in archivos if archivo.endswith('.mp4')]

    # Si no hay videos en la carpeta, devuelve None
    if not videos:
        return None

    # Ordenar los videos por nombre de archivo (fecha de grabación)
    videos.sort(reverse=True)

    # Devolver la ruta del último video grabado
    return os.path.join(ruta_carpeta, videos[0])

