import json


class ConfigManager:
    def __init__(self, config_path):
        self.config = config_path

    def get_config(self):
        with open(self.config, 'r') as file:
            config_data = json.load(file)
            return config_data
