# Speler kiest een class
player_class = "Warrior"

# Kijken welke class gekozen is
match player_class:
    case "Warrior":
        health = 150
        damage = 20

    case "Mage":
        health = 80
        damage = 35

    case "Archer":
        health = 100
        damage = 25

    case "Rogue":
        health = 90
        damage = 30

    case _:
        health = 0
        damage = 0
        print("Deze class bestaat niet!")

# Gegevens printen
if health > 0:
    print("Gekozen class:", player_class)
    print("Health:", health)
    print("Damage:", damage)
