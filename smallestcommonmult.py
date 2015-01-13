def divisible(i):
	for x in range (20, 1, -1):
		if i%x != 0:
			return False 
	return True

i = 2520
while not divisible(i):
	i+=20

print i