class Character:
    all_characters = []
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        Character.all_characters.append(self)