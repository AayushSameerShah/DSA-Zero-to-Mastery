'''
Move one by one, and keep inserting the next element
in the previous list.

There will be a lot of "shifting", so better with the
linkedlists.
'''

def insertionSort_Array(numbers):
    def bubble_down(i):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break 
    
    for i in range(1, len(numbers)):
        bubble_down(i)

    return numbers


numbers = [2, 4, 6, 1, 6, 8, 0, 11, 99, -99]
print(insertionSort_Array(numbers))