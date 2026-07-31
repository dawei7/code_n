def solve(n: int) -> int:
    def common_set_bits(num: int) -> int:
        return (n & num).bit_count()

    answer = 0
    for bit in range(30):
        mask = 1 << bit
        if common_set_bits(mask) > 0:
            answer |= mask

    return answer
