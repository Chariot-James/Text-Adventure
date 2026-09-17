class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def has_item(self, item):
        return item in self.items

    def list_items(self):
        return [item.name for item in self.items]