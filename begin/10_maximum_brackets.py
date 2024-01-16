# Task
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained (Read the notes for more detail about it)
# Example
# With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
#
# 1 * (2 + 3) = 5
# 1 * 2 * 3 = 6
# 1 + 2 * 3 = 7
# (1 + 2) * 3 = 9
# So the maximum value that you can obtain is 9.
#
#
def result(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))


def expression_maximizer(a, b, c):
    max_result = float("-inf")

    # Try all possible combinations of operators and brackets
    for op1 in ["+", "*"]:
        for op2 in ["+", "*"]:
            expression = f"({a} {op1} {b}) {op2} {c}"
            result = eval(expression)
            max_result = max(max_result, result)

            expression = f"{a} {op1} ({b} {op2} {c})"
            result = eval(expression)
            max_result = max(max_result, result)

            expression = f"{a} {op1} {b} {op2} {c}"
            result = eval(expression)
            max_result = max(max_result, result)

            expression = f"({a} {op1} {b}) {op2} ({c})"
            result = eval(expression)
            max_result = max(max_result, result)

            expression = f"({a} {op1} {b} {op2} {c})"
            result = eval(expression)
            max_result = max(max_result, result)

    return max_result


# Example usage:
a, b, c = 1, 2, 3
result = result(a, b, c)
print(f"The maximum value is: {result}")
