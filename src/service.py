
import pyaudio
import speech_to_text
import text_processor
import text_to_speech

# Initialize microphone stream
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def __main__():
    while True:
        audio_stream = stream.read(4000, exception_on_overflow = False)
        input_audio_transcribed = speech_to_text.transcribe(audio_stream)
        if input_audio_transcribed:
            gpt_text_reply = text_processor.reply(input_audio_transcribed)
            text_to_speech.speak(gpt_text_reply)

__main__()
