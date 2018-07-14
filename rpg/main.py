from classes.game import Person, BColors
from classes.magic import Spell

fire = Spell("Fire", 10, 50, "black")
thunder = Spell("Thunder", 30, 70, "black")
blizzard = Spell("Blizzard", 50, 100, "black")
meteor = Spell("Meteor", 44, 66, "black")
water_gun = Spell("Water Gun", 2, 25, "black")

cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(500, 80, 60, 35, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(800, 70, 45, 25, [])

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
		print("You attacked for", dmg, "points of damage.")
	elif index == 1:
		player.choose_magic()
		magic_choice = int(input("Choose magic:")) - 1
		# magic_dmg = player.generate_spell_damage(magic_choice)
		# spell = player.get_spell_name(magic_choice)
		# cost = player.get_spell_mp_cost(magic_choice)
		spell = player.magic[magic_choice]
		magic_dmg = spell.generate_damage()

		current_mp = player.get_mp()

		if spell.cost > current_mp:
			print(BColors.FAIL + "\nYou don't have enough MP\n" + BColors.ENDC)

		player.reduce_mp(spell.cost)
		enemy.take_damage(magic_dmg)
		print(BColors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), "magic damage" + BColors.ENDC)

	enemy_choice = 1
	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	print("Enemy attacks for", enemy_dmg, "\n")

	print("-----------------------------------------")
	print("Enemy HP:" + BColors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC + "\n")

	print("Your HP:" + BColors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.ENDC)
	print("Your MP:" + BColors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.ENDC)

	if enemy.get_hp() == 0:
		print(BColors.OKGREEN + "Your enemy has been defeated. You won!" + BColors.ENDC)
		running = False
	elif player.get_hp() == 0:
		print(BColors.FAIL + "Enemy has defeated you!" + BColors.ENDC)
		running = False

	# running = False
