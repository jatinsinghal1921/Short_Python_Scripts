try:
	print("------ In Try Block ------")
except Exception as e:
	print("----- In Exception Block -----")
	print(e)
else:
	print("----- In Else Block -------")
finally:
	print("----- In Finally Block -----")

print("-----------------------------------------------------")

def exception_handling():
	try:
		print("------ In Try Block ------")
		1/0
	except Exception as e:
		print("----- In Exception Block -----")
		print(e)
		return -1
	except ZeroDivisionError:
		print("----- In Second Exception Block -----")
	else:
		print("----- In Else Block -------")
	finally:
		print("----- In Finally Block -----")

	
# print("-----------------------------------------------------")

# try:
# 	print("------ In Try Block ------")
# 	1/0
# except ValueError:
# 	print("----- In Exception Block -----")
# else:
# 	print("----- In Else Block -------")
# finally:
# 	print("----- In Finally Block -----")


print(exception_handling())