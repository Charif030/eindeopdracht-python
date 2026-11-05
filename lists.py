# Boodschappenlijst maken
boodschappen = ["Brood", "Melk", "Kaas", "Appels", "Bananen"]

# Twee producten toevoegen
boodschappen.append("Cola")
boodschappen.append("Chips")

# Een product verwijderen
boodschappen.remove("Kaas")

# Aantal producten tellen
print("Aantal producten:", len(boodschappen))

# Boodschappenlijst printen
print("Mijn boodschappenlijst:")
print(boodschappen)

# Controleren of melk op de lijst staat
if "Melk" in boodschappen:
    print("Melk staat op de lijst!")
else:
    print("Melk staat niet op de lijst!")
