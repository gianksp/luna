import pyaudio
import speech.recognition as stt
import speech.synthesis as tts
import processor.gpt as gpt

# Initialize microphone stream
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def __main__():
    while True:
        input_audio_stream = stream.read(4000, exception_on_overflow = False)
        input_text_transcribed = stt.transcribe(input_audio_stream)
        if input_text_transcribed:
            gpt_text_reply = gpt.reply(input_text_transcribed)
            tts.speak(gpt_text_reply)

__main__()
