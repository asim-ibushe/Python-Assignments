#Design app which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as "exit from main".
import threading
def evenfactor(num):
	Total=0
	for i in range(1,int((num+2)/2)):
		if num%i==0:
			if i%2==0:
				Total+=i
				print("Even-",i)
	print("Addition Evenfactor=",Total)
######
def oddfactor(num):
	Total=0
	for i in range(1,int((num+2)/2)):
		if num%i==0:
			if i%2!=0:
				Total+=i
				print("Odd-",i)
	print("Addition Oddfactor=",Total)	

def main():
	print("Inside main")
	Number=int(input("Enter any Number: "))
	t1=threading.Thread(target=evenfactor,args=(Number,))
	t2=threading.Thread(target=oddfactor,args=(Number,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("exit from main")

if __name__=="__main__":
	main()	
