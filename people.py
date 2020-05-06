import random

#This isn't useful at the moment but will be when I set character attributes from which ownership of ships and money is based
class Character():
	def __init__(self, name, my_character, honor, gold):
		self.name = name
		self.my_character = my_character
		self.honor = honor
		self.gold = gold

athos_sangiovese = Character("Athos Sangiovese", True, 100, 1000)
my_character = athos_sangiovese

class Crew():
	def __init__(self, name, level, attack, hp): 
		self.name = name 
		self.level = level
		self.attack = attack
		self.hp = hp 

def random_name():
	english_first = ["James", "John", "Stewart", "Charles", "Abraham"]
	english_last = ["Johnson", "Smith", "Billings", "Stewart", "Carey", "Hancock", "Washington", "Silver", "Gold"]
	english_name = random.choice(english_first) + " " + random.choice(english_last)
	print(english_name)
