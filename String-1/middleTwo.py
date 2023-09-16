# Given a string of even length, return a string made of the middle two chars, so the string "string" yields "ri". 
# The string length will be at least 2.

# middleTwo("string") → "ri"
# middleTwo("code") → "od"
# middleTwo("Practice") → "ct"

def middleTwo(a):
	n=int(len(a)/2)
	return a[n-1]+a[n]



a=input("Enter a string:")
print(middleTwo(a))
