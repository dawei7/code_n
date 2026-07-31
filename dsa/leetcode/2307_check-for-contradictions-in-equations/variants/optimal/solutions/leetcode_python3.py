from typing import List


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        parent = {}
        ratio = {}

        def find(variable: str) -> str:
            if parent[variable] != variable:
                previous_parent = parent[variable]
                parent[variable] = find(previous_parent)
                ratio[variable] *= ratio[previous_parent]
            return parent[variable]

        for (left, right), value in zip(equations, values):
            for variable in (left, right):
                if variable not in parent:
                    parent[variable] = variable
                    ratio[variable] = 1.0

            left_root = find(left)
            right_root = find(right)

            if left_root == right_root:
                if abs(ratio[left] / ratio[right] - value) >= 1e-5:
                    return True
                continue

            parent[left_root] = right_root
            ratio[left_root] = value * ratio[right] / ratio[left]

        return False
