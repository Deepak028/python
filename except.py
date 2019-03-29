try:
	a=int(input("enter number"))
	if a<=3:
		b=int((a/a-3))
	elif a==3:
		raise ZeroDivisionError
	else:
		raise NameError
except ZeroDivisionError:
	print("some error occured")
except NameError:
	print("you have choosen a number greater than 3")
else:
	print(b)