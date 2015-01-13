
def foobar():
	palendrome = 0
	for x in range(999, 99, -1):
		for y in range(999, 99, -1):
			product = x*y
			if str(product) == str(product)[::-1] and product > palendrome:
				palendrome = product
	return palendrome
print foobar()
