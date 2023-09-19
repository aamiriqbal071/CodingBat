# Given three ints, a b c, return true if two or more of them have the same rightmost digit. 
# The ints are non-negative. Note: the % "mod" operator computes the remainder, e.g. 17 % 10 is 7.


# lastDigit(23, 19, 13) → true
# lastDigit(23, 19, 12) → false
# lastDigit(23, 19, 3) → true



def lastDigit(a,b,c):
	rightmost_a = a % 10
	rightmost_b = b % 10
	rightmost_c = c % 10
	return rightmost_a == rightmost_b or rightmost_b == rightmost_c or rightmost_c == rightmost_a

print(lastDigit(23, 19, 13))
print(lastDigit(23, 19, 12))
print(lastDigit(23, 19, 3))



