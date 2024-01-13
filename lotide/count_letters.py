def count_letters(str):
    results = {}
    for i in str:
        if i in results:
            results[i] += 1
        else:
            results[i] = 1
    return results
