class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        capacities = []
        left_minimum = float("inf")
        for height in warehouse:
            left_minimum = min(left_minimum, height)
            capacities.append(left_minimum)

        right_minimum = float("inf")
        for index in range(len(warehouse) - 1, -1, -1):
            right_minimum = min(right_minimum, warehouse[index])
            capacities[index] = max(capacities[index], right_minimum)

        boxes.sort()
        capacities.sort()
        box_index = 0

        for capacity in capacities:
            if box_index < len(boxes) and boxes[box_index] <= capacity:
                box_index += 1

        return box_index
