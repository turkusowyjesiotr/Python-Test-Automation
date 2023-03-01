import json


class JsonUtil:
    def __init__(self, file_path):
        self.path = file_path

    def get_json_data(self):
        with open(self.path, 'r') as file:
            json_data = json.load(file)
            return json_data
