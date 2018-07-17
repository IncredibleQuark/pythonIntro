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

#Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 350 HP", 350)
elixer = Item("Elixer", "elixer", "Fully restores  HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 5},
				{"item": elixer, "quantity": 2},
				{"item": grenade, "quantity": 1}]

player1 = Person("Bob ", 1500, 355, 166, 200, player_magic, player_items)
player2 = Person("Dave ", 1800, 420, 150, 150, player_magic, player_items)
player3 = Person("Monica ", 1990, 228, 250, 50, player_magic, player_items)
enemy = Person("Roger ", 11000, 900, 520, 120, [], [])

players = [player1, player2, player3]

running = True

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.ENDC)

while running:
	print("================")
	print("NAME		HP									  	 	MP")
	for player in players:
		player.get_stats()

	enemy.get_enemy_stats()

	print("\n")

	for player in players:

		player.choose_action()
		choice = input("    Choose action:")
		index = int(choice) - 1

		if index == 0:
			dmg = player.generate_damage()
			enemy.take_damage(dmg)
			print("You attacked for", dmg, "points of damage.")

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
				enemy.take_damage(magic_dmg)
				print(BColors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), "magic damage" + BColors.ENDC)

		elif index == 2:
			player.choose_item()
			item_choice = int(input("    Choose item: ")) - 1

			if item_choice == -1:
				continue

			item = player.items[item_choice]["item"]

			if player.items[item_choice]["quantity"] == 0:
				print(BColors.FAIL + "\n" + "You don't have anymore " + str(player.items[item_choice]["item"].name) + BColors.ENDC)
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
				enemy.take_damage(item.prop)
				print(BColors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + BColors.ENDC)

	enemy_choice = 1
	target = random.randrange(0, len(players) - 1)
	enemy_dmg = enemy.generate_damage()
	players[target].take_damage(enemy_dmg)
	print("Enemy attacks " + BColors.FAIL + players[target].get_name() + BColors.ENDC + " for", enemy_dmg, "\n")

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
