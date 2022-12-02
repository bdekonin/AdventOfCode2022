f = open("input.txt", "r")

# Read the input file
input = f.read()

# Split the input into a list of strings
lines = input.splitlines()


# My Score
myscore = 0

# YXZ

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

# X = Lose
# Y = Draw
# Z = Win

def setInputOponent(input: str):
	if (input == "A"):
		return 1
	elif (input == "B"):
		return 2
	elif (input == "C"):
		return 3
	else:
		return "error"
def setInputPersonal(oponent: str, personal: str):
	if (personal == "Y"):
		return setInputOponent(oponent) # Return the same as the oponent
	elif (personal == "X"):
		if (oponent == "A"):
			return 3
		elif (oponent == "B"):
			return 1
		elif (oponent == "C"):
			return 2
		else:
			return "error"
	elif (personal == "Z"):
		if (oponent == "A"):
			return 2
		elif (oponent == "B"):
			return 3
		elif (oponent == "C"):
			return 1
		else:
			return "error"
	else:
		return "error"

def win(personal, oponent):
	if personal == oponent:
		return (personal + 3)

	elif personal == 1:
		if oponent == 3:
			return (personal + 6)
		else:
			return (personal + 0)
	elif personal == 2:
		if oponent == 1:
			return (personal + 6)
		else:
			return (personal + 0)
	elif personal == 3:
		if oponent == 2:
			return (personal + 6)
		else:
			return (personal + 0)


# Loop through the list of strings
for line in lines:
	# Split the string into a list of numbers
	splittedline = line.split()
	oponent = setInputOponent(splittedline[0])
	personal = setInputPersonal(splittedline[0], splittedline[1])

	myscore += win(personal, oponent)
	print (win(personal, oponent))


print ("Final score", myscore)