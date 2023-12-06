def letter_positions(string):
    result = {}
    for i in range(0, len(string)):
        if string[i] == ' ':
            continue
        elif string[i] in result:
            result[string[i]].append(i)
        else:
            result[string[i]] = [i]
    return result


print(letter_positions('hello'))
print(letter_positions(
    'hello this is a much longer test with spaces and characters :) ... '))
