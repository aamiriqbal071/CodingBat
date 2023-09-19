
# You have a blue lottery ticket, with ints a, b, and c on it.
# This makes three pairs, which we'll call ab, bc, and ac.
# Consider the sum of the numbers in each pair.
# If any pair sums to exactly 10, the result is 10.
# Otherwise if the ab sum is exactly 10 more than either bc or ac sums, the result is 5. Otherwise the result is 0.


# blueTicket(9, 1, 0) → 10
# blueTicket(9, 2, 0) → 0
# blueTicket(6, 1, 4) → 10


def blueTicket(a,b,c):
	ab=int(a+b)
	bc=int(b+c)
	ca=int(c+a)

	if ab == 10 or bc == 10 or ca == 10:
		return 10
	elif ab >= bc+10 or ab >= ca+10:
		return 5
	else:
		return 0

print(blueTicket(9, 1, 0))
print(blueTicket(9, 2, 0))
print(blueTicket(6, 1, 4))
