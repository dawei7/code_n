class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        remaining = sum(apple)

        for boxes_used, box_capacity in enumerate(
            sorted(capacity, reverse=True), start=1
        ):
            remaining -= box_capacity
            if remaining <= 0:
                return boxes_used

        return len(capacity)
