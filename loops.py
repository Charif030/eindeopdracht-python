# Monster en speler
monster_health = 150
player_damage = 25
aantal_aanvallen = 0

# De speler valt het monster aan
while monster_health > 0:
    monster_health = monster_health - player_damage
    aantal_aanvallen = aantal_aanvallen + 1

    if monster_health < 0:
        monster_health = 0

    print("Monster heeft nog", monster_health, "health")

print("Monster is verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)
