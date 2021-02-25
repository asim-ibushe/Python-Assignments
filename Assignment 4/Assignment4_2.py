#WAP which contains one lambda function which accepts two parameters and return its multiplication.
mul=lambda num1,num2:num1*num2
def main():
	num1=int(input("Enter first Number :"))
	num2=int(input("Enter second Number :"))
	print("Multiplication is :",mul(num1,num2))

if __name__=="__main__":
	main()
