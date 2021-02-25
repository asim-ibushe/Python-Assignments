#WAP which contains one list of numbers. List contains the numbers which are accepted. Filter out all prime numbers. Map function will multiply each number by 2. Reduce will return maximum num from all.
import functools
def findPrime(num):
	for i in range(2,num):
		if num%i==0:
			return False
	return True

#def Max(data):
#	Max=data[0]
#	for i in range(1,len(data)):
#		if data[i]>Max:
#			Max=data[i]
#	return Max

def main():
	arr=[]
	size=int(input("Enter List size :"))
	print("Enter data in List :")
	for i in range(size):arr.append(int(input()))
	print("List is :",arr)
	prime=list(filter(findPrime,arr))
	print("List after filter :",prime)
	Mul_two=list(map(lambda no:no*2,prime))
	print("List after map :",Mul_two)
	print("Output of reduce :",int(functools.reduce(lambda Max,current:Max if(Max>current) else current,Mul_two)))
if __name__=="__main__":
	main()
