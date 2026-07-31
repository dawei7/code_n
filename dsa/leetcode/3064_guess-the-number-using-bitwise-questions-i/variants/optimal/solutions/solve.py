class CommonSetBitsAPI:
    """Local equivalent of LeetCode's hidden commonSetBits query function."""

    def __init__(self, hidden: int):
        self._hidden = hidden

    def __call__(self, num: int) -> int:
        return (self._hidden & num).bit_count()


def solve(n: int) -> int:
    commonSetBits = CommonSetBitsAPI(n)

    answer = 0
    for bit in range(30):
        mask = 1 << bit
        if commonSetBits(mask) > 0:
            answer |= mask

    return answer
