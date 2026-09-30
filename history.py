import json
import os


class OutfitHistory:
    def __init__(self, filename="history.json"):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            return json.load(file)

    def save_history(self):
        with open(self.filename, "w") as file:
            json.dump(self.history, file, indent=4)

    def create_outfit_id(self, outfit):
        return (
            outfit["top"]["id"]
            + "-"
            + outfit["bottom"]["id"]
            + "-"
            + outfit["shoes"]["id"]
        )

    def add_outfit(self, outfit):
        outfit_id = self.create_outfit_id(outfit)

        if outfit_id not in self.history:
            self.history.append(outfit_id)
            self.save_history()

    def was_worn(self, outfit):
        outfit_id = self.create_outfit_id(outfit)

        return outfit_id in self.history