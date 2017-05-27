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

    def set_position(self, position):
        self.position["x"] = position["x"]
        self.position["y"] = position["y"]

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size