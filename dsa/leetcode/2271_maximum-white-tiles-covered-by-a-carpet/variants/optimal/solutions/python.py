def solve(tiles: list[list[int]], carpetLen: int) -> int:
    ordered = sorted(tiles)
    left = 0
    covered = 0
    answer = 0

    for start, end in ordered:
        covered += end - start + 1
        carpet_start = end - carpetLen + 1

        while ordered[left][1] < carpet_start:
            covered -= ordered[left][1] - ordered[left][0] + 1
            left += 1

        uncovered_left = max(0, carpet_start - ordered[left][0])
        answer = max(answer, covered - uncovered_left)
        if answer == carpetLen:
            return answer

    return answer
