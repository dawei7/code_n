def solve(m: int, n: int, coordinates: list[list[int]]) -> list[int]:
    black_counts: dict[tuple[int, int], int] = {}

    for row, column in coordinates:
        for top in (row - 1, row):
            if not 0 <= top < m - 1:
                continue

            for left in (column - 1, column):
                if 0 <= left < n - 1:
                    block = (top, left)
                    black_counts[block] = black_counts.get(block, 0) + 1

    answer = [0] * 5
    for count in black_counts.values():
        answer[count] += 1

    answer[0] = (m - 1) * (n - 1) - len(black_counts)
    return answer
