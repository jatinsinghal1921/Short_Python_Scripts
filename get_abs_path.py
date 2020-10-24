def process_absPath(input_path):

	if input_path[0] == "/":
		input_path = input_path[1:]
	if input_path[-1] == "/":
		input_path = input_path[:-1]

	input_path = input_path.split("/")
	output_list = []
	for x in input_path:
		if x == "." or x == "":
			continue
		elif x == "..":
			if len(output_list) != 0:
				output_list.pop()
		else: 
			output_list.append(x)

	output_str = "/"
	for x in output_list:
		output_str += x + "/"

	return output_str


if __name__ == "__main__":
	input_path = input("Enter a path : ")
	output_path = process_absPath(input_path)
	print(output_path)



