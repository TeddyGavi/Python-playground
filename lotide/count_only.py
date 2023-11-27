def count_only(array, obj):
    result = {}
    for i in array:
        if i in obj and obj[i]:
            result[i] = result.get(i, 0) + 1

    return result


firstNames = [
    "Karl",
    "Salima",
    "Agouhanna",
    "Fang",
    "Kavith",
    "Jason",
    "Salima",
    "Fang",
    "Joe"
]

print(count_only(firstNames, {"Karl": True}))
print(count_only(firstNames, {"Karl": True, "Fang": True, "Salima": False}))
