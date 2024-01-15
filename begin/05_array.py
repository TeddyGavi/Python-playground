names = ["Bob", "Billy", "Carl", "Luna"]
print(range(len(names)))

for i in names:
    print(i)

print(*range(len(names)), sep=",")

for i in names:
    i = i + "s"
    print(i)

print(names)


def multiples(integer, limit):
    return list(range(integer, limit + 1, integer))


print(multiples(2, 6))
