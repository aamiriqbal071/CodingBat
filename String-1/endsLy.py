# Given a string, return true if it ends in "ly".

# endsLy("oddly") → true
# endsLy("y") → false
# endsLy("oddy") → false

def endsLy(a):
	if a[-2:] == "ly":
		return True
	else:
		return False



a=input("Enter a string:")
print(endsLy(a))
