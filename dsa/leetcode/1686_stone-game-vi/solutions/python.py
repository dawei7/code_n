def solve(aliceValues: list[int], bobValues: list[int]) -> int:
    order = sorted(
        range(len(aliceValues)),
        key=lambda index: aliceValues[index] + bobValues[index],
        reverse=True,
    )
    score_difference = 0
    for turn, index in enumerate(order):
        if turn % 2 == 0:
            score_difference += aliceValues[index]
        else:
            score_difference -= bobValues[index]
    return (score_difference > 0) - (score_difference < 0)
