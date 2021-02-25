#WAP which accept N numbers from user and store it into List. Return addition of all elements from that List.
i=0
Total=0
def AdditionR(data):
	global i
	global Total
	if i<len(data):
		Total+=data[i]
		i+=1
		AdditionR(data)
	return Total
def main():
	arr=[]
	size=int(input("Enter Number of elements :"))
	for i in range(size):arr.append(int(input()))
	print("Data is :",arr)
	print("Addition of all elements of an array using Recursion :",AdditionR(arr))
if __name__ =="__main__":
	main()
