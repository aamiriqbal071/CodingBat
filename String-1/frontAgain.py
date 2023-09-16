# Given a string, return true if the first 2 chars in the string also appear at the end of the string, such as with "edited".


# frontAgain("edited") → true
# frontAgain("edit") → false
# frontAgain("ed") → true

def frontAgain(a):
	if a[:2] == a[-2:]:
		return True
	else:
		return False

a=input("Enter a string:")
print(frontAgain(a))