log_file_obj = open("logs.txt","r")

lines = log_file_obj.readlines()
print(len(lines))
for index,line in enumerate(lines):
	print(index)
	break

print(index)


