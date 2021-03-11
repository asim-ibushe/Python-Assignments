#WAP contains class BankAccount. contains two instance variables as Name & Amount. one class variable as ROI=10.5. Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateInterest()

class BankAccount:
	ROI=10.5
	def __init__(self,name,amount):
		self.Name=name
		self.Amount=amount
	def Deposit(self,cash):
		self.Amount+=cash
		print("Available:",self.Amount)
	def Withdraw(self,cash):
		self.Amount-=cash
		print("Available:",self.Amount)
	def CalculateInterest(self):
		return (self.Amount*BankAccount.ROI*1)/100
	def Display(self):
		print("Name= ",self.Name)
		print("Amount= ",self.Amount)
	@classmethod
	def Display_Rate(cls):
		print(f"Rate of Interest= {cls.ROI} % ")
	@staticmethod
	def Bank_info():
		print("*** Welcome to ICICI Bank ***")


	
def main():
	BankAccount.Bank_info()
	BankAccount.Display_Rate()
	
	per1=BankAccount(input("Enter your name :"),float(input("Initial Amount :")))
	per1.Display()
	print(f"Interest on {per1.Amount} per year is",per1.CalculateInterest())
	per1.Deposit(float(input("Enter amount you need to Deposit:")))
	per1.Withdraw(float(input("Enter amount you need to Withdraw:")))

	per2=BankAccount(input("Enter your name :"),float(input("Initial Amount :")))
	per2.Display()
	print(f"Interest on {per2.Amount} per year is",per2.CalculateInterest())
	per2.Deposit(float(input("Enter amount you need to Deposit:")))
	per2.Withdraw(float(input("Enter amount you need to Withdraw:")))

if __name__=="__main__":
	main()
