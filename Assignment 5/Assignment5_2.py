#WAP using recursion.
def printNum(num):
	if num>0:
		printNum(num-1)
		print(num,end="  ")

def main():
	Number=int(input("Enter any number :"))
	print("Output:",end=" ")
	print(printNum(Number))

if __name__ == "__main__":
	main()
