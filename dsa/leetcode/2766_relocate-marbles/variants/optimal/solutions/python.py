def solve(
    nums: list[int],
    moveFrom: list[int],
    moveTo: list[int],
) -> list[int]:
    occupied = set(nums)

    for source, destination in zip(moveFrom, moveTo):
        occupied.remove(source)
        occupied.add(destination)

    return sorted(occupied)
