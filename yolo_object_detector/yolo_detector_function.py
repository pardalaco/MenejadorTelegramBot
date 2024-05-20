import cv2
import numpy as np

# --------------- READ DNN MODEL ---------------
# Configuración del modelo
config = "yolo_object_detector/model/yolov3.cfg"
# Pesos
weights = "yolo_object_detector/model/yolov3.weights"
# Etiquetas
LABELS = open("yolo_object_detector/model/coco.names").read().strip().split("\n")
colors = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

# Cargar el modelo
net = cv2.dnn.readNetFromDarknet(config, weights)


def detect_objects(image_cv2):
    # --------------- LEER LA IMAGEN Y PREPROCESAMIENTO ---------------
    # Obtener las dimensiones de la imagen
    height, width, _ = image_cv2.shape

    # Crear un blob a partir de la imagen
    # - Escala la imagen a un rango de [0, 1]
    # - Redimensiona la imagen a 416x416 píxeles
    # - swapRB=True cambia los canales de color de BGR a RGB
    # - crop=False evita el recorte de la imagen
    blob = cv2.dnn.blobFromImage(image_cv2, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # --------------- DETECCIONES Y PREDICCIONES ---------------
    ln = net.getLayerNames() # Obtener los nombres de las capas del modelo
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()] # Obtener los nombres de las capas de salida no conectadas

    
    net.setInput(blob) # Establecer el blob como entrada al modelo
    outputs = net.forward(ln) # Realizar la detección y obtener las salidas

    # Listas para almacenar las cajas delimitadoras, las confidencias y los IDs de clase
    boxes = []
    confidences = []
    classIDs = []

    # Procesar cada salida de la detección
    for output in outputs:
        for detection in output:
            
            scores = detection[5:] # Obtener las puntuaciones de las clases
            classID = np.argmax(scores) # Obtener el ID de la clase con mayor puntuación
            confidence = scores[classID] # Obtener la confianza de la detección

            # Filtrar las detecciones con una confianza mínima de 0.5
            if confidence > 0.5:
                # Escalar las coordenadas de la caja a las dimensiones originales de la imagen
                box = detection[:4] * np.array([width, height, width, height])
                (x_center, y_center, w, h) = box.astype("int")
                x = int(x_center - (w / 2))
                y = int(y_center - (h / 2))

                # Agregar la caja, confianza e ID de clase a las listas
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Aplicar la supresión de no máximos para eliminar las cajas delimitadoras redundantes
    idx = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)

    label_count = {}

    # Dibujar las cajas y las etiquetas en la imagen
    if len(idx) > 0:
        for i in idx.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            # Obtener el color y la etiqueta de la clase detectada
            color = colors[classIDs[i]].tolist()
            text = "{}: {:.3f}".format(LABELS[classIDs[i]], confidences[i])
            # Dibujar la caja en la imagen
            cv2.rectangle(image_cv2, (x, y), (x + w, y + h), color, 2)
            # Dibujar la etiqueta en la imagen
            cv2.putText(image_cv2, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # Contar la etiqueta
            label = LABELS[classIDs[i]]
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1

    # Devolver la imagen procesada
    return image_cv2, label_count
