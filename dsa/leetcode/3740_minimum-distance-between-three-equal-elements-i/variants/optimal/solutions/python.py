def solve(nums: list[int]) -> int:
    recent: dict[int, tuple[int, ...]] = {}
    answer: int | None = None

    for index, value in enumerate(nums):
        positions = recent.get(value, ())
        if len(positions) == 2:
            distance = 2 * (index - positions[0])
            answer = distance if answer is None else min(answer, distance)
            recent[value] = (positions[1], index)
        else:
            recent[value] = positions + (index,)

    return -1 if answer is None else answer
