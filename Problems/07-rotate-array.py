# Given an integer array nums, rotate the array to the
# right by k steps, where k is non-negative.
 
## Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

## Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

## Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

## Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

#### THOUGHTS ####
# 1. We can use the additional array of the same size and filled from i:... for the left 
# side and then the right side can be filled :i. But that is easiest and would require extra mem.

# 2. We can make some logic for inplace replacement but there, we will need to shift 1 by 1
# it will be O(n^2) solution or O(2^n) solution, I don't know. It will have so many shifts.

# 3. If we really need to do stuff in place, we need to do that in one go.
import math
def rotate_array(array, k):
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(array)
    k = k % n  # Ensure k is within the bounds of array length

    # Step 1: Reverse the entire array
    reverse(array, 0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(array, 0, k - 1)

    # Step 3: Reverse the remaining elements
    reverse(array, k, n - 1)
    
    return array

print(rotate_array([1,2,3,4,5], k=2))