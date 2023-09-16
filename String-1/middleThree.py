# Given a string of odd length, return the string length 3 from its middle, so "Candy" yields "and". 
# The string length will be at least 3.

# middleThree("Candy") → "and"
# middleThree("and") → "and"
# middleThree("solving") → "lvi"


def middleThree (s):
	n=int(len(s)/2)
	return s[n-1]+s[n]+s[n+1]


s=input("Enter a string:")
print(middleThree(s))