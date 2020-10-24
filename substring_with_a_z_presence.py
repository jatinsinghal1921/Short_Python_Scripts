'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())

for index in range(t):
    in_string = input()
    
    if len(in_string) == 1 :
    	if in_string[0] == 'a' or in_string[0] == 'z':
    		print(1)
    	else:
    		print(0)
    	continue

    left = []
    for i in range(len(in_string)):
    	if i == 0:
    		left.append(0)
    	else:
    		if 'a' in in_string[i-1] or 'z' in in_string[i-1]:
    			left.append(left[i-1] + 1)
    		else:
    			left.append(left[i-1])

    right = []
    j = 0
    for i in range(len(in_string)-1,-1,-1):
    	if i == len(in_string) -1:
    		right.append(0)
    	else:
    		if 'a' in in_string[i+1] or 'z' in in_string[i+1]:
    			right.append(right[j-1] + 1)
    		else:
    			right.append(right[j-1])
    	j = j + 1

    right.reverse()


    total_substring = 0
    for i in range(len(in_string)):
        if in_string[i] == 'a' or in_string[i] == 'z':
            total_substring = total_substring + (len(in_string) - i) + ( (i - left[i]) * (len(in_string) - i - right[i]) )
            
    print(total_substring)
