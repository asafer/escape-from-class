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

	options = ["quit"]
	if state in states:
		options += states[state]
	return options

# method takes two string parameters option and state and returns a string state and an exit code
# the program will only run the exit code if the state is "quit"
# could and should possibly make this into a dictionary in the future
def do_option(option, state):
	global inventory
	if option == "quit":
		return ["quit", "default"]
	else:
		if state == "sitting":
			if option == "listen":
				return ["listening", "default"]
			elif  option == "gossip":
				return ["talking", "default"]
			elif option == "stand":
				return ["standing", "default"]
			elif option == "doodle":
				return ["drawing", "default"]
		if state == "talking":
			if option == "stop talking":
				return ["sitting", "default"]
			elif option == "keep talking":
				if "gossip" in inventory:
					print("You have already learned enough information!")
				else:
					inventory += ["gossip"]
					print("You have learned a valuable piece of information!")
				return ["talking", "default"]
		if state == "listening":
			if option == "stop listening":
				return ["sitting", "default"]
			elif option == "participate":
				return ["participating", "default"]
		if state == "standing":
			if option == "sit":
				return ["sitting", "default"]
			elif option == "leave class":
				return ["quit", "outside"]
		if state == "drawing":
			if option == "stop drawing":
				return ["sitting", "default"]
			elif option == "make masterpiece":
				return ["quit", "draw"]
		if state == "participating":
			if option == "stop participating":
				return ["listening", "default"]
			elif option == "keep participating!":
				return ["quit", "smart"]
		return ["quit", "error"]

escape()
