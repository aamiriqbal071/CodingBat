
# Given two ints, each in the range 10..99, return true if there is a digit that appears in both numbers,
# such as the 2 in 12 and 23. (Note: division, e.g. n//10, gives the left digit while the % "mod" n%10 gives the right digit.)


# shareDigit(12, 23) → true
# shareDigit(12, 43) → false
# shareDigit(12, 44) → false


def shareDigit(a, b):
    
    a_ones = a % 10
    a_tens = a // 10
    b_ones = b % 10
    b_tens = b // 10
    
    
    return a_ones == b_ones or a_ones == b_tens or a_tens == b_ones or a_tens == b_tens


print(shareDigit(12, 23))  
print(shareDigit(12, 43))  
print(shareDigit(12, 44))  
