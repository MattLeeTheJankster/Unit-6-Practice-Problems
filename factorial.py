def factorial(n):
	"""Takes an integer and returns that integer's factorial."""
	
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		

##### Main Program #####
print(factorial(4))
	
	