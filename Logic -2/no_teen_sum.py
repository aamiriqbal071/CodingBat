
# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen -- in the range 13..19 inclusive --
# then that value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().


# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

# def fix_teen(n):
# 	if n==15 or n==16:
# 		return n
# 	elif 13 <= n <=19:
# 		return 0
# def no_teen_sum(a, b, c):
# 	a_new=no_teen_sum(a)
# 	b_new=no_teen_sum(b)
# 	c_new=no_teen_sum(c)
# 	if 15 <= a <= 16 and 15 <= b <= 16 and 15 <= c <= 16:
# 		return a+b+c
# 	elif 13 <= a <= 14 or 17 <= a <= 19:
# 		if 13 <= b <= 14 or 17 <= b <= 19:
# 			return c
# 	else:
# 		return b+c
# 	elif 13 <= b <= 14 or 17 <= b <= 19:
# 		if 13 <= c <= 14 or 17 <= c <= 19:
# 			return a
# 	else:
# 		return a+c

# 	elif 13 <= c <= 14 or 17 <= c <= 19:
# 		if 13 <= a <= 14 or 17 <= a <= 19:
# 			return b
# 	else:
# 		return b+a

# 	elif 13<=a<=19 and 13<=b<=19 and 13<=c<=19:
# 		return 0

# 	else:
# 	return a+b+c


def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    else:
        return n

def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    
    return a + b + c


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))