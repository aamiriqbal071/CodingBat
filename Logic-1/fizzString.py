# Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz".
# If both the "f" and "b" conditions are true, return "FizzBuzz".
# In all other cases, return the string unchanged. (See also: FizzBuzz Code)


# fizzString("fig") → "Fizz"
# fizzString("dib") → "Buzz"
# fizzString("fib") → "FizzBuzz"


def fizzString(a):
	if a[0]=="f" and a[-1]=="b":
		return "FizzBuzz"
	elif a[0]=="f":
		return "Fizz"
	elif a[-1]=="b":
		return "Buzz"
	else:
		return a



print(fizzString("fig"))
print(fizzString("dib"))
print(fizzString("fib"))