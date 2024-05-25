import telebot
import cv2
import numpy as np
import time
import imgTools
import yolo_object_detector.yolo_detector_function as yl
import datetime
import videoTools

# Reemplaza 'TOKEN' con el token de tu bot proporcionado por BotFather
import TOKENS

def main():
    # Crea una instancia del bot
    bot = telebot.TeleBot(TOKENS.TOKEN)

    # Variable para controlar el estado del saludo
    saludo_activo = False

    # Manejador para el comando '/start'
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        welcome_msg = "¡Hola! Soy un bot creado con telebot. ¡Bienvenido!\n\n"
        welcome_msg += "Si necesitas ayuda o información sobre cómo utilizar este bot, te recomiendo pulsar el comando /help."
        bot.send_message(message.chat.id, welcome_msg)

    # Manejador para el comando '/help'
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        help_txt = "ℹ️ **Bienvenido al Centro de Ayuda**\n\n"
        help_txt += "Aquí tienes una lista de comandos disponibles y su funcionalidad:\n\n"

        help_txt += "🚀 [/start](command:/start): Inicia la conversación con el bot.\n"
        help_txt += "📚 [/help](command:/help): Muestra esta información de ayuda sobre cómo utilizar el bot.\n"
        help_txt += "📷 [/foto](command:/foto): Solicita al bot una foto desde la cámara web en línea.\n"
        help_txt += "🖼️ [/foto_procesada](command:/foto_procesada): Solicita al bot una foto con detección de objetos.\n"
        help_txt += "🔄 [/last_person](command:/last_person): Solicita al bot foto de la ultima persona que ha pasado.\n\n"

        help_txt += "¡No dudes en utilizar estos comandos para interactuar conmigo! 😊"

        bot.send_message(message.chat.id, help_txt, parse_mode='Markdown')

    # Manejador para el comando '/foto'
    @bot.message_handler(commands=['foto'])
    def handle_photo(message):

        # Cargar la imagen con OpenCV
        image = imgTools.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
        image = imgTools.imagen_to_cv2(image)

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
        image = imgTools.descargar_imagen('https://www.acifalcoi.com/webcam/menejador.jpg')
        image = imgTools.imagen_to_cv2(image)

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


    # Función para manejar el comando '/last_person'
    @bot.message_handler(commands=['last_person'])
    def handle_photo(message):
        
        img = imgTools.obtener_ultima_imagen_cv()

        if img is None:
            bot.send_message(message.chat.id, "Aun no hay imagenes")
            return

        image_encode = cv2.imencode('.jpg', img)[1]
        # Crear un array de bytes para enviar la imagen
        image_bytes = np.array(image_encode).tobytes()

        # Enviar la imagen
        bot.send_photo(message.chat.id, photo=image_bytes)

    # Manejador para el comando '/video'
    @bot.message_handler(commands=['video'])
    def handle_video(message):
        # Ruta al video que deseas enviar
        video_path = videoTools.obtener_ultimo_video_grabado("./video/")

        if video_path is None:
            bot.send_message(message.chat.id, "Aun no hay videos")   
            return
        
        try:
            # Envía el video al chat desde donde se recibió el comando
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video)
        except Exception as e:
            bot.reply_to(message, f"No se pudo enviar el video. Error: {e}")

    # Manejador para mensajes de texto
    @bot.message_handler(func=lambda message: True)
    def handle_text(message):
        bot.reply_to(message, "¡Hola! Soy un bot creado con telebot. Puedo responder a tus mensajes.")

    print("Iniciando bot...")
    # Ejecutar el bot
    bot.polling()

if __name__ == "__main__":
    print("Iniciando bot")
    main()
