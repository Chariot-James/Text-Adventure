class Character:
    def __init__(self, name, role, health, strength, armor):
        self.name = name
        self.role = role
        self.health = health
        self.strength = strength
        self.armor = armor

    def attack(self, target):
        damage = self.strength
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def dead(self):
        print(f"{self.name} has died.")