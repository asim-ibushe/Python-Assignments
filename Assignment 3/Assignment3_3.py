#WAP which accept N numbers from user and store it into List. Return Minumum number from that List.
def findMin(data):
	Min=data[0]
	for i in range(1,len(data)):
		if data[i]<Min:
			Min=data[i]
	return Min

def main():
	arr=[]
	size=int(input("Enter Number of elements :"))
	print("Enter Data :")
	for i in range(size):arr.append(int(input()))
	print("Output :",findMin(arr))

if __name__=="__main__":
	main()

		
