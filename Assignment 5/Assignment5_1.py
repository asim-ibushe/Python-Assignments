#WAP using recursion which displays pattern..
def Display(num):
	if(num>0):
		print("*",end="  ")
		Display(num-1)


def main():
	Number=int(input("Enter any number :"))
	print("Output:",end=" ")
	print(Display(Number))

if __name__ == "__main__":
	main()
