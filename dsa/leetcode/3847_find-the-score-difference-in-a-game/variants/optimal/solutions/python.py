def solve(nums: list[int]) -> int:
    first_player_active = True
    difference = 0

    for index, points in enumerate(nums):
        if points % 2 == 1:
            first_player_active = not first_player_active
        if (index + 1) % 6 == 0:
            first_player_active = not first_player_active

        if first_player_active:
            difference += points
        else:
            difference -= points

    return difference
