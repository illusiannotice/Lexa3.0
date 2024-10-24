from typing import Callable

from config import config
from stt import stt
from tts import tts

API = config.CfgAPI()
cfg = API.load_config()
greeting = "Слушаю"

class Assistant:
    def __init__(self):
        self.names = cfg["cmd"]["wake_words"]
        self.voice = tts.LexaTTS()

    @staticmethod
    def start(self, func: Callable):
        stt.record(stt.callback_vosk, func)