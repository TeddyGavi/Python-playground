def count_letters(str):
    results = {}
    for i in str:
        if i in results:
            results[i] += 1
        else:
            results[i] = 1
    return results


print(count_letters('hi'))
print(count_letters('hiiiiiihhhi'))
