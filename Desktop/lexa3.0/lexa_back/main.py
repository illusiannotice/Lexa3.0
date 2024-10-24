import config
from assistant import assistant

lexa = assistant.Assistant()
def main(input_text: str):
    lexa.voice.load_cfg()
    for name in lexa.names:
        if name in input_text:
            lexa.voice.speak()
            break
