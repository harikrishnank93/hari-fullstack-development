def sum(a,b):
	x=a+b
	return x
def sub(a,b):
	x=a-b
	return x
def mul(a,b):
	x=a*b
	return x
def div(a,b):
	if b is 0:
		return("denominator can't be 0")
	else:
		x=a/b
		return x
a=int(input("enter the first number"))
b=int(input("enter the second number"))
choice=int(input("enter your choice"))
if choice is 1:
	print sum(a,b)
elif choice is 2:
	print sub(a,b)
elif choice is 3:
	print mul(a,b)
elif choice is 4:
	print div(a,b)
else:
	print "enter valid choice"		
 
