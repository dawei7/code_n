class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        selected_ones = min(numOnes, k)
        selected_neg_ones = max(0, k - numOnes - numZeros)
        return selected_ones - selected_neg_ones
