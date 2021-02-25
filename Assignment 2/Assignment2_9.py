#WAP which accept number from user and return NOD in that number.
def CalNumber_Digit(num):
	count=0
	while (num != 0):
		num=int(num/10)
		#print(num)
		count+=1
	return count	


def main():
	print("--Application to calculate No of Digit---")
	Number=int(input("Enter any Number :"))
	Iret=CalNumber_Digit(Number)
	print(f"There are {Iret} No of Digit in a Number.")
if __name__=="__main__":
	main()
