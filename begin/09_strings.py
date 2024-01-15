def reverse(st):
    st = st[::-1]
    return st


def reverse_words(sentence):
    arr = sentence.split()
    arr.reverse()
    return " ".join(arr)


print(reverse("hello"))
print(reverse_words("hello, there"))
