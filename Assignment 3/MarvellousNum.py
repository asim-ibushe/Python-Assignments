def ChkPrime(num):
	for i in range(2,num):
		#print(i)
		if (num % i ==0):
			return False
	return True
