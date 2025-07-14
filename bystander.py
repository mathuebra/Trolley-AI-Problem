import random

class Bystander:
    def __init__(self, id, base_escape_chance, traits=None):
        self.id = id
        self.traits = traits if traits else []
        self.base_escape_chance = self.calculate_escape_chance()
    