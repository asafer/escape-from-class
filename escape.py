import os

# When you reach the end of your path - these are in a specific order on purpose
endgames = {"default": "You gave up.", \
"error": "You have managed to find a path that ends nowhere. Good luck with that.", \
"draw": "You draw a masterpiece which is bought for five million dollars. You decide to quit college and live off of that. Congratulations!", \
"smart": "You participate so much that the professor remembers your name for the rest of the semester. You still only get an A-.", \
"outside": "You have successfully escaped from class! Good luck passing without any notes."}

# now we can store things yay!
inventory = []

def get_valid_int(start, end, text):
	choice = -1
	try:
		choice = int(input(text))
	except ValueError:
		choice = -1
	else:
		if choice < start or choice >= end:
			choice = -1
	while (choice == -1):
		print("That was not an option!")
		try:
			choice = int(input(text))
		except ValueError:
			choice = -1
		else:
			if choice < start or choice >= end:
				choice = -1
	return choice

def escape():
	os.system("clear")
	print("You are in class for an hour and a half. Good luck.")
	state = ["sitting", "default"]
	quit = 0
	while (not quit):
		print("Your current state is:", state[0])
		print("What would you like to do next?")
		options = get_options(state[0])
		i = 0
		for option in options:
			i += 1
			print(str(i) + ": " + option)
		choice = get_valid_int(1, len(options)+1, "Type the number of your choice: ")
		state = do_option(options[choice-1], state[0])
		if state[0] == "quit":
			quit = 1
			print(endgames[state[1]])


# method takes a string parameter state and returns a list of string options
def get_options(state):
	states = {"sitting": ["listen", "gossip", "stand", "doodle"], \
	"listening": ["participate", "stop listening"], \
	"talking": ["stop talking", "keep talking"], \
	"standing": ["sit", "leave class"], \
	"drawing": ["stop drawing", "make masterpiece"], \
	"participating": ["stop participating", "keep participating!"]}

	options = ["quit", "check inventory"]
	if state in states:
		options += states[state]
	return options

# method takes two string parameters option and state and returns a string state and an exit code
# the program will only run the exit code if the state is "quit"
def do_option(option, state):
	global inventory
	if option == "quit":
		return ["quit", "default"]
	elif option == "check inventory":
		if len(inventory) == 0:
			print("Your inventory is empty!")
		else:
			print("Inventory contents:")
			[print(item) for item in inventory]
		return [state, "default"]
	else:
		states = {"sitting": {"listen": ["listening", "default"], \
					"gossip": ["talking", "default"], \
					"stand": ["standing", "default"], \
					"doodle": ["drawing", "default"]}, \
		"talking": {"stop talking": ["sitting", "default"], \
					"keep talking": ["talking", "default", 1, "valuable gossip"]}, \
		"listening": {"stop listening": ["sitting", "default"], \
					"participate": ["participating", "default"]}, \
		"standing": {"sit": ["sitting", "default"], \
					"leave class": ["quit", "outside"]}, \
		"participating": {"stop participating": ["sitting", "default"], \
					"keep participating!": ["quit", "smart"]}, \
		"drawing": {"stop drawing": ["sitting", "default"], \
					"make masterpiece": ["quit", "draw"]}}
		if state in states and option in states[state]:
			value = states[state][option]
			if len(value) == 2: # no addition to inventory
				return value
			else: # adding somthing to inventory
				if value[2] <= inventory.count(value[3]): # number of item allowed in inventory
					print("You can't add more", value[3], "to your inventory right now!")
				else:
					inventory += [value[3]] # item to add is in fourth slot
					print(value[3], "has been added to your inventory!")
				return value[:2]
	return ["quit", "error"]

escape()
