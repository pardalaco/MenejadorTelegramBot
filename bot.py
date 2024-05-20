import telebot
import cv2
import numpy as np
import time
import imgDownloader
import yolo_object_detector.yolo_detector_function as yl
import time
import datetime

# Reemplaza 'TOKEN' con el token de tu bot proporcionado por BotFather
import TOKENS

# Crea una instancia del bot
bot = telebot.TeleBot(TOKENS.TOKEN)

# Variable para controlar el estado del saludo
saludo_activo = False

# Manejador para el comando '/start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "¡Hola! Soy un bot creado con telebot. ¡Bienvenido!")

# Manejador para el comando '/help'
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Puedes enviarme mensajes y yo te responderé. También puedes usar /start para comenzar y /help para obtener ayuda.")

# Manejador para el comando '/saludo'
@bot.message_handler(commands=['saludo'])
def handle_hola(message):
    global saludo_activo
    saludo_activo = True
    while saludo_activo:
        bot.send_message(message.chat.id, "Hola")
        time.sleep(5)

# Manejador para el comando '/stop_saludo'
@bot.message_handler(commands=['stop_saludo'])
def handle_stop_saludo(message):
    global saludo_activo
    saludo_activo = False
    bot.send_message(message.chat.id, "El saludo ha sido detenido.")

# Manejador para el comando '/foto'
@bot.message_handler(commands=['foto'])
def handle_photo(message):

    # Cargar la imagen con OpenCV
    image = imgDownloader.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
    image = imgDownloader.imagen_to_cv2(image)

    # Convertir la imagen a un formato adecuado para enviarla a través de Telegram
    image_encode = cv2.imencode('.jpg', image)[1]
    # Crear un array de bytes para enviar la imagen
    image_bytes = np.array(image_encode).tobytes()

    # Enviar la imagen
    bot.send_photo(message.chat.id, photo=image_bytes)

# Manejador para el comando '/foto_procesada'
@bot.message_handler(commands=['foto_procesada'])
def handle_photo(message):

    # Cargar la imagen con OpenCV
    image = imgDownloader.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
    image = imgDownloader.imagen_to_cv2(image)

    image_yl = yl.detect_objects(image)
    image = image_yl[0]
    labels = image_yl[1]

    # Convertir la imagen a un formato adecuado para enviarla a través de Telegram
    image_encode = cv2.imencode('.jpg', image)[1]
    # Crear un array de bytes para enviar la imagen
    image_bytes = np.array(image_encode).tobytes()

    # Enviar la imagen
    bot.send_photo(message.chat.id, photo=image_bytes)
    bot.send_message(message.chat.id, str(labels))

# Función para manejar el comando '/foto_procesada_loop'
@bot.message_handler(commands=['foto_procesada_loop'])
def handle_photo(message):
    print("Procesando...")
    bot.send_message(message.chat.id, "Procesando en loop")
    while True:  # Bucle infinito para ejecutar continuamente
        # Cargar la imagen con OpenCV
        image = imgDownloader.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
        image = imgDownloader.imagen_to_cv2(image)

        fecha_descarga = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Imagen descargada ({fecha_descarga})", end="\r")

        image_yl = yl.detect_objects(image)
        image = image_yl[0]
        labels = image_yl[1]

        # Verificar si hay algo en labels antes de enviar el mensaje
        if labels:
            # Convertir la imagen a un formato adecuado para enviarla a través de Telegram
            image_encode = cv2.imencode('.jpg', image)[1]
            # Crear un array de bytes para enviar la imagen
            image_bytes = np.array(image_encode).tobytes()

            # Enviar la imagen
            bot.send_photo(message.chat.id, photo=image_bytes)
            # bot.send_message(message.chat.id, str(labels))

        # Esperar un tiempo antes de la siguiente iteración para evitar sobrecargar el sistema
        time.sleep(60)  # Esperar 1 minuto antes de la próxima ejecución

# Manejador para mensajes de texto
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, "¡Hola! Soy un bot creado con telebot. Puedo responder a tus mensajes.")

print("Iniciando bot...")
# Ejecutar el bot
bot.polling()
