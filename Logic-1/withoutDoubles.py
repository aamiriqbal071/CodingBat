# Return the sum of two 6-sided dice rolls, each in the range 1..6.
# However, if noDoubles is true, if the two dice show the same value,
# increment one die to the next value, wrapping around to 1 if its value was 6.


# withoutDoubles(2, 3, true) → 5
# withoutDoubles(3, 3, true) → 7
# withoutDoubles(3, 3, false) → 6


def withoutDoubles(a,b,noDoubles):
	if noDoubles:
		if a == 6 and b==6 :
			return 6+1
		elif a==b:
			return a+b+1
		else:
			return a+b

	else:
		return a+b


print(withoutDoubles(2, 3, True))
print(withoutDoubles(3, 3, True))
print(withoutDoubles(3, 3, False))