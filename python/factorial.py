def factorial(num):
	factorial_Total = 1
	while num > 0:
		factorial_Total *= num
		num -= 1
	return factorial_Total