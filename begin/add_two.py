def main():
    x1 = input("What is x? ")
    y1 = input("What is y? ")
    add_two(x1, y1)


def add_two(n1: str, n2: str):
    val1 = int(n1) if n1.isdecimal() else None
    val2 = int(n2) if n2.isdecimal() else None
    if val1 and val2:
        print(val1 + val2)
    else:
        print("Enter a Valid integer!")
        main()


main()
