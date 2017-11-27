def square_of_sum(x):
	"""
	The square of the sum of the first x natural numbers
	"""
	return sum([val for val in range(x+1)])**2


def sum_of_squares(x):
	"""
	The sum of the squares of the first x natural numbers
	"""
	return sum([val**2 for val in range(x+1)])


def difference(x):
	"""
	the difference between the square of 
	the sum of the first ten natural numbers 
	and the sum of the squares of 
	the first ten natural numbers
	"""
	return square_of_sum(x) - sum_of_squares(x)
