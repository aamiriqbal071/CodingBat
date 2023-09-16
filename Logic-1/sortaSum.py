
# Given 2 ints, a and b, return their sum.
# However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


# sortaSum(3, 4) → 7
# sortaSum(9, 4) → 20
# sortaSum(10, 11) → 21


def sortaSum(a,b):
	sum=int(a+b)
	if sum in range(10, 20):
		return 20 
	else:
		return sum



print(sortaSum(3, 4))
print(sortaSum(9, 4))
print(sortaSum(10, 11))