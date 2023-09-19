
# Given three ints, a b c, return true if b is greater than a, and c is greater than b.
# However, with the exception that if "bOk" is true, b does not need to be greater than a.


# inOrder(1, 2, 4, false) → true
# inOrder(1, 2, 1, false) → false
# inOrder(1, 1, 2, true) → true

def inOrder(a,b,c,bOk):
	if c>b and b>a:
		return True 
	elif bOk:
		if c > b:
			return True
	else:
		return False



print(inOrder(1, 2, 4, False))
print(inOrder(1, 2, 1, False))
print(inOrder(1, 1, 2, True))