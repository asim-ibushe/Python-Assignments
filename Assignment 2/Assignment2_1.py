#program which call all the functions from server module by accepting the parameters from user.

from Assignment2_1server import *

def main():
	print("--Basic Calculator Application--")
	Number1=int(input("Enter First number :"))	
	Number2=int(input("Enter Second number :"))
	print("Addition of two no is :",Add(Number1,Number2))
	print("Substraction of two no is :",Sub(Number1,Number2))
	print("Multiplication of two no is :",Mult(Number1,Number2))
	print("Division of two no is :",Div(Number1,Number2))

if __name__=="__main__":
	main()
