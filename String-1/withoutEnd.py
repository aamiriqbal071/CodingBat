# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


# withoutEnd("Hello") → "ell"
# withoutEnd("java") → "av"
# withoutEnd("coding") → "odin"


def word(a):
	n=len(a)
	b=a[1:n-1]
	return b

a=input("Enter the word:")
print(word(a))