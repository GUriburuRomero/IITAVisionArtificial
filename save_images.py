from controller import Robot, Camera
import cv2
import numpy as np
import keyboard
import os

# Inicializar Webots
robot = Robot()
time_step = int(robot.getBasicTimeStep())

# Obtener dispositivos
camera = robot.getDevice("camera1")
camera.enable(time_step)

h = camera.getHeight()
w = camera.getWidth()

# Inicializar YOLO
contador = 1

while robot.step(time_step) != -1:
    # Capturar imagen desde la cámara
    img = camera.getImage()
    if keyboard.is_pressed('s'):
        img = np.array(np.frombuffer(img, np.uint8).reshape((h, w, 4)))
        img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_LINEAR)
        #img = cv.colorChange(img, 'RGB')
        os.chdir("C:/Users/CORE SYSTEM/Desktop/Imagenes_tomadas") # Paste the path where u will save the image
        cv2.imwrite(str("imagen"+str(contador)+".png"), img)
        contador += 1