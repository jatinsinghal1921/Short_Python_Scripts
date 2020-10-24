def readn(fileContents,n,count):
	if (n*count) >= len(fileContents):
		pass
	else:
		start = (n*count)
		file = fileContents[start:]
		
		if len(file) < n:
			n = len(file)
		
		string = ""
		for i in range(n):
			string += file[i]	

		print(string)	
	return (count + 1)


def main():
	f = open("testFile.txt","r")
	fileContents = f.read()	
	n = int(input("Input the n value"))
	global count

	count = readn(fileContents,n,count)
	print("************")
	count = readn(fileContents,n,count)
	print("************")
	count = readn(fileContents,n,count)
	print("************")
	count = readn(fileContents,n,count)
	print("************")
	count = readn(fileContents,n,count)


count = 0
main()	