from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_index = 0
        for current in range(1, target[-1] + 1):
            operations.append("Push")
            if current == target[target_index]:
                target_index += 1
                if target_index == len(target):
                    break
            else:
                operations.append("Pop")
        return operations
