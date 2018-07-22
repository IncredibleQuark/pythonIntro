from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 10, 50, "black")
thunder = Spell("Thunder", 30, 70, "black")
blizzard = Spell("Blizzard", 50, 100, "black")
meteor = Spell("Meteor", 44, 66, "black")
water_gun = Spell("Water Gun", 2, 25, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 350 HP", 350)
elixer = Item("Elixer", "elixer", "Fully restores  HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, thunder, blizzard, cure]
player_items = [{"item": potion, "quantity": 5},
				{"item": elixer, "quantity": 2},
				{"item": grenade, "quantity": 1}]

player1 = Person("Bob ", 1500, 355, 166, 200, player_magic, player_items)
player2 = Person("Dave ", 1800, 420, 150, 150, player_magic, player_items)
player3 = Person("Monica ", 1990, 228, 250, 50, player_magic, player_items)

enemy1 = Person("Ork   ", 2500, 300, 100, 100, enemy_magic, [])
enemy2 = Person("Roger ", 11000, 900, 520, 120, enemy_magic, [])
enemy3 = Person("Ork   ", 2500, 300, 100, 100, enemy_magic, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.ENDC)

while running:
	print("================")
	print("NAME		HP									  	 	MP")
	for player in players:
		player.get_stats()

	for enemy in enemies:
		enemy.get_enemy_stats()

	print("\n")

	for player in players:

		player.choose_action()
		choice = input("    Choose action:")
		index = int(choice) - 1

		if index == 0:
			dmg = player.generate_damage()
			enemy = player.choose_target(enemies)

			enemies[enemy].take_damage(dmg)
			print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

			if enemies[enemy].get_hp() == 0:
				print(enemies[enemy].name.replace(" ", "") + " has died.")
				del enemies[enemy]

		elif index == 1:
			player.choose_magic()
			magic_choice = int(input("    Choose magic:")) - 1

			if magic_choice == -1:
				continue

			spell = player.magic[magic_choice]
			magic_dmg = spell.generate_damage()

			current_mp = player.get_mp()

			if spell.cost > current_mp:
				print(BColors.FAIL + "\nYou don't have enough MP\n" + BColors.ENDC)

			player.reduce_mp(spell.cost)

			if spell.type == "white":
				player.heal(magic_dmg)
				print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + BColors.ENDC)
			elif spell.type == "black":
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(magic_dmg)
				print(BColors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg),
					  "magic damage to" + enemies[enemy].name.replace(" ", "") + BColors.ENDC)

				if enemies[enemy].get_hp() == 0:
					print(enemies[enemy].name.replace(" ", "") + "has died.")
					del enemies[enemy]

		elif index == 2:
			player.choose_item()
			item_choice = int(input("    Choose item: ")) - 1

			if item_choice == -1:
				continue

			item = player.items[item_choice]["item"]

			if player.items[item_choice]["quantity"] == 0:
				print(BColors.FAIL + "\n" + "You don't have anymore " + str(
					player.items[item_choice]["item"].name) + BColors.ENDC)
				continue

			player.items[item_choice]["quantity"] -= 1

			if item.type == "potion":
				player.heal(item.prop)
				print(BColors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + BColors.ENDC)
			elif item.type == "elixer":
				if item.name == "MegaElixer":
					for i in players:
						i.hp = i.maxhp
						i.mp = i.maxmp
				else:
					player.hp = player.maxhp
					player.mp = player.maxmp
				print(BColors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + BColors.ENDC)

			elif item.type == "attack":
				enemy = player.choose_target(enemies)
				enemy.take_damage(item.prop)
				print(BColors.FAIL + "\n" + item.name + " deals", str(item.prop),
					  "points of damage to " + enemies[enemy].name.replace(" ", "") + BColors.ENDC)

				if enemies[enemy].get_hp() == 0:
					print(enemies[enemy].name.replace(" ", "") + " has died.")
					del enemies[enemy]

	# Enemy attack phase
	for enemy in enemies:

		enemy_choice = random.randrange(0, 2)

		if enemy_choice == 0:
			target = random.randrange(0, len(players) - 1)
			enemy_dmg = enemies[0].generate_damage()
			print(enemy.name.replace(" ", "") + " attacks " + BColors.FAIL + players[target].name.replace(" ", "") +
				  BColors.ENDC + " for:" + str(enemy_dmg))

			players[target].take_damage(enemy_dmg)
			print("Enemy attacks " + BColors.FAIL + players[target].get_name() + BColors.ENDC + " for", str(enemy_dmg),
				  "\n")
		elif enemy_choice == 1:
			spell, magic_dmg = enemy.choose_enemy_spell()
			enemy.reduce_mp(spell.cost)
			print("Enemy chose", spell.name, "damage is", magic_dmg)

			if spell.type == "white":
				enemy.heal(magic_dmg)
				print(BColors.OKBLUE + "\n" + spell.name + " heals " + enemy.name + "for", str(magic_dmg),
					  "HP." + BColors.ENDC)
			elif spell.type == "black":
				target = random.randrange(0, len(players) - 1)
				players[target].take_damage(magic_dmg)
				print(BColors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals " + str(
					magic_dmg),
					  "magic damage to " + BColors.FAIL + players[target].name.replace(" ", "") + BColors.ENDC)

				if players[target].get_hp() == 0:
					print(players[target].name.replace(" ", "") + "has died.")
					del players[target]

	# Check if battle is over
	defeated_enemies = 0
	defeated_players = 0

	for enemy in enemies:
		if enemy.get_hp() == 0:
			defeated_enemies += 1

	for player in players:
		if player.get_hp() == 0:
			defeated_players += 1

	# Check if player won
	if defeated_enemies == 2:
		print(BColors.OKGREEN + "Your enemy has been defeated. You won!" + BColors.ENDC)
		running = False

	# Check if enemy won
	elif defeated_players == 2:
		print(BColors.FAIL + "Enemy has defeated you!" + BColors.ENDC)
		running = False
