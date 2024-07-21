def selection_sort(numbers):
    for i in range(len(numbers)):
        smallest = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j
        numbers[smallest], numbers[i] = numbers[i], numbers[smallest]
    return numbers

numbers = [2, 4, 6, 1, 6, 8, 0]
print(selection_sort(numbers))