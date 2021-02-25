#WAP which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
def FindFrequency(data,num):
	count=0
	for i in range(len(data)):
		if data[i]==num:
			count+=1
	return count

def main():
	arr=[]
	size=int(input("Enter Number of elements in List :"))
	print("Enter Data :")
	for i in range(size):arr.append(int(input()))
	num=int(input("Enter Element to search :"))
	print("Output :",FindFrequency(arr,num))

if __name__=="__main__":
	main()

