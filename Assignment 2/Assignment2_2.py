#WAP which accept one number and display * pattern with square matrix.
def PrintStar(num):
	for row in range(num):
		for col in range(num):
			print("*",end="  ")
		print("")

def main():
	count=int(input("Enter any Number :"))
	PrintStar(count)

if __name__=="__main__":
	main()
