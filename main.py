from character import Character
from items import Item

import time




def print_slow(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.05)
    print()


# Text Adventure

# Intro to game
print_slow("Old man: Hello, stranger. Who might you be?")
x = str(input("Enter your name: "))

print_slow(f"{x} hmmm, well welcome to Aven")



player = Character(x, None, 100, 10, 5)

# Role Selection
print_slow("Old man: Hmmm... what kind of adventurer are you?")
time.sleep(1)
print("Select a role from the following options:")
print("1. Warrior | Health: 120, Strength: 15, Armor: 10")
time.sleep(0.05)
print("2. Mage | Health: 80, Strength: 20, Armor: 5")
time.sleep(0.05)
print("3. Rogue | Health: 90, Strength: 12, Armor: 8")
time.sleep(0.05)
print("4. Archer | Health: 95, Strength: 14, Armor: 7")
time.sleep(0.05)
print("5. Monk | Health: 110, Strength: 10, Armor: 12")
time.sleep(1)
role = int(input("Enter the number corresponding to your role: "))

# Player updates based on role selection
if role == 1:
    player.role = "Warrior"
    player.health += 20
    player.strength += 5
    player.armor += 5
elif role == 2:
    player.role = "Mage"
    player.health -= 10
    player.strength += 10
    player.armor -= 5
elif role == 3:
    player.role = "Rogue"
    player.health += 10
    player.strength += 5
    player.armor -= 5
elif role == 4:
    player.role = "Archer"
    player.health += 5
    player.strength += 7
    player.armor -= 3
elif role == 5:
    player.role = "Monk"
    player.health += 15
    player.strength += 3
    player.armor += 2


print_slow(
    "Oh... a " + player.role + "... I see."
)

if player.role in {"Warrior", "Rogue", "Archer"}:
    print_slow(
        f"Well, if you are a {player.role} then you will need" + 
        " a weapon. I don't have much but take a look."
    )
else:
    print_slow(
        f"Well, if you are a {player.role} then you will need" + 
        " a spell or an artifact. I don't have much but take a look."
    )

# Shop interaction
print_slow("The old man shows you his limited wares.")
print_slow("Choose an item to purchase:")

old_man_shop_items1 = [
    Item("Short Sword", 5, 3),
    Item("Axe", 7, 6),
]

for i, item in enumerate(old_man_shop_items1, start=1):
    print(f"{i}. {item.name} - {item.dmg} (Cost: {item.cost} gold)")