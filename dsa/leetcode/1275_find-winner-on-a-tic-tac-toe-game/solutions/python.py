def solve(moves):
    board = [[0] * 3 for _ in range(3)]
    for turn, (r, c) in enumerate(moves):
        board[r][c] = 1 if turn % 2 == 0 else -1
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    if any(sum(line) == 3 for line in lines):
        return "A"
    if any(sum(line) == -3 for line in lines):
        return "B"
    return "Draw" if len(moves) == 9 else "Pending"
