#WAP contains one class Arithmetic. one instance variable as Value. Four instance methods ChkPrime(), ChkPerfect(), SumFactors(), Factors()

class Arithmetic:
	def __init__(self,Num):
		self.Value=Num
		print("Object Created!!")
	def ChkPrime(self):
		if self.Value<1:
			return "Not Prime"
		for i in range(2,self.Value):
			if (self.Value%i)==0:
				return "Not Prime Number"
		return "It is a prime NO"
	def Factors(self):
		All_fact=[]
		for i in range(1,int(self.Value/2)+1):
			if self.Value%i==0:
				All_fact.append(i)
		return All_fact
	def SumFactors(self):
		Total=0
		array=self.Factors()
		for i in range(len(array)):
			Total+=array[i]
		return Total
	def ChkPerfect(self):
		if self.SumFactors()==self.Value:
			return "Perfect Number"
		else:
			return "Not a Perfect Number"

def main():
	Num1=Arithmetic(int(input("Enter a Number: ")))
	print(Num1.ChkPrime(),Num1.ChkPerfect(),f"Sum of All factors {Num1.SumFactors()}",f"list of all factor of a Num={Num1.Factors()}",sep=",")
	Num2=Arithmetic(int(input("Enter a Number: ")))
	print(Num2.ChkPrime(),Num2.ChkPerfect(),f"Sum of All factors {Num2.SumFactors()}",f"list of all factor of a Num={Num2.Factors()}",sep=",")
if __name__=="__main__":
	main()
