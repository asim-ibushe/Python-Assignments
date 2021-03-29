#Accept file name and one string from user and return the frequency of that string from file.
def main():
	file_name=input("Enter file name (along file extension) :")
	fobj=open(file_name,"r")
	content=fobj.read()
	words=content.split(" ")
	string=input("Find a word(count) :")
	Icnt=0
	if string in words:
		for i in range(len(words)):
			if words[i]==string:
				Icnt+=1
		print("No of Occurances(word) in file :",Icnt)
	else:
		print(f"{string} Not found")
if __name__=="__main__":
	main()
