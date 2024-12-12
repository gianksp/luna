# OFFLINE MODE
import json
import os
from utils import config
import vosk

# Load the Vosk model
dir = os.path.dirname(__file__)
model_path = os.path.join(dir, f"../../model/{config.get('speech-to-text-model')}")
model = vosk.Model(model_path)

# Initialize the recognizer with the model
recognizer = vosk.KaldiRecognizer(model, 16000)

def transcribe(audio):
    if recognizer.AcceptWaveform(audio):
        result = recognizer.Result()
        return json.loads(result)['text'].lower()