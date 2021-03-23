#Design py app which creates three threads as small,capital,digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.
import threading
def small(string):
	print("Thread small id: ",threading.get_ident())
	print("Creating Thread small--")
	for i in string:
		if (i>='a' and i<='z'):
			print("small-",i)
########
def capital(string):
	print("Thread capital id: ",threading.get_ident())
	print("Creating Thread capital--")
	for i in string:
		if (i>='A' and i<='Z'):
			print("capital-",i)
#######
def digits(string):
	print("Thread digits id: ",threading.get_ident())
	print("Creating Thread digits--")
	for i in string:
		if i.isnumeric():
			print("Digit-",i)	

def main():
	print("Inside main")
	string_name=input("Enter any string: ")
	t1=threading.Thread(target=small,args=(string_name,))
	t2=threading.Thread(target=capital,args=(string_name,))
	t3=threading.Thread(target=digits,args=(string_name,))
	t1.start()
	t2.start()
	t3.start()

if __name__=="__main__":
	main()
