def solve(rows: int = 1000000000) -> int:
    """Find number of entries not divisible by 7 in the first rows of Pascal's triangle.
    
    Time Complexity: O(log_7(rows))
    Space Complexity: O(1)
    """
    def count_not_div_7(n: int) -> int:
        if n == 0:
            return 0

        # Find largest power of 7 <= n
        p7 = 1
        while p7 * 7 <= n:
            p7 *= 7

        d = n // p7
        rem = n % p7

        full_blocks = (d * (d + 1) // 2) * (28 ** (len(oct(p7)) - 3))  # 28^(power)
        # Power of 7 is log7(p7)
        power = 0
        temp = p7
        while temp > 1:
            temp //= 7
            power += 1

        full_blocks = (d * (d + 1) // 2) * (28 ** power)
        partial_block = (d + 1) * count_not_div_7(rem)

        return full_blocks + partial_block

    return count_not_div_7(rows)
