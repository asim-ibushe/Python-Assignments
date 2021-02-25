#WAP which accept one number from user and check whether number is prime or not.
def ChkPrime(num):
	for i in range(2,num):
		#print(i)
		if (num % i ==0):
			return False
	return True

def main():
	print("--Application to Check Number Prime or Not---")
	Number=int(input("Enter any Number :"))
	bret=ChkPrime(Number)
	if bret == True:
		print("Entered number is Prime")
	else:
		print("Entered number is Not a Prime Number")

if __name__=="__main__":
	main()
