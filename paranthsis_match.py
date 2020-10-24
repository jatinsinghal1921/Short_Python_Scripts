input_string = input("Enter input string : ")

open_brac = 0
close_brac = 0
delete_count = 0

for character in input_string:
	if character == "(":
		open_brac += 1
	else:
		close_brac += 1

	if close_brac > open_brac:
		close_brac -= 1
		delete_count += 1

if open_brac > close_brac:
	delete_count += (open_brac - close_brac)


print(delete_count)
