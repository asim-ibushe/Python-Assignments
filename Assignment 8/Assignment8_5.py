#Design py app which contains two threads named as thread1 and thread2.Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.

import threading

def thread1(Kulup):
	Lock=Kulup
	Lock.acquire()
	print("## Inside thread 1 ##")
	for i in range(1,51):
		print("Thread1 :",i)
	Lock.release()
########################################
def thread2(Kulup):
	Lock=Kulup
	Lock.acquire()
	print("## Inside thread 2 ##")
	for i in range(50,0,-1):
		print("Thread2 :",i)
	Lock.release()

def main():
	Kulup=threading.Lock()
	print("Inside main")
	t1=threading.Thread(target=thread1,args=(Kulup,))
	t2=threading.Thread(target=thread2,args=(Kulup,))
	t1.start()

	t2.start()
	
	
if __name__=="__main__":
	main()
