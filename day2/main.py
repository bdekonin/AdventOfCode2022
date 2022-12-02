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

def setInput(input: str):
	if (input == "A" or input == "X"):
		return 1
	elif (input == "B" or input == "Y"):
		return 2
	elif (input == "C" or input == "Z"):
		return 3
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
	oponent = setInput(splittedline[0])
	personal = setInput(splittedline[1])

	myscore += win(personal, oponent)
	print (win(personal, oponent))


print ("Final score", myscore)