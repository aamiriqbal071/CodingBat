# Given two strings, append them together (known as "concatenation") and return the result.
# However, if the concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".

# conCat("abc", "cat") → "abcat"
# conCat("dog", "cat") → "dogcat"
# conCat("abc", "") → "abc"


def conCat(a,b):
	n=len(a)
	if a[n-1]==b[0]:
		return a+b[1:]
	else:
		return a+b


a=input("Enter a string:")
b=input("Enter a string:")
print(conCat(a,b))