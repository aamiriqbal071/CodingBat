
# Given a number n, return true if n is in the range 1..10, inclusive.
# Unless outsideMode is true, in which case return true if the number is less or equal to 1, or greater or equal to 10.


# in1To10(5, false) → true
# in1To10(11, false) → false
# in1To10(11, true) → true

def in1To10(n,is_outsideMode):
	if is_outsideMode:
		return 0 <= n <= 11
	else:
		return 1 < n < 10


print(in1To10(5, False))
print(in1To10(11, False))
print(in1To10(11, True))