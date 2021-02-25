#WAP which contains one lambda function which accepts one parameter and return power of two.
power_2=lambda no:no*no
def main():
	Num=int(input("Enter any Number :"))
	print(f"{Num} to the power two is :",power_2(Num))

if __name__=="__main__":
	main()
