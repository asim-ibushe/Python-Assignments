#WA recursive programme which display 5 to 1.
def printNum(num):
	if num>0:
		print(num,end="  ")
		printNum(num-1)

def main():
	Number=int(input("Enter any number :"))
	print("Output:",end=" ")
	print(printNum(Number))

if __name__ == "__main__":
	main()		
