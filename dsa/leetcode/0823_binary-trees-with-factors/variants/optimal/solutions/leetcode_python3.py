from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulus = 1_000_000_007
        values = sorted(arr)
        ways = {}
        total = 0

        for index, root in enumerate(values):
            root_ways = 1
            for factor_index in range(index):
                left = values[factor_index]
                if root % left != 0:
                    continue
                right = root // left
                if right in ways:
                    root_ways += ways[left] * ways[right]

            ways[root] = root_ways % modulus
            total = (total + ways[root]) % modulus

        return total
