# # Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and "java" yields "ya". 
# If either string is length 0, use '@' for its missing char.

# # lastChars("last", "chars") → "ls"
# # lastChars("yo", "java") → "ya"
# # lastChars("hi", "") → "h@"


def lastChars(a,b):
	n=int(len(b))
	if n==0:
		return a[0]+'@'
	return a[0]+b[n-1]


a=input("Enter a string:")
b=input("Enter a string:")
print(lastChars(a,b))
	