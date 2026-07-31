def solve(plantTime: list[int], growTime: list[int]) -> int:
    planted = 0
    answer = 0
    for growth, planting in sorted(
        zip(growTime, plantTime),
        reverse=True,
    ):
        planted += planting
        answer = max(answer, planted + growth)
    return answer
