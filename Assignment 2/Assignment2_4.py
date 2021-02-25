#WAP which accept one number from user and return addition of its factors.
def AddFact(num):
	Total=0
	for i in range(1,num):
		if num % i==0:
			#print(i)
			Total+=i
	return Total
def main():
	print("--App to print sum of all factors of Number--")
	Number=int(input("Enter any Number :"))
	print(AddFact(Number))
if __name__=="__main__":
	main()
