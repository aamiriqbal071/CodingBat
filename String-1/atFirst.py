# # Given a string, return a string length 2 made of its first 2 chars.
#  If the string length is less than 2, use '@' for the missing chars.

# # atFirst("hello") → "he"
# # atFirst("hi") → "hi"
# # atFirst("h") → "h@"


def atFirst(a):
	if len(a) >= 2:
		return a[:2]
	else:
		return a+'@'


a=input("Enter a string:")
print(atFirst(a))


