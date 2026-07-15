"""Optimal app-local solution for LeetCode 970."""


def solve(x, y, bound):
    def powers(base):
        values = [1]
        if base == 1:
            return values
        while values[-1] * base <= bound:
            values.append(values[-1] * base)
        return values

    answers = set()
    for x_power in powers(x):
        for y_power in powers(y):
            value = x_power + y_power
            if value <= bound:
                answers.add(value)
    return list(answers)
