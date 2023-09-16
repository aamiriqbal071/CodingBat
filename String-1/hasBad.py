
#Given a string, return true if "bad" appears starting at index 0 or 1 in the string,
#such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, including 0.
#Note: use .equals() to compare 2 strings.


# # hasBad("badxx") → true
# # hasBad("xbadxx") → true
# # hasBad("xxbadxx") → false

def hasBad(s):
	if s[:3] == 'bad' or s[1:4] == 'bad':
		return True
	else:
		return False


s=input("Enter a string:")
print(hasBad(s))