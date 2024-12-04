from openai import OpenAI
import pygame
from io import BytesIO

client = OpenAI()

def speak(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )

    audio_bytes = response.content
    audio_stream = BytesIO(audio_bytes)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)