# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# https://leetcode.com/problems/move-zeroes/description/

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


def move_zeros(array):
    i = 0
    j = i+1
    while(i<len(array) and j<len(array)):
        if array[i] == 0 and array[j] != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
        elif array[i] == 0 and array[j] == 0:
            j += 1
    return array

print(move_zeros([0,1,0,0,0,3,12, 6, 0, 0]))

# This code is cool and works but ChatGPT has better version in which...
# let's just print that.

# --------------------------------------------------------------- #

def move_zeros_gpt(nums):
    # Initialize a pointer for the position to place the next non-zero element.
    non_zero_index = 0
    
    # Iterate through the array.
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element with the element at the non_zero_index.
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            # Move the pointer to the next position.
            non_zero_index += 1

    return nums

print(move_zeros_gpt([0, 1, 0, 0, 0, 3, 12, 6, 0, 0]))

 