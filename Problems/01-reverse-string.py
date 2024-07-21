# Just reverse the string in "non-pyhonic" way
reversed_string = []
def reverse_string(str_):
    for i in range(len(str_)-1, -1, -1):
        reversed_string.append(str_[i])
    return "".join(reversed_string)

print(reverse_string("Aayush Shah"))