import re

string = "/var/file1.txt"

# check if 'Python' is at the beginning
match = re.findall("^(.+)\/([^/]+)$", string)
print(match)


# if match:
#   print(match)
#   print("pattern found inside the string")
# else:
#   print("pattern not found")  

# Output: pattern found inside the string
