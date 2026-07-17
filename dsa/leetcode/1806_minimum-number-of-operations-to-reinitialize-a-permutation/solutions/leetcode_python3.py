class Solution:
    def reinitializePermutation(self, n: int) -> int:
        position = 1
        operations = 0

        while True:
            if position % 2 == 0:
                position //= 2
            else:
                position = n // 2 + (position - 1) // 2
            operations += 1

            if position == 1:
                return operations
