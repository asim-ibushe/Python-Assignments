#WAP which accept N numbers from user and store it into List. Return Maximum number from that List.
def findMax(data):
	Max=data[0]
	for i in range(1,len(data)):
		if data[i]>Max:
			Max=data[i]
	return Max	

def main():
	arr=[]
	size=int(input("Enter Number of elements :"))
	print("Enter Data :")
	for i in range(size):arr.append(int(input()))
	print("Output :",findMax(arr))

if __name__=="__main__":
	main()

		
