class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        def has_no_zero(value: int) -> bool:
            return "0" not in str(value)

        for first in range(1, n):
            second = n - first
            if has_no_zero(first) and has_no_zero(second):
                return [first, second]

        raise ValueError("the problem guarantees a valid decomposition")
