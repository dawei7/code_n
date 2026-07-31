class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        segments = list(zip(nums1, nums0))

        def order(segment: tuple[int, int]) -> tuple[int, int, int]:
            ones, zeros = segment
            if zeros == 0:
                return (0, 0, 0)
            if ones == 0:
                return (2, 0, 0)
            return (1, -ones, zeros)

        segments.sort(key=order)

        value = 0
        modulo = 1_000_000_007
        for ones, zeros in segments:
            for _ in range(ones):
                value = (value * 2 + 1) % modulo
            for _ in range(zeros):
                value = value * 2 % modulo
        return value
