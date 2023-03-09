def f(x):
    return x * x


print(f(5))
print(type(f))


def calc_1(a, b):
    return a + b


def calc_2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


math(calc_1, 5, 45)
math(calc_2, 5, 45)


# Lambda function

calc_1 = lambda a, b: a + b
math(calc_1, 5, 45)
math(lambda a, b: a + b, 5, 45)
