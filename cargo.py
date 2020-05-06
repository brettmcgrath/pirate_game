all_cargo_list = []
cargo_dict = {}
my_cargo_dict = {}

class Cargo():
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight 
		self.cost = cost 
		cargo_dict.update({self.name : self})
		my_cargo_dict.update({self.name : 0})
		all_cargo_list.append(name)

tobacco = Cargo("tobacco", 10, 10)
tea = Cargo("tea", 10, 10)
coffee = Cargo("coffee", 10, 10)
rum = Cargo("rum", 10, 10)

