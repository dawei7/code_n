class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        adjacency = [0] * n
        for u, v in edges:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u

        one_nodes = 0
        for node, value in enumerate(nums):
            if value == 1:
                one_nodes |= 1 << node

        answer = 0
        for subset in range(1, 1 << n):
            if (subset & one_nodes).bit_count() % 2 == 1:
                continue

            reached = 0
            frontier = subset & -subset
            while frontier:
                node_bit = frontier & -frontier
                frontier ^= node_bit
                reached |= node_bit
                node = node_bit.bit_length() - 1
                frontier |= adjacency[node] & subset & ~reached

            if reached == subset:
                answer += 1

        return answer
