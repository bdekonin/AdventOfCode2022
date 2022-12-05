lines = open('input.txt').readlines()



stacks = [[' '], ['W', 'R', 'F'],
			['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
			['P', 'M', 'Z', 'N', 'L'],
			['J', 'C', 'H', 'R'],
			['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
			['G', 'C', 'W', 'L', 'F', 'Z'],
			['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
			['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
			['J', 'W', 'H', 'G', 'R', 'S', 'V']]

# stacks = [[' '], ['Z', 'N'],
# 			['M', 'C', 'D'],
# 			['P']]

data = []
for line in lines:
	element = []
	for token in line.strip().split(" "):
		element.append(token)
	data.append(element)

for item in data:
	origin = int(item[3])
	destination = int(item[5])
	amount = int(item[1])
	for i in range(amount):
		copy = stacks[origin][-1]
		stacks[origin].pop()
		stacks[destination].append(copy)

solution = ""
for stack in stacks:
	solution += stack[-1]

print("Part One: ", solution)

stacks = [[' '], ['W', 'R', 'F'],
			['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
			['P', 'M', 'Z', 'N', 'L'],
			['J', 'C', 'H', 'R'],
			['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
			['G', 'C', 'W', 'L', 'F', 'Z'],
			['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
			['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
			['J', 'W', 'H', 'G', 'R', 'S', 'V']]

data = []
for line in lines:
	element = []
	for token in line.strip().split(" "):
		element.append(token)
	data.append(element)

for item in data:
	origin = int(item[3])
	destination = int(item[5])
	amount = int(item[1])
	temp = []
	for i in range(amount):
		copy = stacks[origin][-1]
		stacks[origin].pop()
		temp.insert(0, copy)
	for letter in temp:
		stacks[destination].append(letter)

solution = ""
for stack in stacks:
	solution += stack[-1]

print("Part Two: ", solution)
