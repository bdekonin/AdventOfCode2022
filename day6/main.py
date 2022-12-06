lines = open('input.txt').readlines()

def has_duplicate_chars(s: str):
	chars = set()
	for c in s:
		if c in chars:
			return True
		chars.add(c)

	return False

# Part 1
n = 0
marker = ''
for line in lines:
	while 1:
		marker = line[n:n+4]
		if marker == '':
			break
		n += 1
		if has_duplicate_chars(marker) == False:
			n += 3
			break

print("Part 1: ", n)

# Part 2
n = 0
marker = ''
for line in lines:
	while 1:
		marker = line[n:n+14]
		if marker == '':
			break
		n += 1
		if has_duplicate_chars(marker) == False:
			n += 13
			break

print("Part 2: ", n)
