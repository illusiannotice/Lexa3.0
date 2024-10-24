import torch
import sounddevice as sd
from time import sleep

from typing import Optional

language: Optional[str] = None
model_id: Optional[str] = None
samplerate: Optional[int] = None
device = None
speaker: Optional[str] = None

class LexaTTS:

    @staticmethod
    def load_cfg(
                 speaker_p: str = "baya",
                 language_p: str = "ru",
                 model_id_p: str = "ru_v3",
                 device_p: str = "cpu",
                 samplerate_p: int = 48000):

        global language, model_id, samplerate, device, speaker

        language = language_p
        model_id = model_id_p
        samplerate = samplerate_p
        device = torch.device(device_p)
        speaker = speaker_p

    @staticmethod
    def speak(speech: str):
        model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                               model="silero_tts",
                               language=language,
                               speaker=model_id)[0]
        model.to(device)

        audio = model.apply_tts(text=speech,
                                speaker=speaker,
                                sample_rate=samplerate)

        sd.play(audio, samplerate)
        sleep(len(audio) / samplerate)


if __name__ == "__main__":
    voice = LexaTTS()
    voice.load_cfg()
    voice.speak("привет мир")

