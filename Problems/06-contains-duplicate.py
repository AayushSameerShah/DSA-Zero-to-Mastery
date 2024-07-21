# Given an integer array nums, return true if 
# any value appears at least twice in the array, 
# and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def contains_duplicate(array):
    counter = {}
    for elem in array:
        if counter.get(elem, 0) > 0:
            return True
        else:
            counter[elem] = 1
    return False

print(contains_duplicate([1,2,3]))

# ------------------------------------------- #
## The better way from ChatGPT:
def contains_duplicate(array):
    seen = set()
    for elem in array:
        if elem in seen:
            return True
        seen.add(elem)
    return False

