#WAP which accept one number and display below pattern.
def Pattern(num):
	for i in range(1,num+1):
		for j in range(1,num+1):
			print(j,end="  ")
		print("")

def main():
	print("--Application to print specific pattern---")
	Number=int(input("Enter any Number :"))
	Pattern(Number)
if __name__=="__main__":
	main()
