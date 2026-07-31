class CommonBitsAPI:
    """Local equivalent of LeetCode's stateful commonBits query function."""

    def __init__(self, hidden: int):
        self._hidden = hidden

    def __call__(self, num: int) -> int:
        count = 30 - (self._hidden ^ num).bit_count()
        self._hidden ^= num
        return count


def solve(n: int) -> int:
    commonBits = CommonBitsAPI(n)

    zero_count = commonBits(0)
    answer = 0

    for bit in range(30):
        next_zero_count = commonBits(1 << bit)
        if next_zero_count > zero_count:
            answer |= 1 << bit
        zero_count = next_zero_count

    return answer
