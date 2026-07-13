def solve(ghosts: list[list[int]], target: list[int]) -> bool:
    player_distance = abs(target[0]) + abs(target[1])
    return all(
        abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) > player_distance
        for ghost in ghosts
    )
