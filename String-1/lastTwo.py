# Given a string of any length,return a new string where the last 2 chars, if present, are swapped, so "coding" yields "codign".

# lastTwo("coding") → "codign"
# lastTwo("cat") → "cta"
# lastTwo("ab") → "ba"

def lastTwo(a):
	if len(a) <= 2:
		return a[-2:]
	else:
		return a[:-2]+a[-1]+a[-2]

a=input("Enter a string:")
print(lastTwo(a))
