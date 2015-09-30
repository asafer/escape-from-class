import os
from inventory import *

# When you reach the end of your path - these are in a specific order on purpose
endgames = {"default": "You gave up.", \
"error": "You have managed to find a path that ends nowhere. Good luck with that.", \
"draw": "You draw a masterpiece which is bought for five million dollars. You decide to quit college and live off of that. Congratulations!", \
"smart": "You participate so much that the professor remembers your name for the rest of the semester. You still only get an A-.", \
"outside": "You have successfully escaped from class! Good luck passing without any notes."}

# when we want to tell the player something. Max one per state right now.
texts = {"sitting": "Maybe you should do something.", \
		"looking": "You see a person hanging out by the door. They look like they might talk to you if you give them some information.", \
		"LEVEL TWO": "The person seems pleased with the gossip. They point out a cool looking tunnel you could explore. And they give you a flashlight.", \
		"in tunnel": "You are in the tunnel. Suddenly, the entrance shuts behind you. Good thing you have a flashlight!"}

# now we can store things yay!
itory = None

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
	global itory
	os.system("clear")
	itory = Inventory()
	print("You are in class for an hour and a half. Good luck.")
	state = ["sitting", "default"]
	quit = 0
	while (not quit):
		print()
		if state[0] in texts:
			print(texts[state[0]])
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
	"participating": ["stop participating", "keep participating!"], \
	"outside": ["go back in", "look around"], \
	"looking": ["talk to person", "go back in"], \
	"LEVEL TWO": ["enter tunnel"], \
	"in tunnel": []} # add story here!!

	options = ["quit", "check inventory"]
	if state in states:
		options += states[state]
	return options

# method takes two string parameters option and state and returns a string state and an exit code
# the program will only run the exit code if the state is "quit"
# thinking about making inventory additions into a class for easier program reading
def do_option(option, state):
	global itory
	if option == "quit":
		return ["quit", "default"]
	elif option == "check inventory":
		print(itory)
		return [state, "default"]
	else:
		states = {"sitting": {"listen": ["listening", "default"], \
								"gossip": ["talking", "default"], \
								"stand": ["standing", "default"], \
								"doodle": ["drawing", "default"]}, \
					"talking": {"stop talking": ["sitting", "default"], \
								"keep talking": ["talking", "default", [(0, "valuable gossip", 1)]]}, \
					"listening": {"stop listening": ["sitting", "default"], \
								"participate": ["participating", "default"]}, \
					"standing": {"sit": ["sitting", "default"], \
								"leave class": ["outside", "default"]}, \
					"participating": {"stop participating": ["sitting", "default"], \
								"keep participating!": ["quit", "smart"]}, \
					"drawing": {"stop drawing": ["sitting", "default"], \
								"make masterpiece": ["quit", "draw"]}, \
					"outside": {"go back in": ["standing", "default"], \
								"look around": ["looking", "default"]}, \
					"looking": {"go back in": ["standing", "default"], \
								"talk to person": ["LEVEL TWO", "default", [(1, "valuable gossip"), (0, "flashlight", 1)]]}, \
					"LEVEL TWO": {"enter tunnel": ["in tunnel", "default"]}}
		if state in states and option in states[state]:
			value = states[state][option]
			if len(value) == 2: # don't do anything with inventory
				return value
			else: # do something with inventory (list of tuples)
				for tup in value[2]:
					if tup[0] == 0: # add
						itory.add(tup[1], tup[2])
					elif tup[0] == 1: # use
						success = itory.use(tup[1])
						if not success:
							return [state, "default"]
				return value[:2]
	return ["quit", "error"]

escape()
