#WAP which accepts file name from user and check whether that file exists in current directory or not.
from os import path
def main():
	file_name=input("Enter file name(along .extension) You need to check :Is it Present or Not =")
	if path.exists(file_name)==True:
		print("Yepp, file is Present")
	else:
		print("Sorry, file does not exist")
if __name__=="__main__":
	main()
