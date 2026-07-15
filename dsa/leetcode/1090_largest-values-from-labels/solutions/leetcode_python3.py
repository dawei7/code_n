from typing import List


class Solution:
    def largestValsFromLabels(
        self,
        values: List[int],
        labels: List[int],
        numWanted: int,
        useLimit: int,
    ) -> int:
        label_usage = {}
        total = 0
        selected = 0

        for value, label in sorted(zip(values, labels), reverse=True):
            if selected == numWanted:
                break
            if label_usage.get(label, 0) == useLimit:
                continue
            label_usage[label] = label_usage.get(label, 0) + 1
            total += value
            selected += 1

        return total
