#Design py app which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
import threading

def Even_thread():
	print("Even thread")
	arr=[]
	num=1
	while len(arr)<10:
		if num%2==0:
			arr.append(num)
			print("Even",num)
		num+=1

def Odd_thread():
	print("Odd thread")
	arr=[]
	num=1
	while len(arr)<10:
		if num%2!=0:
			arr.append(num)
			print("Odd",num)
		num+=1

	
def main():
	print("Inside main")
	#print(Even_thread())
	#print(Odd_thread())
	t1=threading.Thread(target=Even_thread())
	t2=threading.Thread(target=Odd_thread())
	t1.start()
	t2.start()

if __name__=="__main__":
	main()
