# Requires: 
# 1. cv2 for accessing webcam (to install; pip install opencv-python)
# 2. numpy for handling image arrays (to install; pip install numpy)

# Script will;
# 1. Capture Video (or images) from the webcam.
# 2. Run until it is manually stopped, or the time limit set is reached.

# Imports
import cv2
import numpy as np
import threading
import time

# Video Capture Parameters
VIDEO_OUTPUT = "output_video.avi"
IMAGE_OUTPUT = "capture.jpg"
CAPTURE_MODE = "video"  # Set to "image" to capture a single frame
RECORD_SECONDS = 10 # Increase or decrease this value to record for longer/shorter

# Function to Capture Video or Image
def capture_video():
    print(" Starting Camera...")
    cap = cv2.VideoCapture(0)  # 0 for default webcam

    if not cap.isOpened():
        print(" Error: Could not open webcam!")
        return

    if CAPTURE_MODE == "video":
        print(" Recording Video...")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, 20.0, (640, 480))

        start_time = time.time()
        while time.time() - start_time < RECORD_SECONDS:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow('Recording...', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out.release()
        print(f" Video Saved: {VIDEO_OUTPUT}")

    elif CAPTURE_MODE == "image":
        print(" Capturing Image...")
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(IMAGE_OUTPUT, frame)
            print(f" Image Saved: {IMAGE_OUTPUT}")

    cap.release()
    cv2.destroyAllWindows()

# Run Video Functions
video_thread = threading.Thread(target=capture_video)

video_thread.start()

video_thread.join()

print(" Recording Complete!")
