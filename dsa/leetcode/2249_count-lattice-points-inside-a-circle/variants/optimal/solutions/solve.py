def solve(circles: list[list[int]]) -> int:
    covered = set()
    for center_x, center_y, radius in circles:
        squared_radius = radius * radius
        for x in range(center_x - radius, center_x + radius + 1):
            squared_x = (x - center_x) ** 2
            for y in range(center_y - radius, center_y + radius + 1):
                if squared_x + (y - center_y) ** 2 <= squared_radius:
                    covered.add((x, y))
    return len(covered)
