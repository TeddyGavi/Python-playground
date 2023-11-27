import random
random_arr = random.sample(range(100), 100)
print(random_arr)


def bubblin(arr):
    for j in range(0, len(arr) - 1):
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubblin(random_arr))
