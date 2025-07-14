import random

class Bystander:
    _id_counter = 1

    def __init__(self, id=None, name="", base_escape_chance=0.6, traits=None):
        if id is None:
            self.id = Bystander._id_counter
            Bystander._id_counter += 1
        else:
            self.id = id
        self.name = name
        self.traits = traits if traits else []
        self.base_escape_chance = base_escape_chance
        self.adjusted_escape_chance = self.calculate_escape_chance()
    def calculate_escape_chance(self):
        chance = self.base_escape_chance
        if "elderly" in self.traits:
            chance -= 0.3
        if "disabled" in self.traits:
            chance -= 0.2
        if "child" in self.traits:
            chance -= 0.1
        if "athlete" in self.traits:
            chance += 0.2
        if "pregnant" in self.traits:
            chance -= 0.1
        if "young" in self.traits:
            chance += 0.2
            
        return max(0, min(1, chance))
    
    def decide(self):
        return "escape" if random.random() < self.adjusted_escape_chance else "stay"
    
    def status(self):
        return f"{self.name} ({', '.join(self.traits)}) – Escape chance: {self.adjusted_escape_chance:.0%}"