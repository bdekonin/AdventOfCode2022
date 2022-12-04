lines = open('input.txt').readlines()

partone = 0;
parttwo = 0;
for line in lines:
	first, second = line.split(',')
	f_value = first.split('-')
	s_value = second.split('-')

	a, b = int(f_value[0]), int(f_value[1])
	c, d = int(s_value[0]), int(s_value[1])

	if a <= c <= d <= b:
		partone += 1
	elif c <= a <= b <= d:
		partone += 1

	if a <= c <= b:
		parttwo += 1
	elif c <= a <= d:
		parttwo += 1

print('part 1: ', partone)
print('part 2: ', parttwo)
