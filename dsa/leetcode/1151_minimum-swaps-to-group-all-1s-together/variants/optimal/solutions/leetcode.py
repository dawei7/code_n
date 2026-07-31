class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        if ones <= 1:
            return 0
        zeros = ones - sum(data[:ones])
        best = zeros
        for right in range(ones, len(data)):
            zeros += data[right - ones] - data[right]
            best = min(best, zeros)
        return best
