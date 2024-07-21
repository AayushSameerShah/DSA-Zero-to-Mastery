def bubble_sort(numbers):
    for grand in range(len(numbers)):
        for i in range(len(numbers) - 1 - grand):
            if numbers[i] > numbers[i+1]:
               numbers[i], numbers[i+1] = numbers[i+1],  numbers[i]
        
    return numbers


numbers = [2, 4, 6, 1, 6, 8, 33]
print(bubble_sort(numbers))