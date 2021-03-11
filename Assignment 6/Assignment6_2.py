#WAP contains one class named as Circle.Three instance variables as Radius, Area, Circumference. one class variable as PI which is initialise to 3.14. Three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display() Accept mehtod will accept value of Radius from user

class Circle:
	PI=3.14
	def __init__(self):
		self.Radius=0.0
		self.Area=0.0
		self.Circumference=0.0
	def Accept(self):
		self.Radius=float(input("Enter value of Radius :"))
	def CalculateArea(self):
		self.Area=Circle.PI*self.Radius*self.Radius
	def CalculateCircumference(self):
		self.Circumference=2*Circle.PI*self.Radius
	def Display(self):
		print(f"Circle with Radius {self.Radius} Area= {self.Area} Circumference= {self.Circumference} ")

def main():
	c1=Circle()
	c1.Accept()
	c1.CalculateArea()
	c1.CalculateCircumference()
	c1.Display()
	
	c2=Circle()
	c2.Accept()
	c2.CalculateArea()
	c2.CalculateCircumference()
	c2.Display()	
if __name__=="__main__":
	main()
