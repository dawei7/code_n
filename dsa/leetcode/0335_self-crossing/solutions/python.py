def solve(distance: list[int]) -> bool:
    for index in range(3, len(distance)):
        if (
            distance[index] >= distance[index - 2]
            and distance[index - 1] <= distance[index - 3]
        ):
            return True

        if (
            index >= 4
            and distance[index - 1] == distance[index - 3]
            and distance[index] + distance[index - 4] >= distance[index - 2]
        ):
            return True

        if (
            index >= 5
            and distance[index - 2] >= distance[index - 4]
            and distance[index] + distance[index - 4] >= distance[index - 2]
            and distance[index - 1] <= distance[index - 3]
            and distance[index - 1] + distance[index - 5] >= distance[index - 3]
        ):
            return True
    return False
