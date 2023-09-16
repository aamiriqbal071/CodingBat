# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

# nonStart("Hello", "There") → "ellohere"
# nonStart("java", "code") → "avaode"
# nonStart("shotl", "java") → "hotlava"


a=input("Enter a string:")
b=input("Enter a string:")

print(a[1:]+b[1:])