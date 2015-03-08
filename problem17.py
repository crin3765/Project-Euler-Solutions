""" 
Code to solve Project Euler #17. The problem statement is

If all of the number from 1 to 1000 were written out in words, how many letters would be used?

Note that this includes and, as in 143 = one hundred and forty three. 

"""

wordsUnderTwenty = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
wordsOverTwenty =  ["thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

total = 0

for num in range(1, 1001):
	numString = str(num)

	# For numbers 1-9 inclusive
	if len(numString) == 1:
		total += len(wordsUnderTwenty[num - 1])
		continue


	# Handles occurrences of 1-20 (when number is >= 10), including the teens.
	if int(numString[-2:]) <= 20:
		if (int(numString[-2:])) != 0:
			total += len(wordsUnderTwenty[int(numString[-2:]) - 1])

	# Handles occurences of 21 - 29 inclusive.
	elif int(numString[-2:]) <= 29:
		total += len("twenty")
		total += len(wordsUnderTwenty[int(numString[-1]) - 1])

	# Handles occurences of 30 - 99 inclusive. 
	else :
		total += len(wordsOverTwenty[int(numString[-2]) - 3])
		if int(numString[-1]) != 0:
			total += len(wordsUnderTwenty[int(numString[-1]) - 1])

	# Handles numbers 100-999 inclusive.
	if len(numString) >= 3:
		if int(numString[-3]) != 0:
			total += len("hundred")
			total += len(wordsUnderTwenty[int(numString[-3]) - 1])
		if int(numString[-2:]) != 0:
			total += len("and")	# Don't forget the 'and'

	if num == 1000:
		total += len("thousnad")
		total += len("one")
		


print(total)
