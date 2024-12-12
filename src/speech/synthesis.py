from io import BytesIO
from utils import config
from openai import OpenAI
import pygame

client = OpenAI()

def speak(text):
    response = client.audio.speech.create(
        model=config.get("text-to-speech-model"),
        voice=config.get("text-to-speech-voice"),
        input=text
    )

    audio_bytes = response.content
    audio_stream = BytesIO(audio_bytes)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)