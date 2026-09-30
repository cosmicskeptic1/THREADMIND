import json


class Wardrobe:
    def __init__(self, filename="wardrobe.json"):
        self.filename = filename
        self.data = self.load_wardrobe()

    def load_wardrobe(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def get_tops(self):
        return self.data["tops"]

    def get_bottoms(self):
        return self.data["bottoms"]

    def get_shoes(self):
        return self.data["shoes"]

    def get_all_items(self):
        return (
            self.data["tops"]
            + self.data["bottoms"]
            + self.data["shoes"]
        )