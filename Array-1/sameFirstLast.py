
# Given an array of ints, return true if the array is length 1 or more, and the first element and the last element are equal.


# sameFirstLast([1, 2, 3]) → false
# sameFirstLast([1, 2, 3, 1]) → true
# sameFirstLast([1, 2, 1]) → true



def sameFirstLast(a):
	if a[0] == a[-1] and len(a)>1:
		return True
	else:
		return False

print(sameFirstLast([1, 2, 3]))
print(sameFirstLast([1, 2, 3, 1]))
print(sameFirstLast([1, 2, 1]))