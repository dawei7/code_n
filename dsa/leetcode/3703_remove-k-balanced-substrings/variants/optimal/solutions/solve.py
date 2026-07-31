def solve(s: str, k: int) -> str:
    runs: list[list[str | int]] = []

    for character in s:
        if runs and runs[-1][0] == character:
            runs[-1][1] += 1
        else:
            runs.append([character, 1])

        if character == ")" and len(runs) >= 2 and runs[-1][1] == k and runs[-2][0] == "(" and runs[-2][1] >= k:
            runs.pop()
            runs[-1][1] -= k
            if runs[-1][1] == 0:
                runs.pop()

    return "".join(character * count for character, count in runs)
