# Requires: 
# 1. pyaudio for recording (to install; pip install pyaudio)
# 2. cv2 for accessing webcam (to install; pip install opencv-python)
# 3. numpy for handling image arrays (to install; pip install numpy)

# Script will;
# 1. Record Audio from the microphone.
# 2. Capture Video (or images) from the webcam.
# 3. Run until it is manually stopped.

import cv2
import pyaudio
import wave
import numpy as np
import threading
import time

# Audio Recording Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # CD Quality Audio
CHUNK = 1024
RECORD_SECONDS = 10 # Increase or decrease this value to record for longer/shorter
AUDIO_OUTPUT = "output_audio.wav"

# Video Capture Parameters
VIDEO_OUTPUT = "output_video.avi"
IMAGE_OUTPUT = "capture.jpg"
CAPTURE_MODE = "video"  # Set to "image" to capture a single frame

# Function to Record Audio
def record_audio():
    print(" Recording Audio...")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save to File
    wf = wave.open(AUDIO_OUTPUT, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f" Audio Saved: {AUDIO_OUTPUT}")

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

# Run Both Functions in Parallel
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=capture_video)

audio_thread.start()
video_thread.start()

audio_thread.join()
video_thread.join()

print(" Recording Complete!")
