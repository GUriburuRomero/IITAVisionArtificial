from ultralytics import YOLO

model = YOLO('yolov8m.pt')

results = model(source="0", show=True)

print(results)