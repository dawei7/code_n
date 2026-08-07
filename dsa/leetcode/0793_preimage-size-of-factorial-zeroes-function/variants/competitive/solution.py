class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(value: int) -> int:
            total = 0
            while value:
                value //= 5
                total += value
            return total

        low = 0
        high = 5 * k + 5
        while low < high:
            middle = (low + high) // 2
            if trailing_zeroes(middle) < k:
                low = middle + 1
            else:
                high = middle
        return 5 if trailing_zeroes(low) == k else 0
