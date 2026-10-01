# Requires: 
# 1. pyaudio for recording (to install; pip install pyaudio)

# Script will;
# 1. Record Audio from the microphone.
# 2. Run until it is manually stopped, or the time limit set is reached.

# Imports
import pyaudio
import wave
import threading

# Audio Recording Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # CD Quality Audio
CHUNK = 1024
RECORD_SECONDS = 20 # Increase or decrease this value to record for longer/shorter
AUDIO_OUTPUT = "output_audio.wav"

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


# Run Audio function
audio_thread = threading.Thread(target=record_audio)

audio_thread.start()

audio_thread.join()

print(" Recording Complete!")
