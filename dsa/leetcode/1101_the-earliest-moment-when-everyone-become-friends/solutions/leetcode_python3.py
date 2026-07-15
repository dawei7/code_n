from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(person: int) -> int:
            while person != parent[person]:
                parent[person] = parent[parent[person]]
                person = parent[person]
            return person

        for timestamp, first, second in sorted(logs):
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                continue
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
            components -= 1
            if components == 1:
                return timestamp
        return -1
