import json
import os


class DataManager:
    def __init__(self, folder):
        self.folder = folder
        if not (os.path.exists(folder)):
            os.makedirs(folder, exist_ok=True)

    def save(self, filename, data):
        file_path = os.path.join(self.folder, filename)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, filename, default=None):
        path = os.path.join(self.folder, filename)
        if not os.path.exists(path):
            self.save(filename, default)
        with open(path) as file:
            return json.load(file)

    def load_all(self):
        data = {}
        for file in os.listdir(self.folder):
            if file.endswith(".json"):
                data[file.replace(".json", "")] = self.load(file)
        return data.items()
