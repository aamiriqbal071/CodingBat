
# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


# middleWay([1, 2, 3], [4, 5, 6]) → [2, 5]
# middleWay([7, 7, 7], [3, 8, 0]) → [7, 8]
# middleWay([5, 2, 9], [1, 4, 5]) → [2, 4]

def middleWay(a,b):
	n = int(len(a)/2)
	c=list()
	c.append(a[n])
	c.append(b[n])
	return c



print(middleWay([1, 2, 3], [4, 5, 6]))
print(middleWay([7, 7, 7], [3, 8, 0]))
print(middleWay([5, 2, 9], [1, 4, 5]))