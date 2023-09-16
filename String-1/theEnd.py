# Given a string, return a string length 1 from its front, unless front is false,
# in which case return a string length 1 from its back. The string will be non-empty.

# theEnd("Hello", true) → "H"
# theEnd("Hello", false) → "o"
# theEnd("oh", true) → "o"


def theEnd (a,b):
	if a[1] == b:
		return True
	else:
		return False


a=input("Enter a string:")
b=input("Enter a char:")
print(theEnd(a,b))