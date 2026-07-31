from bisect import bisect_left


def solve(houses: list[int], heaters: list[int]) -> int:
    heaters.sort()
    radius = 0
    for house in houses:
        insertion = bisect_left(heaters, house)
        right = heaters[insertion] - house if insertion < len(heaters) else float("inf")
        left = house - heaters[insertion - 1] if insertion > 0 else float("inf")
        radius = max(radius, min(left, right))
    return int(radius)
