from typing import Dict, List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.values: Dict[int, int] = {
            index: value for index, value in enumerate(nums) if value != 0
        }

    def dotProduct(self, vec: "SparseVector") -> int:
        smaller = self.values
        larger = vec.values
        if len(smaller) > len(larger):
            smaller, larger = larger, smaller

        return sum(value * larger.get(index, 0) for index, value in smaller.items())
