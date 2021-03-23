#Design py app which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.
import threading
def evenlist(arr):
	print("Thread even--")
	Total=0
	#print(arr)
	#print(len(arr))
	for i in range(len(arr)):
		if arr[i]%2==0:
			Total+=arr[i]
			print('Even-',arr[i])
	print("Addition of EvenNo :",Total)
##############################
def oddlist(arr):
	print("Thread Od--")
	Total=0
	#print(arr)
	#print(len(arr))
	for i in range(len(arr)):
		if arr[i]%2!=0:
			Total+=arr[i]
			print('Odd-',arr[i])
	print("Addition of OddNo :",Total)

def main():
	print("Inside main")
	array=[]
	size=int(input("Enter No of Elements:"))
	for i in range(1,size+1):
		array.append(int(input("Enter No :"))) 
	t1=threading.Thread(target=evenlist,args=(array,))
	t2=threading.Thread(target=oddlist,args=(array,))
	t1.start()
	t2.start()
if __name__=="__main__":
	main()
