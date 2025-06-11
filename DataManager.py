import json
import os
from typing import Type, List


class DataManager:
    def __init__(self, folder):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def save(self, filename, data):
        with open(os.path.join(self.folder, filename), "w") as file:
            json.dump(data, file, indent=4)

    def load(self, filename):
        path = os.path.join(self.folder, filename)
        if not os.path.exists(path):
            self.save(self, filename, None)
        with open(path) as file:
            return json.load(file)

    def load_all(self):
        data = {}
        for file in os.listdir(self.folder):
            if file.endswith(".json"):
                data[file.replace(".json", "")] = self.load(file)
        return data
