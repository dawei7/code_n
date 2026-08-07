class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        best_index = -1
        best_capacity = float("inf")

        for index, box_capacity in enumerate(capacity):
            if itemSize <= box_capacity < best_capacity:
                best_capacity = box_capacity
                best_index = index

        return best_index
