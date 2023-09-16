
# Given an int array length 2, return true if it does not contain a 2 or 3.


# no23([4, 5]) → true
# no23([4, 2]) → false
# # no23([3, 5]) → false



def has23(nums):
    if 2 in nums or 3 in nums:
        return False
    else:
        return True 



print(has23([4, 5]))
print(has23([4, 2]))
print(has23([3, 5]))