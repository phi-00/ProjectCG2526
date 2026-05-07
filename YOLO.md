**Most Recent YOLO models:**
- YOLOv5 – by Ultralytics
    - Not officially by original YOLO authors
    - Very easy to use (PyTorch-based)
    - Different sizes: v5n, v5s, v5m, v5l, v5x
    - Became extremely popular
- YOLOv6 – by Meituan
    - Optimized for industrial applications
    - Good speed/accuracy tradeoff
- YOLOv7
    - Strong accuracy and speed
    - More complex architecture
- YOLOv8 – by Ultralytics
    - Very popular today
    - Supports detection, segmentation, classification
    - Easy API, great docs
    - Anchor-free design
- YOLOv9 / YOLOv10 (latest research direction)
    - Push efficiency and accuracy further
    - More experimental / cutting-edge

**Sizes:**
- Nano (n) -> fastest, lowest accuracy
- Small (s) -> lightweight
- Medium (m) -> balanced
- Large (l) -> high accuracy
- Extra Large (x) -> best accuracy, heavy

**Recommended (My opinion):**
- YOLOv8 (small or medium)
    - Easy to train and deploy
    - Strong performance
    - Great ecosystem

- YOLOv8n or YOLOv5n (if real-time speed is needed)
    - Runs on Raspberry Pi, Jetson, etc.
    - Lower accuracy but very fast

**To put on unreal engine:**
We could use python:
1º step:
´´´
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

results = model(frame)
´´´

2º step: Send frames from Unreal

In Unreal (C++ or Blueprint):
    - Capture camera using SceneCaptureComponent2D
    - Convert to image

3º step: Communication layer
Use:
    - TCP sockets (fastest)
    - REST API (easier)
    - ZeroMQ (clean architecture)

4º step: Draw detections in Unreal
- Use DrawDebugBox or UMG overlay
- Or spawn actors at detected locations

Link of the video i found to help:
https://www.youtube.com/watch?v=xpqiAvuAUfk