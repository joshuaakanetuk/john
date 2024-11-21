from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO('yolov8m.pt')  # 'n' is for "nano" (smallest model)
results = model('1.jpg')  # Path to your image

# results.show()  # Display results