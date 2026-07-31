class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        mismatch_positions = [
            index
            for index, (first, second) in enumerate(zip(s1, s2))
            if first != second
        ]
        mismatch_count = len(mismatch_positions)

        if mismatch_count % 2:
            return -1
        if mismatch_count == 0:
            return 0

        previous_two = 0
        previous_one = x

        for index in range(1, mismatch_count):
            current = min(
                previous_one + x,
                previous_two
                + 2
                * (
                    mismatch_positions[index]
                    - mismatch_positions[index - 1]
                ),
            )
            previous_two, previous_one = previous_one, current

        return previous_one // 2
