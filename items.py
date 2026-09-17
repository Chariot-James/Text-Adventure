class Item:
    def __init__(self, name, dmg, cost):
        self.name = name
        self.dmg = dmg
        self.cost = cost

    def use(self, target):
        target.health -= self.dmg  # Example effect: reduce target's health by item's damage
        print(f"{self.name} used on {target.name} for {self.dmg} damage!")