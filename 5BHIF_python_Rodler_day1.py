from math import floor


def calculate(mass):
    return floor(mass/3) - 2


if __name__ == '__main__':

    with open('data.txt') as f:
        mass = [int(x) for x in f.readlines()]

    print(sum(map(calculate, mass)))

    # Part 2:
    c = 0
    for m in mass:
        while m > 0:
            m = max(0, calculate(m))
            c += m
    print(c)