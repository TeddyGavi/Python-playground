def eq_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        for idx, i in enumerate(arr1):
            if isinstance(i, list) and isinstance(arr2[idx], list):
                return eq_arrays(i, arr2[idx])
            elif i != arr2[idx]:
                return False
    return True


print(eq_arrays([1, 2, 3], [1, 2, 3]))
print(eq_arrays([1, [1, 2], 3], [1, 2, 3]))
print(eq_arrays([1, [1, 2], 3], [1, [1, 2], 3]))
print(eq_arrays([1, [1, [1, 2], 2], 3], [1, [1, [1, 2], 2], 3]))
print(eq_arrays([1, [1, [1], 2], 3], [1, [1, [1, 2], 2], 3]))
