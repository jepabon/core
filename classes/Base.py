class Base(object):
    name = ""
    image = ""
    position = {
        "x": 0,
        "y": 0
    }
    size = {
        'width': 30,
        'height': 30
    }
    speed = 1

    def __init__(self, position=None):
        if position:
            self.position["x"] = position["x"]
            self.position["y"] = position["y"]

    def __str__(self):
        return self.name
