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
- `/saludo`: Activa el saludo automático del bot.
- `/stop_saludo`: Detiene el saludo automático del bot.
- `/foto`: Solicita al bot una foto desde la cámara web en línea.
- `/foto_procesada`: Solicita al bot una foto con detección de objetos.
- `/foto_procesada_loop`: Activa el modo de detección de objetos en bucle.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir un pull request o reportar problemas en el repositorio.

¡Diviértete usando este bot!

