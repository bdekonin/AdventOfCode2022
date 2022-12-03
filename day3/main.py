lines = open('input.txt').readlines()

# Part 1
score = 0;
for line in lines:
	# split line in half
	first = line[:len(line)//2]
	second = line[len(line)//2:]

	for c in first:
		if second.find(c) != -1:
			if c.isupper():
				score += (ord(c) - 38)
				break;
			else:
				score += (ord(c) - 96)
				break;

print('part 1: ', score)

# Part 2
i = 0;
score = 0;
chunks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
for chunk in chunks:
	first = chunk[0]
	second = chunk[1]
	third = chunk[2]

	for c in first:
		if second.find(c) != -1:
			if third.find(c) != -1:
				if c.isupper():
					score += (ord(c) - 38)
					break;
				else:
					score += (ord(c) - 96)
					break;

print('part 2: ', score)

# A = 27
# B = 28
# C = 29
# D = 30
# E = 31
# F = 32
# G = 33
# H = 34
# I = 35
# J = 36
# K = 37
# L = 38
# M = 39
# N = 40
# O = 41
# P = 42
# Q = 43
# R = 44
# S = 45
# T = 46
# U = 47
# V = 48
# W = 49
# X = 50
# Y = 51
# Z = 52

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# h = 8
# i = 9
# j = 10
# k = 11
# l = 12
# m = 13
# n = 14
# o = 15
# p = 16
# q = 17
# r = 18
# s = 19
# t = 20
# u = 21
# v = 22
# w = 23
# x = 24
# y = 25
# z = 26
