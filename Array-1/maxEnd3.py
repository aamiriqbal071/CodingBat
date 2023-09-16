# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


# maxEnd3([1, 2, 3]) → [3, 3, 3]
# maxEnd3([11, 5, 9]) → [11, 11, 11]
# maxEnd3([2, 11, 3]) → [3, 3, 3]

def maxEnd3(a):
    if a[0] > a[-1]:
        n = a[0]
    else:
        n = a[-1]

    for i in range(len(a)):  
        a[i] = n
    
    return a

print(maxEnd3([1, 2, 3]))   # Output: [3, 3, 3]
print(maxEnd3([11, 5, 9]))  # Output: [11, 11, 11]
print(maxEnd3([2, 11, 3]))  # Output: [3, 3, 3]
