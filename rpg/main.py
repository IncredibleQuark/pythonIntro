from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "dmg": 50},
		 {"name": "Thunder", "cost": 30, "dmg": 70},
		 {"name": "Blizzard", "cost": 50, "dmg": 100},
		 {"name": "Water Gun", "cost": 2, "dmg": 25}]

player = Person(500, 80, 60, 35, magic)
enemy = Person(800, 70, 45, 25, magic)

running = True

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.ENDC)

while running:
	print("================")
	player.choose_action()
	choice = input("Choose action:")
	index = int(choice) - 1

	if index == 0:
		dmg = player.generate_damage()
		enemy.take_damage(dmg)
		print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

	enemy_choice = 1
	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

	# running = False
