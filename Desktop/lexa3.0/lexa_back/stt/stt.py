import time
import speech_recognition as sr
from faster_whisper import WhisperModel
from typing import Optional, Callable
from config import config
import wave
import vosk
import json

mic = sr.Microphone()
r = sr.Recognizer()
voice = WhisperModel("base.en", device="cpu", compute_type="int8")

def callback_vosk(recognizer, audio: sr.AudioData, f: Callable):
    vosk.SetLogLevel(-1)
    model = vosk.Model("../stt/model_ru")
    vosk_rec = vosk.KaldiRecognizer(model, audio.sample_rate)
    vosk_rec.AcceptWaveform(audio.get_wav_data())
    result = json.loads(vosk_rec.Result())
    text = result["text"]
    f(text)


def callback_whisper(recognizer, audio: sr.AudioData, f: Callable):
    with wave.open("../recs/rec.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.sample_width)
        wf.setframerate(audio.sample_rate)
        wf.writeframes(audio.get_wav_data())
    path = "../recs/rec.wav"
    segments, _ = voice.transcribe(path)
    segments = list(segments)
    transcript = segments[0].text
    f(transcript)
    print(transcript)


def record(callback: Callable, f: Callable):
    with mic as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(source, callback, f)
    print("listening...")
    while True:
        time.sleep(0.4)


if __name__ == "__main__":
    record(callback_vosk, ...)
