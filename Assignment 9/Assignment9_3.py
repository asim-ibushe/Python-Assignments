#WAP which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line arguments.
import sys
def main():
	if len(sys.argv)==2:
		file_name=sys.argv[1]
		print("Existing File name= ",file_name)
		first_file=open(file_name,"r")
		content=first_file.read()
		print("Data in file is :",content)
		second_file=open("Demo.txt","w")
		second_file.write(content)
		print(f"Copied all content from {file_name} to file Demo.txt")
	else:
		print("Invalid argument passed")
if __name__=="__main__":
	main()
