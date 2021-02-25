#WAP Accepting n no from user ,filter out all prime numbers from user_defined set and perform addition of all prime no print it.
from MarvellousNum import *
def ListPrime(data):
	arr_ret=[]
	for i in range(len(data)):
		if ChkPrime(data[i])==True:
			arr_ret.append(data[i])
	return arr_ret
	
def main():
	arr=[]
	Addition=0
	size=int(input("Enter size of List :"))
	print("Enter Data in List :")
	for i in range(size):arr.append(int(input()))
	print("Data is :",arr)
	prime=ListPrime(arr)
	print("Filtered Prime NO:",prime)
	for i in range(len(prime)):
		Addition+=prime[i]
	print("Output :",Addition)
	
	
if __name__=="__main__":
	main()		
