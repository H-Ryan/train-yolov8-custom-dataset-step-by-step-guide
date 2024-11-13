from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratches

# Use the model
results = model.train(data="AbsolutePathToTheConfigFile\\config.yaml", epochs=1)  # train the model, the path should be absolute in windows
