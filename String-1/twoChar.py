# Given a string and an index, return a string length 2 starting at the given index. 
# If the index is too big or too small to define a string length 2, use the first 2 chars. 
# The string length will be at least 2.


# twoChar("java", 0) → "ja"
# twoChar("java", 2) → "va"
# twoChar("java", 3) → "ja"

def twoChar (a,i):
	if i<0 or i+2 > len(a):
		return a[:2]
	else:
		return a[i:i+2]

a=input("Enter a string:")
i=int(input("Enter the index:"))
print(twoChar(a,i))