a=raw_input("enter the string \n")
print a
b=0
c=0
d=0
e=0
for i in a:
	if i in "aeiouAEIOU":
		b=b+1
	elif i not in " ?aeiouAEIOU":
		c=c+1
	elif i in " ":
		d=d+1
	elif i in "?":
		e=e+1
print "number of vowels are",b
print "number of constants are",c
print "number of words are",d+1
print "number of question mark",e

	
