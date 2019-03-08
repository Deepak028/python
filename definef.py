def func1():
	print("hii")
	print("hello everyone")
func1()
def func2(b):
	print("hello",b)
func2(4)
def func3(a,b,c):
	z=a+b+c
	print(a,b,c,z)
func3(3,7,6)
def func4(university="CMR"):
	print("i am in"+"\t",university)
func4("IITM")
func4("IITB")
func4("IITD")
func4()
def func5(a,b,c):
	d=a+b+c
	return (d)
def func6():
	print("calling the other func")
	e=func5(2,4,6)
	print(e)
func6()