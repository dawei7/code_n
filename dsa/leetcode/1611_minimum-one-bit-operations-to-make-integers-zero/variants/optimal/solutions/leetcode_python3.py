class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        operations = 0
        while n:
            operations ^= n
            n >>= 1
        return operations
