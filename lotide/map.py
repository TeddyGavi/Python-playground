def map(array, cb):
    result = []
    for i in array:
        result.append(cb(i))

    return result


def add_one(n):
    return n + 1


print(map([1, 2, 3], add_one))
