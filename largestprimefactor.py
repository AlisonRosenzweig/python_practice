number = 600851475143
def is_prime(x):
	
	for y in range(2,int(x**.5+1)):
		if x % y == 0 :
			return False 
	return True 
sqrt = int(number**.5 + 1)
print sqrt

for x in range(3, sqrt) :
	if number % x == 0 :
		if is_prime(x):
			print x
		elif is_prime(number/x) :
			print number/x







	