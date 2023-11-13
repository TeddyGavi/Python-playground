def main():
    n = int(input("Whats x? "))
    print("x is even") if is_even(n) else print("x is odd")


def is_even(n):
    return n % 2 == 0


main()
