import random
import math

from people import Character, my_character
from ships import Ship, my_ship_dict, my_ships_list, other_ship_dict, other_ships_list
from cargo import Cargo, my_cargo_dict, cargo_dict, all_cargo_list

#This is the beginning to a text based game where you purchase, furnish, and fight a pirate ship against other ships
current_port = "Nassau"

#This is the main character's ship
ship1 = {}

#The ship2 is an enemy ship, it is randomized below to randomly enounter ships at sea for battle
ship2 = random.choice(list(other_ship_dict.values()))

#This function returns user to the main menu when something is under construction still
def not_available():
	return_to_menu = input("Sorry these functions are not available yet, would you like to return to the menu? ")
	if return_to_menu == "yes":
		menu()
	else: 
		print("Very well, matey, thanks for playing!")
		exit()

#This function allows the user to choose from the ships they own before they leave port
def ship_choice():
	global ship1
	for number, key in enumerate(my_ship_dict):
		print(number + 1, key)
	ship_choice = my_ships_list[(int(input("\nSelect the number of the ship you would like to sail: ")) - 1)]
	print("You will sail {}, a fine vessel!\n".format(ship_choice))
	ship1 = my_ship_dict[ship_choice]
	return ship1

#This is the function used to try and flee battle, should take into account speed of ship and damage
def flee(fleeing, flee_from):
	global ship1
	global ship2
	chance = random.randint(1,10)
	if fleeing == ship1:
		if chance > (1 + (ship1.sails - ship2.sails)):
			print("You cannot outrun the enemy ship!\n")
			return_fire = math.ceil((ship2.attack / 100) * (ship2.gun_capacity / 2) + (random.randint(1,7) / chance))
			ship1.hp -= return_fire
			if ship1.hp > 0:
				print("You have {} in HP remaining after an enemy broadside.\n".format(ship1.hp))
				escape_attempt = input("Would you like to keep trying to escape? ")
				if escape_attempt == "yes": 
					flee(ship1, ship2)
		else: 
			print("You managed to escape and set sails for port!\n")
			print("Your ship's HP is currently {}. Consider staying in port for repairs.\n".format(ship1.hp))
			menu()
	if fleeing == ship2:
		if chance > (1 + (ship2.sails - ship1.sails)):
			give_them_hell = ("The enemy has unsuccessfully tried to escape! Shall we give them hell?!")
			if give_them_hell == "yes":
				volley = math.ceil((ship1.attack / 100) * (ship1.gun_capacity / 2) + (random.randint(1,7) / chance))
				ship2.hp -= volley
				print("Without mercy we have brought the enemy ship to {} HP after they have tried to escape.\n".format(ship2.hp))
				flee(ship2, ship1)
			else: 
				print("You have shown them mercy and returned to port. Honourable indeed!\n")
				menu()

#This function is for cannon firing while in battle. It deducts HP from the enemy ship.		
def battle(first_to_fire, second_to_fire):
	global ship1
	global ship2
	chance = random.randint(1,4)
	if first_to_fire.my_ship == True:
		if ship1.cannon_balls > ship1.gun_capacity: 
			volley = math.ceil((ship1.attack / 100) * (ship1.gun_capacity / 2) + (random.randint(1,7) / chance))
			ship2.hp -= volley
			ship1.cannon_balls -= (ship1.gun_capacity / 2)
			print("You damaged {} with a battle, leaving her with {} left in HP.\n".format(ship2.name, ship2.hp))
			if ship2.hp > 0:
				return_fire = math.ceil((ship2.attack / 100) * ship2.gun_capacity / 2) + (random.randint(1,7) / chance)
				ship1.hp -= volley
				ship2.cannon_balls -= (ship2.gun_capacity / 2)
				print("{} returned fire with a broadside, leaving you with {} left in HP.\n".format(ship1.name, ship1.hp))
				if ship1.cannon_balls > 0:
					fire_again = input("You have {} cannon balls left. Fire again?! ".format(ship1.cannon_balls))
					if fire_again == "yes":
						battle(ship1, ship2)
				else: 
					volley_warning()
			else: 
				print("You have sunk the enemy ship!")
				#HERE I NEED TO TAKE THE SHIP OUT OF THE SHIP LIST SO I CAN'T BATTLE IT AGAIN
				menu()
		elif ship1.cannon_balls < ship1.gun_capacity and ship1.cannon_balls > 0:
			volley = math.ceil((ship1.attack / 100) * (ship1.cannon_balls) + (random.randint(1,7) / chance))
			ship2.hp -= volley
			ship1.cannon_balls -= (ship1.gun_capacity / 2)
			if ship1.cannon_balls < 0:
				ship1.cannon_balls = 0
			if ship2.hp > 0:
				print("You damaged {} with a broadside but only have {} cannon balls left to spare! You have left the enemy with {} left in HP.\n".format(ship2.name, ship1.cannon_balls, ship2.hp))
				battle(ship2, ship1)
			else:
				print("The enemy ship has found her way to Davey Jones's locker!")
				#HERE I NEED TO TAKE THE SHIP OUT OF THE SHIP LIST SO I CAN'T BATTLE IT AGAIN
				menu()
		else:
			volley_warning()
	else:
		if ship2.cannon_balls < 0:
			ship2.cannon_balls = 0
			flee(ship2, ship1)
		else: 
			volley = math.ceil((ship2.attack / 100) * (ship1.gun_capacity / 2) + (random.randint(1,7) / chance))
			ship1.hp -= volley
			ship2.cannon_balls -= (ship2.gun_capacity / 2)
			print("{} damaged your ship with a broadside. You have {} HP left.\n".format(ship1.name, ship1.hp))
			if ship1.cannon_balls > 0: 
				return_fire = input("Shall we fire upon the enemy? ")
				if return_fire == "yes":
					battle(ship1, ship2)
				else: 
					flee(ship1, ship2)
			else:
				volley_warning()

def volley_warning():
	global ship1
	global ship2
	out_of_volley = input("You are out of cannon volley! Flee immediately or face certain death! Shall we flee?\n")
	if out_of_volley == "yes":
		flee(ship1, ship2)
	else: 
		chance = random.randint(1,4)
		volley = math.ceil((ship2.attack / 100) * (ship2.gun_capacity / 2) + (random.randint(1,7) / chance))
		ship1.hp -= volley
		print("The enemy mercilessly rains hell fire upon you, leaving you defenseless with {} HP.".format(ship1.hp))
		volley_warning()

#This function is the first encounter of ships on the sea. It alerts the player to a spotting of an enemy ship and randomizes who attacks first. 
def ship_encounter(ship1, ship2):
	if ship1 in my_ship_dict.values():
		print("You have spotted {}, an enemy {}.".format(ship2.name, ship2.ship_class))
		fire_first = random.randint(1,2)
		if fire_first == 2:
			battle(ship2, ship1)
		else:
			fire = input("Open your cannon ports and fire or turn tail and flee!\n"
				"1. FIRE AT WILL!\n"
				"2. Run away!!!!\n\n")
			if fire == "1":
				battle(ship1, ship2)
			else: 
				flee(ship1, ship2)
	else: 
		print("You must select a ship before entering battle! Choose a number from the list below.\n")
		ship_choice()
		ship_encounter(ship1, ship2)

#This is the purchase menu from which you can purchase cargo to sail to other ports
def purchase():
	if ship1 in my_ship_dict.values():
		while ship1.weight <= ship1.max_weight:
			print("\nFreight available for purchase: ")
			for number, key in enumerate(cargo_dict):
				print(number + 1, key)
			try:
				cargo_select = all_cargo_list[(int(input("""Select from the list of goods above to purchase items or type "port" to return to port: """)) -1)]
			except ValueError:
				menu()
			else: 
				cargo = cargo_dict[cargo_select]
				amount = int(input("How many crates of {} shall we take aboard? ".format(cargo_select)))
				if ship1.weight + (amount * cargo.weight) <= ship1.max_weight:
					my_cargo_dict[cargo_select] += amount
					print("Our current cargo manifest reads as follows:")
					print(my_cargo_dict)
					cargo_sum = sum(my_cargo_dict.values()) 
					cargo_weight = cargo_sum * cargo.weight  
					print("We are carrying ", cargo_weight, " lbs. of cargo at present.")
					ship1.change_weight(cargo_weight)
					print("{} ship now weighs: {}\n".format(ship1.name, ship1.weight))
				else: 
					print("Purchasing that much cargo will put your ship overweight, select a lesser ammount.")
		else: 
			print("Your ship is too heavy, you cannot add any more cargo.")
	else: 
		print("Are you planning to take your cargo by horse? Bring your ship back and will will load her up!")
		ship_choice()
		print("Now that you have a ship, how much would you like to load aboard your ship? ")
		purchase()

def menu():
	destiny = input("Welcome to the port of {}, {}! See the menu below to set a course to pirate infamy!\n\n"
	"1. Select a ship for sailing\n"
	"2. Customize or purchase ships\n"
	"3. Purchase goods for your ship\n"
	"4. Hire crew\n"
	"5. Sail for battle\n"
	"6. Embark on a trading voyage\n"
	"7. TEST \n\n".format(current_port, my_character.name))
	if destiny == "1":
		ship_choice()
		menu()
	elif destiny == "3":
		purchase()
		menu()
	elif destiny == "5": 
		if ship1 in my_ship_dict.values():
			ship_encounter(ship1, ship2)
		else:
			print("\nYou must select a ship before setting sail!")
			ship_choice()
			ship_encounter(ship1, ship2)
	elif destiny == "7": 
		from people import random_name; random_name()
		menu()
	else: 
		not_available()

#The below code starts the game through running a menu from which all other options are available
menu()
