def flatten(arr):
    if len(arr) == 0:
        return []
    if isinstance(arr[0], list):
        return flatten(*arr[:1]) + flatten(arr[1:])

    # call function with sublist as argument
    return arr[:1] + flatten(arr[1:])


print(flatten([1, 2, 3, [1, 2]]))
