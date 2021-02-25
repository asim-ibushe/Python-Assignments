#WAP which accept number from user and return addition of digits in that number.

def CalAdd_Digits(num):
	Total=0
	while (num != 0):
		Total+=int(num%10)
		num=int(num/10)
	return Total

def main():
	print("--Application to calculate Addition of Digits in a Number---")
	Number=int(input("Enter any Number :"))
	Iret=CalAdd_Digits(Number)
	print(f"Addition of Digits in a Number is {Iret}.")
if __name__=="__main__":
	main()
