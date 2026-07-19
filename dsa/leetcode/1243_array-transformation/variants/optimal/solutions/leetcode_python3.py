from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        values = arr[:]
        active = set(range(1, len(values) - 1))

        while active:
            changes = []
            for index in active:
                if (
                    values[index] < values[index - 1]
                    and values[index] < values[index + 1]
                ):
                    changes.append((index, 1))
                elif (
                    values[index] > values[index - 1]
                    and values[index] > values[index + 1]
                ):
                    changes.append((index, -1))
            if not changes:
                break

            for index, delta in changes:
                values[index] += delta
            active = {
                neighbor
                for index, _ in changes
                for neighbor in (index - 1, index, index + 1)
                if 0 < neighbor < len(values) - 1
            }

        return values
