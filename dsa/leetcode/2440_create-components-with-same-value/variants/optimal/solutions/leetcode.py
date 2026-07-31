from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        node_count = len(nums)
        adjacency = [[] for _ in range(node_count)]
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)

        parent = [-1] * node_count
        order = [0]
        for node in order:
            for neighbor in adjacency[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        total = sum(nums)
        maximum_components = total // max(nums)

        for component_count in range(maximum_components, 1, -1):
            if total % component_count:
                continue

            target = total // component_count
            subtotal = nums.copy()
            valid = True

            for node in reversed(order[1:]):
                if subtotal[node] > target:
                    valid = False
                    break
                if subtotal[node] < target:
                    subtotal[parent[node]] += subtotal[node]

            if valid and subtotal[0] == target:
                return component_count - 1

        return 0
