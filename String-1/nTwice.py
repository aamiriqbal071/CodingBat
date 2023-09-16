# Given a string and an int n, return a string made of the first and last n chars from the string.
# The string length will be at least n.


# nTwice("Hello", 2) → "Helo"
# nTwice("Chocolate", 3) → "Choate"
# nTwice("Chocolate", 1) → "Ce"

def nTwice(a,b):
	return a[:b]+a[-b:]



a=input("Enter a string:")
b=int(input("Enter an int:"))
print(nTwice(a,b))