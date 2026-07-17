class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(peak: int, length: int) -> int:
            descending = peak - 1
            if descending >= length:
                lowest = peak - length
                return (descending + lowest) * length // 2
            return descending * (descending + 1) // 2 + length - descending

        def required_sum(peak: int) -> int:
            return (
                peak
                + side_sum(peak, index)
                + side_sum(peak, n - index - 1)
            )

        low, high = 1, maxSum
        while low < high:
            middle = (low + high + 1) // 2
            if required_sum(middle) <= maxSum:
                low = middle
            else:
                high = middle - 1
        return low
