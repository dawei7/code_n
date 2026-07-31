class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        value = 1

        while value <= n:
            count += 1
            value = (value << 1) | 1

        return count
