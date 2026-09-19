def add(*args):
    total = 0

    for num in args:
        total += num

    return total


print(add(1, 2, 3,6,8))
