def solve(apple: list[int], capacity: list[int]) -> int:
    remaining = sum(apple)

    for boxes_used, box_capacity in enumerate(
        sorted(capacity, reverse=True), start=1
    ):
        remaining -= box_capacity
        if remaining <= 0:
            return boxes_used

    return len(capacity)
