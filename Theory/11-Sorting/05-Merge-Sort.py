'''
I am glad that I have implemented this in the first try!
'''

def mergeSort(numbers):
    def divide_and_conquer(numbers):
        '''
        This method will be used recursively and does both things.
        Divide and then Merge.
        '''
        if len(numbers) == 1: # the base cae
            return numbers
        
        ####################
        ### DIVIDE PHASE ###
        ####################
        length = len(numbers) // 2
        
        # divide in half
        left = numbers[:length]
        right = numbers[length:]

        # keep dividing until both sides have single element
        left = divide_and_conquer(left)
        right = divide_and_conquer(right)
        
        ####################
        ### MERGE  PHASE ###
        ####################
        
        # Create an array to store the merged elements
        merged = [None] * (len(left) + len(right))
        
        i = 0 # for left pointer
        j = 0 # for right pointer
        idx = 0 # main pointer in the `merged`` list
        
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                merged[idx] = left[i]
                i += 1
            else:
                merged[idx] = right[j]
                j += 1
            idx += 1

        # cleaning (for leftover numbers)
        while i < len(left):
            merged[idx] = left[i]
            idx += 1
            i += 1
        
        while j < len(right):
            merged[idx] = right[j]
            idx += 1
            j += 1

        return merged
    return divide_and_conquer(numbers)
    
import numpy as np
numbers = list(np.random.randint(-100, 100, 20))
print(mergeSort(numbers))