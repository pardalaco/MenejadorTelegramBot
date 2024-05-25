# Bot de Telegram con detección de objetos

Este bot de Telegram utiliza la librería telebot para interactuar con los usuarios y ofrece funcionalidades para enviar fotos desde una cámara web en línea y realizar detección de objetos en esas imágenes utilizando YOLO (You Only Look Once).

## Funcionalidades

- **Saludo programado**: El bot puede saludar automáticamente cada cierto intervalo de tiempo.
- **Envío de fotos**: Los usuarios pueden solicitar al bot que les envíe una foto tomada desde una cámara web en línea.
- **Detección de objetos**: Además de enviar la foto, el bot puede realizar detección de objetos en la imagen y enviarla junto con las etiquetas de los objetos detectados.
- **Detección de objetos en bucle**: Se incluye la opción de realizar la detección de objetos en un bucle continuo, enviando imágenes con objetos detectados a intervalos regulares.

## Requisitos

Para ejecutar este bot, necesitarás tener instaladas las siguientes dependencias:

- telebot
- OpenCV (cv2)
- numpy
- imgDownloader
- yolo_object_detector

Puedes instalar estas dependencias utilizando pip y el archivo `requirements.txt` proporcionado.

## Configuración

Antes de ejecutar el bot, asegúrate de haber configurado el archivo TOKENS.py con el token de tu bot proporcionado por BotFather.

## Uso

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias usando `pip install -r requirements.txt`.
3. Ejecuta el script `bot.py` para iniciar el bot.
4. Interactúa con el bot a través de Telegram utilizando los comandos proporcionados.

## Comandos disponibles

- `/start`: Inicia la conversación con el bot.
- `/help`: Muestra información de ayuda sobre cómo utilizar el bot.
- `/foto`: Solicita al bot una foto desde la cámara web en línea.
- `/foto_procesada`: Solicita al bot una foto con detección de objetos.
- `/last_person`: Solicita al bot foto de la ultima persona que ha pasado.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un pull request o reportar problemas en el repositorio.

¡Diviértete usando este bot!

## Configuración adicional modelo de datos yolo

Antes de ejecutar el bot, asegúrate de realizar lo siguiente:

1. Descarga el archivo `yolov3.weights` desde el siguiente enlace: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights).
2. Pega el archivo descargado en la carpeta `/yolo_object_detector/models` dentro de este repositorio.

Este archivo `yolov3.weights` es necesario para el funcionamiento correcto del detector de objetos YOLO utilizado por el bot. Asegúrate de tenerlo en la ubicación especificada antes de ejecutar el bot.

## Configuración del Token del Bot

Antes de ejecutar el bot, asegúrate de realizar lo siguiente:

1. Obtén el token de tu bot de Telegram proporcionado por BotFather.
2. Abre el archivo `TOKENS.py` en la raíz del proyecto.
3. Reemplaza el valor de la variable `TOKEN` con tu token de bot obtenido en el paso anterior.

Es importante configurar correctamente el token del bot para que pueda interactuar con la API de Telegram. Asegúrate de haber realizado estos pasos antes de ejecutar el bot.

