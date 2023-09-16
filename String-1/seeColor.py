# Given a string, if the string begins with "red" or "blue" return that color string, otherwise return the empty string.


# seeColor("redxx") → "red"
# seeColor("xxred") → ""
# seeColor("blueTimes") → "blue"


def seeColor(a):
	if a[:3] == "red":
		return "red"

	elif a[:4] == "blue":
		return "blue"

	else:
		return ""

a=input("Enter a string:")
print(seeColor(a))