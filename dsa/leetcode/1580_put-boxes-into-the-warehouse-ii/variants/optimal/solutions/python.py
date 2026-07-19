def solve(boxes: list[int], warehouse: list[int]) -> int:
    capacities: list[int] = []
    left_minimum = float("inf")

    for height in warehouse:
        left_minimum = min(left_minimum, height)
        capacities.append(int(left_minimum))

    right_minimum = float("inf")
    for index in range(len(warehouse) - 1, -1, -1):
        right_minimum = min(right_minimum, warehouse[index])
        capacities[index] = max(capacities[index], int(right_minimum))

    boxes = sorted(boxes)
    capacities.sort()
    box_index = 0

    for capacity in capacities:
        if box_index < len(boxes) and boxes[box_index] <= capacity:
            box_index += 1

    return box_index
