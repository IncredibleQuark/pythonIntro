from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "dmg": 50},
		 {"name": "Thunder", "cost": 30, "dmg": 70},
		 {"name": "Blizzard", "cost": 50, "dmg": 100},
		 {"name": "Water Gun", "cost": 2, "dmg": 25}]

player = Person(500, 80, 60, 35, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
