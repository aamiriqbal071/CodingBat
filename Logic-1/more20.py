# Return true if the given non-negative number is 1 or 2 more than a multiple of 20. See also: Introduction to Mod


# more20(20) → false
# more20(21) → true
# more20(22) → true

def more20(n):
	return n%20==1 or n%20==2


print(more20(20))
print(more20(21))
print(more20(22))