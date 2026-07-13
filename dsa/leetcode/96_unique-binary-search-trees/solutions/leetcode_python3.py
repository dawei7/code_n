class Solution:
    def numTrees(self, n: int) -> int:
        count = [0] * (n + 1)
        count[0] = 1

        for nodes in range(1, n + 1):
            for left_size in range(nodes):
                right_size = nodes - 1 - left_size
                count[nodes] += count[left_size] * count[right_size]

        return count[n]
