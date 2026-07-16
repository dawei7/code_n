class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class DisjointSet:
            def __init__(self, size: int) -> None:
                self.parent = list(range(size + 1))
                self.rank = [0] * (size + 1)
                self.components = size

            def find(self, node: int) -> int:
                while self.parent[node] != node:
                    self.parent[node] = self.parent[self.parent[node]]
                    node = self.parent[node]
                return node

            def union(self, left: int, right: int) -> bool:
                root_left = self.find(left)
                root_right = self.find(right)
                if root_left == root_right:
                    return False
                if self.rank[root_left] < self.rank[root_right]:
                    root_left, root_right = root_right, root_left
                self.parent[root_right] = root_left
                if self.rank[root_left] == self.rank[root_right]:
                    self.rank[root_left] += 1
                self.components -= 1
                return True

        alice = DisjointSet(n)
        bob = DisjointSet(n)
        used = 0

        for edge_type, left, right in edges:
            if edge_type == 3 and alice.union(left, right):
                bob.union(left, right)
                used += 1

        for edge_type, left, right in edges:
            if edge_type == 1 and alice.union(left, right):
                used += 1
            elif edge_type == 2 and bob.union(left, right):
                used += 1

        if alice.components != 1 or bob.components != 1:
            return -1
        return len(edges) - used
