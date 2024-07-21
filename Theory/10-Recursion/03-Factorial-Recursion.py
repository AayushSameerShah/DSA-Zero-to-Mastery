def factorialRecursion(number):
    if number in [0, 1]:
        return number
    return number * factorialRecursion(number=number-1)

print(factorialRecursion(10))

