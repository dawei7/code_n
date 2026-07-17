def solve(boxTypes: list[list[int]], truckSize: int) -> int:
    total_units = 0
    for number_of_boxes, units_per_box in sorted(
        boxTypes, key=lambda box_type: box_type[1], reverse=True
    ):
        loaded = min(number_of_boxes, truckSize)
        total_units += loaded * units_per_box
        truckSize -= loaded
        if truckSize == 0:
            break
    return total_units
