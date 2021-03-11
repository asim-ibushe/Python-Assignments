#WAP class Demo with variables as no1, no2 and class variable as value.define two methods of class as Fun and Gun which displays values of instance variables.

class Demo:
	Value=100
	def __init__(self,num1,num2):
		self.no1=num1
		self.no2=num2
	def Fun(self):
		print("Number 1=",self.no1)
		
	def Gun(self):
		print("Number 2=",self.no2)

def main():
	Obj1=Demo(11,21)
	Obj2=Demo(51,101)
	Obj1.Fun()
	Obj2.Fun()
	Obj1.Gun()
	Obj2.Gun()

if __name__=="__main__":
	main()

