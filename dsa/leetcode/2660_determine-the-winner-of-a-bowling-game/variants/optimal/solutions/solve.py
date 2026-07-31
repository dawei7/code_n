def solve(player1: list[int], player2: list[int]) -> int:
    def score(rolls: list[int]) -> int:
        total = 0
        for index, pins in enumerate(rolls):
            doubled = (index >= 1 and rolls[index - 1] == 10) or (index >= 2 and rolls[index - 2] == 10)
            total += pins * (2 if doubled else 1)
        return total

    score1 = score(player1)
    score2 = score(player2)
    if score1 == score2:
        return 0
    return 1 if score1 > score2 else 2
