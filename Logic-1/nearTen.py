
# Given a non-negative number "num", return true if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


# nearTen(12) → true
# nearTen(17) → false
# nearTen(19) → true


def nearTen(num):
	return num % 10 == 2 or num % 10 == 1 or num % 10 == 9 or num % 10 == 8


print(nearTen(12))
print(nearTen(17))
print(nearTen(19))