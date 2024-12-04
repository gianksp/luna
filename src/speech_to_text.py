# OFFLINE MODE
import vosk
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Load the Vosk model
VOSK_MODEL = os.getenv("VOSK_MODEL")
dir = os.path.dirname(__file__)
model_path = os.path.join(dir, f"../model/{VOSK_MODEL}")
model = vosk.Model(model_path)

# Initialize the recognizer with the model
recognizer = vosk.KaldiRecognizer(model, 16000)

def transcribe(audio):
    if recognizer.AcceptWaveform(audio):
        result = recognizer.Result()
        return json.loads(result)['text'].lower()