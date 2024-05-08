from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')
model.train(data=r'C:\Users\CORE SYSTEM\Desktop\entrenar_img', epochs=20, imgsz=500)