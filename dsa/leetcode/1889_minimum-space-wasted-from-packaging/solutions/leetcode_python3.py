from bisect import bisect_right
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        modulo = 1_000_000_007
        ordered_packages = sorted(packages)
        minimum_capacity = None

        for supplier in boxes:
            ordered_boxes = sorted(supplier)
            if ordered_boxes[-1] < ordered_packages[-1]:
                continue

            capacity = 0
            packed = 0
            for box_size in ordered_boxes:
                next_packed = bisect_right(ordered_packages, box_size, lo=packed)
                capacity += (next_packed - packed) * box_size
                packed = next_packed
                if packed == len(ordered_packages):
                    break

            if minimum_capacity is None or capacity < minimum_capacity:
                minimum_capacity = capacity

        if minimum_capacity is None:
            return -1
        return (minimum_capacity - sum(ordered_packages)) % modulo
