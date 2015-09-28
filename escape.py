import os

# When you reach the end of your path - these are in a specific order on purpose
endgames = ["You gave up.", \
"You have managed to find a path that ends nowhere. Good luck with that.", \
"You draw a masterpiece which is bought for five million dollars. You decide to quit college and live off of that. Congratulations!", \
"You participate so much that the professor remembers your name for the rest of the semester. You still only get an A-.", \
"You have successfully escaped from class! Good luck passing without any notes."]

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
	state = ["sitting", 0]
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
# could and should possibly make this into a dictionary in the future
def get_options(state):
	options = ["quit"]
	if state == "sitting":
		options += ["listen", "gossip", "stand", "doodle"]
	if state == "listening":
		options += ["participate", "stop listening"]
	if state == "talking":
		options += ["stop talking", "keep talking"]
	if state == "standing":
		options += ["sit", "leave class"]
	if state == "drawing":
		options += ["stop drawing", "make masterpiece"]
	if state == "participating":
		options += ["stop participating", "keep participating!"]
	return options

# method takes two string parameters option and state and returns a string state and an exit code
# the program will only run the exit code if the state is "quit"
# could and should possibly make this into a dictionary in the future
def do_option(option, state):
	if option == "quit":
		return ["quit", 0]
	else:
		if state == "sitting":
			if option == "listen":
				return ["listening", 0]
			elif  option == "gossip":
				return ["talking", 0]
			elif option == "stand":
				return ["standing", 0]
			elif option == "doodle":
				return ["drawing", 0]
		if state == "talking":
			if option == "stop talking":
				return ["sitting", 0]
			elif option == "keep talking":
				return ["talking", 0]
		if state == "listening":
			if option == "stop listening":
				return ["sitting", 0]
			elif option == "participate":
				return ["participating", 0]
		if state == "standing":
			if option == "sit":
				return ["sitting", 0]
			elif option == "leave class":
				return ["quit", 4]
		if state == "drawing":
			if option == "stop drawing":
				return ["sitting", 0]
			elif option == "make masterpiece":
				return ["quit", 2]
		if state == "participating":
			if option == "stop participating":
				return ["listening", 0]
			elif option == "keep participating!":
				return ["quit", 3]
		return ["quit", 1]

escape()
