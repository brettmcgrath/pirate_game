my_ships_list = []
other_ships_list = []
my_ship_dict = {}
other_ship_dict = {}

#These are the classifications of ships allowed in the game
class Ship():
	def __init__(self, name, my_ship, ship_class, attack, hp, gun_capacity, sails, weight, max_weight, cannon_balls):
		self.name = name
		self.my_ship = my_ship
		self.ship_class = ship_class
		self.attack = attack
		self.hp = hp
		self.gun_capacity = gun_capacity
		self.sails = sails
		self.weight = weight
		self.max_weight = max_weight
		self.cannon_balls = cannon_balls
		if my_ship == True:
			my_ship_dict.update({self.name : self})
			my_ships_list.append(name)
		else: 
			other_ship_dict.update({self.name : self})
			other_ships_list.append(name)
	def change_weight(self, additional_weight):
		self.weight = additional_weight + self.weight

#This is a list of ships for use
trusty_crusty = Ship("The Trusty Crusty", True, "brig", 100, 100, 10, 2, 3000, 10000, 100)
old_slowpoke = Ship("The Old Slowpoke", True, "brig", 100, 100, 10, 2, 3000, 10000, 100)
red_reaper = Ship("The Red Reaper", True, "frigate", 100, 200, 22, 4, 6000, 20000, 100)
weary_wanderer = Ship("The Weary Wanderer", True, "sloop of war", 100, 150, 16, 3, 4500, 15000, 10)

#This is a list of potential enemy ships 
the_hispaniola = Ship("The Hispaniola", False, "brig", 100, 100, 10, 2, 3000, 10000, 100)
wakemaker = Ship("The Wakemaker", False, "brig", 100, 100, 10, 2, 3000, 10000, 100)

