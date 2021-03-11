#WAP contains class named as BookStore with instance variables as Name, Author. class variable as NoOfBooks init to 0. Instance method as Display
class BookStore:
	NoOfBooks=0
	def __init__(self,B_name,A_name="NA"):
		self.Name=B_name
		self.Author=A_name
		BookStore.NoOfBooks=BookStore.NoOfBooks+1
	def Display(self):
		print(f"{self.Name} by {self.Author} .No of Books Available :{BookStore.NoOfBooks}")
def main():
	b1=BookStore("An Autobiography","Jawaharlal Nehru")
	b1.Display()
	b2=BookStore("Arion and the Dolphin","Vikram Seth")
	b2.Display()
	b3=BookStore("Arthashastra","Kautilya")
	b3.Display()
if __name__ == "__main__":
	main()
