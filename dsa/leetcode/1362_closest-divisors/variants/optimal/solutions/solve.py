from math import isqrt


def solve(num):
    def closest_pair(value):
        divisor = isqrt(value)
        while value % divisor:
            divisor -= 1
        return [divisor, value // divisor]

    first = closest_pair(num + 1)
    second = closest_pair(num + 2)
    if second[1] - second[0] < first[1] - first[0]:
        return second
    return first
