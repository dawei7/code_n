def solve(n: int) -> int:
    state = n

    def common_bits(num: int) -> int:
        nonlocal state
        count = 30 - (state ^ num).bit_count()
        state ^= num
        return count

    zero_count = common_bits(0)
    answer = 0

    for bit in range(30):
        next_zero_count = common_bits(1 << bit)
        if next_zero_count > zero_count:
            answer |= 1 << bit
        zero_count = next_zero_count

    return answer
