#program which call all the functions from server module by accepting the parameters from user.

from Assignment2_1server import *

def main():
	print("--Basic Calculator Application--")
	Number1=int(input("Enter First number :"))	
	Number2=int(input("Enter Second number :"))
	print("Dashboard Options :\n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Exit")
	choice=0
	while choice<5:
		choice=int(input("Choose one option from Dashboard :"))
		if choice==1:
			print("Addition of two no is :",Add(Number1,Number2))
		elif choice==2:
			print("Substraction of two no is :",Sub(Number1,Number2))
		elif choice==3:
			print("Multiplication of two no is :",Mult(Number1,Number2))
		elif choice==4:
			print("Division of two no is :",Div(Number1,Number2))
		elif choice==5:
			break;
		else:
			print("Invalid Input choice!!!")
	print("Succesfully Terminated, Thank You !!!")

if __name__=="__main__":
	main()
