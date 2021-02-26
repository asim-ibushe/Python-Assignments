#WAP which accept number from user and return summation of its digits.
Sum=0
def DigiSumR(num):
	global Sum
	if num > 0:
		Sum+=int(num%10)
		DigiSumR(int(num/10))
	return Sum

def main():
	Number=int(input("Enter any Number :"))
	print("Output:",end=" ")
	print(DigiSumR(Number))

if __name__=="__main__":
	main()
