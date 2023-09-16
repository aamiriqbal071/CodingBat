# Given an int array, return true if the array contains 2 twice, or 3 twice. The array will be length 0, 1, or 2.

# double23([2, 2]) → true
# double23([3, 3]) → true
# double23([2, 3]) → false

def double23(a):
	n=int(len(a))
	b=0
	for i in range(n):
		if a[i] == 2:
			b=int(b+1)
	if b >= 2:
		return True
	else:
		return False


print(double23([2, 2]))
print(double23([3, 3]))
print(double23([2, 3]))