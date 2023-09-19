
# Given three ints, a b c, return true if one of them is 10 or more less than one of the others.


# lessBy10(1, 7, 11) → true
# lessBy10(1, 7, 10) → false
# lessBy10(11, 1, 7) → true


def lessBy10(a,b,c):
    diff_ab = abs(a - b)
    diff_ac = abs(a - c)
    diff_bc = abs(b - c)
    
    if diff_ab >= 10 or diff_ac >= 10 or diff_bc >= 10:
        return True
    else:
        return False

print(lessBy10(1, 7, 11))
print(lessBy10(1, 7, 10))
print(lessBy10(11, 1, 7))