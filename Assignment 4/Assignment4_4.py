#WAP which contains one list of numbers. List contains the numbers which are accepted.Filterout all no which are even. Map function will calculate its square. Reduce will return addition of all that number.
import functools
def main():
	arr=[]
	size=int(input("Enter List size :"))
	print("Enter data in List :")
	for i in range(size):arr.append(int(input()))
	print("List is :",arr)
	even_n=list(filter(lambda no:no%2==0,arr))
	print("List after filter :",even_n)
	square_n=list(map(lambda no:no*no,even_n))
	print("List after map :",square_n)
	output=int(functools.reduce(lambda no1,no2:no1+no2,square_n))
	print("Output of reduce :",output)
if __name__=="__main__":
	main()
