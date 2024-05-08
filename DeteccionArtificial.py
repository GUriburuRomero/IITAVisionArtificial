from controller import Robot, Camera
import cv2
from ultralytics import YOLO
import numpy as np

# Inicializar Webots
robot = Robot()
time_step = int(robot.getBasicTimeStep())

# Obtener dispositivos
camera = robot.getDevice("camera1")
camera.enable(time_step)

# Inicializar YOLO
model = YOLO('C:/Users/CORE SYSTEM/Desktop/ModeloEntrenado.pt')

while robot.step(time_step) != -1:
    # Capturar imagen desde la cámara
    img = camera.getImage()
    img_width, img_height = camera.getWidth(), camera.getHeight()

    # Convertir la imagen a formato numpy
    img = np.frombuffer(img, np.uint8).reshape((img_height, img_width, 4))

    # Convertir la imagen de Webots a formato compatible con OpenCV (BGR)
    #img_cv2 = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

    # Ejecutar detección de objetos con YOLO
    results = model(img, show=False)

