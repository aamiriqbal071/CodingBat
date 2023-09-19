
# You have a green lottery ticket, with ints a, b, and c on it.
# If the numbers are all different from each other, the result is 0.
# If all of the numbers are the same, the result is 20. If two of the numbers are the same, the result is 10.


# greenTicket(1, 2, 3) → 0
# greenTicket(2, 2, 2) → 20
# greenTicket(1, 1, 2) → 10


def greenTicket(a,b,c):
	if a==b==c:
		return 20
	elif a != b != c:
		return 0
	elif a == b or c == a or b == c:
		return 10
	else:
		return 0


print(greenTicket(1, 2, 3))
print(greenTicket(2, 2, 2))
print(greenTicket(1, 1, 2))
