#WAP contains class named as Arithmetic. Three instance variables as Value1, Value2. Three instance methods as Accept(), Addition(), Substraction(), Multiplication(), Division()
class Arithmetic:
	def __init__(self):
		self.Value1=0
		self.Value2=0
	def Accept(self):
		self.Value1=int(input("Enter First Number :"))	
		self.Value2=int(input("Enter Second Number :"))
	def Addition(self):
		return self.Value1+self.Value2
	def Substraction(self):
		return self.Value1-self.Value2
	def Multiplication(self):
		return self.Value1*self.Value2
	def Division(self):
		return self.Value1/self.Value2
def main():
	A1=Arithmetic()
	A1.Accept()
	print(f"Number1 is {A1.Value1} Number2 is {A1.Value2} there Addition= {A1.Addition()} Sustraction= {A1.Substraction()} Multiplication= {A1.Multiplication()} Division= {A1.Division()}")
	A2=Arithmetic()
	A2.Accept()
	print(f"Number1 is {A2.Value1} Number2 is {A2.Value2} there Addition= {A2.Addition()} Sustraction= {A2.Substraction()} Multiplication= {A2.Multiplication()} Division= {A2.Division()}")
if __name__ == "__main__":
	main()
