'''
This is giving some nostalgia.
I have never implemented the quicksort myself while I was in the college.
This time, I will do implement it myself. 

I "memorized" the code. That sucks, right? You should never memorize the 
code, but I did. So, let's undo that.
'''


def quickSort(numbers):
    def divide_and_conquer(numbers):
        if len(numbers) <= 1:
            return numbers
        
        pivot = len(numbers) - 1
        i = 0

        while (i < pivot):
            if numbers[i] > numbers[pivot]:
                numbers[i], numbers[pivot-1] = numbers[pivot-1], numbers[i]
                numbers[pivot-1], numbers[pivot] = numbers[pivot], numbers[pivot-1]
                pivot -= 1
            else:
                i += 1
        
        left = numbers[:pivot]
        right = numbers[pivot:]
        
        left = divide_and_conquer(left)
        right = divide_and_conquer(right)

        return left+right
    return divide_and_conquer(numbers)

import numpy as np
numbers = list(np.random.randint(-1000, 1000, 400))
print(quickSort(numbers))

    
