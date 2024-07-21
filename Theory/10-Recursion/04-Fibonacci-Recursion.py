def fibonacciRecursive(prev, curr, count):
    if count == 0:
        return None
    count -= 1
    print(curr)
    return fibonacciRecursive(curr, prev + curr, count)


fibonacciRecursive(0, 1, 12)