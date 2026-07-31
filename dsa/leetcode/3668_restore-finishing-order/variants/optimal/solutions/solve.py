def solve(order: list[int], friends: list[int]) -> list[int]:
    friend_ids = set(friends)
    return [participant for participant in order if participant in friend_ids]
