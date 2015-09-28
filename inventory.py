class Inventory:

	# organization: dictionary where keys = item names
	# each key has a list of length two [max, current]
	# contains max number of items permitted and
	# how many items we currently have

	def __init__(self):
		self.items = {}

	def __str__(self):
		if self.is_empty():
			return "Your inventory is empty!"
		s = "Inventory contents:\n" # fix later
		for item in self.items:
			if self.items[item][1] > 0:
				s += item
				s += " x" + str(self.items[item][1])
		return s

	def add(self, name, max_num):
		if name in self.items:
			if self.items[name][0] == self.items[name][1]:
				print("You can't add any more " + name + " to your inventory!")
			else:
				self.items[name][1] += 1
				print("You have added added " + name + " to your inventory!")
		else:
			self.items[name] = [max_num, 1]
			print("You have added added " + name + " to your inventory!")

	def use(self, name):
		if name in self.items and self.items[name][1] > 0:
			self.items[name][1] -= 1
		else:
			print("You don't have this!")

	def update_max(self, name, max_num):
		if name in self.items:
			self.items[name][0] = max_num
		else:
			print("You don't have this item!")

	def is_empty(self):
		for item in self.items:
			if self.items[item][1] > 0:
				return False
		return True

