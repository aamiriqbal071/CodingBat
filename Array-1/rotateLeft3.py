
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


# rotateLeft3([1, 2, 3]) → [2, 3, 1]
# rotateLeft3([5, 11, 9]) → [11, 9, 5]
# rotateLeft3([7, 0, 0]) → [0, 0, 7]


def rotate_left3(nums):
    
    rotated = [0, 0, 0]
    rotated[0] = nums[1]
    rotated[1] = nums[2]
    rotated[2] = nums[0]
    
    return rotated




print(rotateLeft3([1, 2, 3]))
print(rotateLeft3([5, 11, 9]))
print(rotateLeft3([7, 0, 0]))

