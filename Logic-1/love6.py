
# The number 6 is a truly great number. Given two int values, a and b, return true if either one is 6.
# Or if their sum or difference is 6. Note: the function Math.abs(num) computes the absolute value of a number.


# love6(6, 4) → true
# love6(4, 5) → false
# love6(1, 5) → true

def love6(a,b):
	return a==6 or b==6 or a+b == 6 or abs(a-b)==6



print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))