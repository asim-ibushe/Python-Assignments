#WAP which accept one number and display pattern.
def Pattern(num):
	for row in range(num,-1,-1):
		for col in range(row):
			print("*",end="  ")
		print("") 
def main():
	print("--Application to print specific pattern---")
	Number=int(input("Enter any Number :"))
	Pattern(Number)
if __name__=="__main__":
	main()
