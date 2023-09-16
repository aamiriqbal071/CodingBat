
# Return true if the given non-negative number is a multiple of 3 or 5, but not both.


# old35(3) → true
# old35(10) → true
# old35(15) → false

def old35(n):

	if n%5==0 and n%3==0:
		return False


	elif n%5==0 or n%3==0:
		return True

print(old35(3))
print(old35(10))
print(old35(15))
