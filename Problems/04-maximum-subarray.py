# Given an integer array nums, find the 

# subarray
#  with the largest sum, and return its sum.

## Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

## Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

## Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer approach, which is more subtle.


## Note that this solution is given by ChatGPT after my long code.
## This is better version and my code was a bit long. 
## Here, I have written the comments for better understanding.

def find_subarray(array):
    if len(array) == 1:
        return array[0], 0, 1, array

    # assume that the first is always the largest
    best_largest_sum = array[0]
    
    # assign the first as current
    curr_largest_sum = array[0]
    best_start = best_stop = start = 0

    for i in range(1, len(array)):
        # we will just keep track of single variable
        
        # if you've made it less than 0
        # then reset it with new item
        if curr_largest_sum < 0:
            curr_largest_sum = array[i]
            start = i # a fresh start
        else:
            # if not zero, then keep going
            curr_largest_sum += array[i]

        # well, if the current is better than the best
        # update; otherwise keep going with current
        if curr_largest_sum > best_largest_sum:
            best_largest_sum = curr_largest_sum
            best_start = start
            best_stop = i + 1

    return best_largest_sum, best_start, best_stop, array[best_start:best_stop]


print(find_subarray([5,4,-1,7,8]))