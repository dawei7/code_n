class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0

        while n:
            lowest_bit = n & -n
            if n & (lowest_bit << 1):
                n += lowest_bit
            else:
                n -= lowest_bit
            operations += 1

        return operations
