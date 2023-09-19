
# Given three ints, a b c, return true if it is possible to add two of the ints to get the third.


# twoAsOne(1, 2, 3) → true
# twoAsOne(3, 1, 2) → true
# twoAsOne(3, 2, 2) → false


def twoAsOne(a,b,c):
	return a+b == c or a+c == b or c+b ==a

print(twoAsOne(1, 2, 3))
print(twoAsOne(3, 1, 2))
print(twoAsOne(3, 2, 2))