
# Given an int array, return a new array with double the length where its last element is the same as the original array, and all the other elements are 0.
# The original array will be length 1 or more. Note: by default, a new int array contains all 0's.


# makeLast([4, 5, 6]) → [0, 0, 0, 0, 0, 6]
# makeLast([1, 2]) → [0, 0, 0, 2]
# makeLast([3]) → [0, 3]


def makeLast(a):

	if len(a) < 1:
		raise ValueError("Input array must have a length of 1 or more")
	n=int(len(a)*2)
	new_a=[]
	for i in range(n):
		new_a.append(0)
	new_a[-1]=a[-1]
	return new_a					






print(makeLast([4, 5, 6]))
print(makeLast([1, 2]))
print(makeLast([3]))
