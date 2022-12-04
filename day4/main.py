lines = open('input.txt').readlines()

count = 0;
for line in lines:
	first, second = line.split(',')
	f_value = first.split('-')
	s_value = second.split('-')

	a, b = int(f_value[0]), int(f_value[1])
	c, d = int(s_value[0]), int(s_value[1])

	if a <= c <= d <= b:
		count += 1
	elif c <= a <= b <= d:
		count += 1

print(count)