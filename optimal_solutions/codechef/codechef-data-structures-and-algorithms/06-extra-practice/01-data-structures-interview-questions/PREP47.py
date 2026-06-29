import sys

def divide(a, b):
    negative = (a < 0) ^ (b < 0)
    dividend = abs(a)
    divisor = abs(b)
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while dividend >= temp << 1:
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    if negative:
        quotient = -quotient
    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)
    if quotient > INT_MAX:
        return INT_MAX
    if quotient < INT_MIN:
        return INT_MIN
    return quotient

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    results = []
    index = 1
    for _ in range(t):
        a = int(input_data[index])
        b = int(input_data[index + 1])
        index += 2
        results.append(str(divide(a, b)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
