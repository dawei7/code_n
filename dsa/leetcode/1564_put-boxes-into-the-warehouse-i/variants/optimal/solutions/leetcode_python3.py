from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ordered_boxes = sorted(boxes)
        clearance = []
        minimum_height = float("inf")
        for room_height in warehouse:
            minimum_height = min(minimum_height, room_height)
            clearance.append(minimum_height)

        box_index = 0
        for room_height in reversed(clearance):
            if box_index == len(ordered_boxes):
                break
            if ordered_boxes[box_index] <= room_height:
                box_index += 1

        return box_index
