#WA recursive program which accept number from user and return its factorial.
Fact=1
def FactR(num):
	global Fact
	if num==0:
		return 1
	else:
		Fact=Fact*num
		FactR(num-1)
	return Fact

def main():
	Number=int(input("Enter any Number :"))
	print("Output:",end=" ")
	print(FactR(Number))

if __name__=="__main__":
	main()
