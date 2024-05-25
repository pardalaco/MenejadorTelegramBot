import multiprocessing
import imgDownloader
import bot
import signal

# Programa de inicio, al inicializar este programa, inicializa los programas necesarios para poner en marcha la aplicación

def stop_programs(signum, frame):
    print("\nCtrl + C detectado. Deteniendo los programas...")
    process1.terminate()
    process2.terminate()
    print("Programas detenidos correctamente.")

if __name__ == "__main__":
    print("Runing main.py")

    signal.signal(signal.SIGINT, stop_programs)  # Capturar la señal Ctrl + C

    # Crear procesos para ejecutar los programas
    process1 = multiprocessing.Process(target=bot.main) # Cada dia a las 12:05 ejecuta una rutina de creación de video, compresión de imagenes...
    process2 = multiprocessing.Process(target=imgDownloader.main) # Cada minuto desgarga una imagen

    # Iniciar los procesos
    process1.start()
    process2.start()

    # Esperar a que ambos procesos terminen
    process1.join()
    process2.join()

    print("Ambos programas han terminado de ejecutarse.")
