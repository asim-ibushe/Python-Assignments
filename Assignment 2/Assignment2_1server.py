#create a module named as Arithmetic which contains 4 functions as Add() for addition,Sub() for substraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation.

def Add(num1,num2):
	return num1+num2

def Sub(num1,num2):
	return num1-num2

def Mult(num1,num2):
	return num1*num2

def Div(num1,num2):
	if(num2==0):
		print('Div by 0 Not possible')
		return "Error"
	return num1/num2

