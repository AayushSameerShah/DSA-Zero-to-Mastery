# Given both arrays, merge the arrays and sort the 
# final array.

# Assume that both arrays will be sorted themselves.

def merge_and_sort(array1, array2):
    i = 0
    j = 0

    merged_array = []
    while (i<len(array1) and j<len(array2)):
        left = array1[i]
        right = array2[j]
        if  left < right:
            merged_array.append(left)
            i += 1
        else:
            merged_array.append(right)
            j += 1
    
    # add any remaining elements (only one of bottom will run)
    merged_array.extend(array1[i:])
    merged_array.extend(array2[j:])

    return merged_array
print(merge_and_sort([0, 2, 4], [1, 3, 5, 55, 77, 88]))