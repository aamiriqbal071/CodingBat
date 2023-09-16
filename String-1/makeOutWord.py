
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# Note: use str.substring(i, j) to extract the String starting at index i and going up to but not including index j.


# makeOutWord("<<>>", "Yay") → "<<Yay>>"
# makeOutWord("<<>>", "WooHoo") → "<<WooHoo>>"
# makeOutWord("[[]]", "word") → "[[word]]"

def word(a,b):
	first_part=a[:2]
	second_part=a[2:]
	return first_part+b+second_part

a=input("Enter the tags:")
b=input("Enter the word:")
print(word(a,b))