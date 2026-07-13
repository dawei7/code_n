class Solution:
    def smallestGoodBase(self, n: str) -> str:
        number = int(n)
        for exponent in range(number.bit_length() - 1, 1, -1):
            low = 2
            high = 1 << ((number.bit_length() + exponent - 1) // exponent)
            while low <= high:
                base = (low + high) // 2
                total = 1
                term = 1
                for _ in range(exponent):
                    term *= base
                    total += term
                    if total > number:
                        break
                if total == number:
                    return str(base)
                if total < number:
                    low = base + 1
                else:
                    high = base - 1
        return str(number - 1)
