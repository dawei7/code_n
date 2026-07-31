from typing import List


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_group = max(groups)
        first_index = {}
        for index, value in enumerate(elements):
            if value <= max_group and value not in first_index:
                first_index[value] = index

        best_for_value = [-1] * (max_group + 1)
        for value, index in first_index.items():
            for multiple in range(value, max_group + 1, value):
                if best_for_value[multiple] == -1 or index < best_for_value[multiple]:
                    best_for_value[multiple] = index

        return [best_for_value[group] for group in groups]
