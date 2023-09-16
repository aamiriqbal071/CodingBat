# Given a string, return a version without both the first and last char of the string. The string may be any length, including 0.

# withouEnd2("Hello") → "ell"
# withouEnd2("abc") → "b"
# withouEnd2("ab") → ""

def withouEnd2 (a):
	n=int(len(a))
	return a[1:n-1]

a=input("Enter a string:")
print(withouEnd2(a))