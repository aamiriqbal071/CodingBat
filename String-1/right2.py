# Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. The string length will be at least 2.

# right2("Hello") → "loHel"
# right2("java") → "vaja"
# right2("Hi") → "Hi"

def right2(a):
	b=a[-2:]
	return(b+a[:-2])





a=input("Enter a string:")
print(right2(a))
