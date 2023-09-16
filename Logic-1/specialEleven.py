
# We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11.
# Return true if the given non-negative number is special.


# specialEleven(22) → true
# specialEleven(23) → true
# specialEleven(24) → false

def specialEleven(n):
	return n%11==0 or n%11==1


print(specialEleven(22))
print(specialEleven(23))
print(specialEleven(24))