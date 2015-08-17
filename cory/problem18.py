"""
Code to compute the solution to Project Euler problem 18. The problem asks
to compute the maximum sum possible by starting at the top of the pyramid
and working your way down in a line.
"""

string_of_inputs = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


matrix = []

#Separates the pyramid of values into a list of lists
for line in string_of_inputs.splitlines():
	list_of_values = [int(x) for x in line.split()]
	matrix.append(list_of_values)

z = len(matrix) - 1

while (z != 0):
	x = 0
	for num in matrix[z - 1]:
		matrix[z-1][x] += max(matrix[z][x], matrix[z][x+1])
		x += 1

	z -= 1

print(matrix[0])