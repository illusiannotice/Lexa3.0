import json


class CfgAPI:
    def __init__(self):
        self.CONFIG_FILE = "../config/cmd.json"
        self.config = None

    def load_config(self):
        with open(self.CONFIG_FILE, "rb") as file:
            return json.load(file)


if __name__ == '__main__':
    api = CfgAPI()
    print(api.load_config())
