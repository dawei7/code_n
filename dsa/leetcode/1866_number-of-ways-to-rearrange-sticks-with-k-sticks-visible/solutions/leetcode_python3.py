class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        modulo = 1_000_000_007
        previous = [0] * (k + 1)
        previous[0] = 1

        for stick_count in range(1, n + 1):
            current = [0] * (k + 1)
            for visible in range(1, min(stick_count, k) + 1):
                current[visible] = (
                    previous[visible - 1]
                    + (stick_count - 1) * previous[visible]
                ) % modulo
            previous = current

        return previous[k]
