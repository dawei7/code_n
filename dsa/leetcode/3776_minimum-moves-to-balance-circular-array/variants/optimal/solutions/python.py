def solve(balance: list[int]) -> int:
    if sum(balance) < 0:
        return -1

    deficit_index = next(
        (index for index, amount in enumerate(balance) if amount < 0),
        None,
    )
    if deficit_index is None:
        return 0

    n = len(balance)
    needed = -balance[deficit_index]
    available_by_distance = sorted(
        (
            (min(abs(index - deficit_index), n - abs(index - deficit_index)), amount)
            for index, amount in enumerate(balance)
            if amount > 0
        ),
        key=lambda donor: donor[0],
    )

    answer = 0
    for distance, available in available_by_distance:
        used = min(needed, available)
        answer += distance * used
        needed -= used
        if needed == 0:
            return answer

    return -1
