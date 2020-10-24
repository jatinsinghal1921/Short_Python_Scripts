def product_of_3Numbers(l):

	l.sort()
	count = 0

	for i in range(1,4):
		i = -i
		if l[i] > 0:
			count += 1

	if count == 0:
		return l[-1]*l[-2]*l[-3]
	elif count == 1 or count == 2:
		return l[0]*l[1]*l[-1]
	else:
		pro1 = l[-1]*l[-2]*l[-3]
		pro2 = l[0]*l[1]*l[-1]

		if pro1 >= pro2:
			return pro1
		else:
			return pro2	

def main():
	l = [-10,-10,5,0,-20,10]
	result = product_of_3Numbers(l)
	print(result)


main()

