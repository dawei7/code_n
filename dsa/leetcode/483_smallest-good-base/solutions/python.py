"""Integer geometric-sum binary search for LeetCode 483."""


def solve(n: str) -> str:
    number = int(n)
    for exponent in range(number.bit_length() - 1, 1, -1):
        low = 2
        high = 1 << ((number.bit_length() + exponent - 1) // exponent)
        while low <= high:
            base = (low + high) // 2
            total = (pow(base, exponent + 1) - 1) // (base - 1)
            if total == number:
                return str(base)
            if total < number:
                low = base + 1
            else:
                high = base - 1
    return str(number - 1)
