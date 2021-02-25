#WAP which accept one number from user and return its factorial.
def fact(num):
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	return fact
def main():
	print("--Application to calculate factorial of a number--")
	Number=int(input("Enter any number :"))
	print(fact(Number))

if __name__=="__main__":
	main()
