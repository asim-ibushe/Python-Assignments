#WAP which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure. Accept names of both the files from command line.
import sys
def main():
	if len(sys.argv)==3:
		file1=sys.argv[1]
		file2=sys.argv[2]
		first_f=open(file1,"r")
		second_f=open(file2,"r")
		if first_f.read()==second_f.read():
			print("Success")
		else:
			print("Failure")
	else:
		print("Invalid Arguments passed")

if __name__=="__main__":
	main()
