#WAP which accept file name from user and open that file and display the contents of that file on screen.
from os import path
def main():
	file_name=input("Enter File name(along file extension) :")
	try:
		fobj=open(file_name,"r")
		print(fobj.read())
	except Exception as obj:
		print("Sorry, file does not exist",obj)
	

if __name__=="__main__":
	main()
