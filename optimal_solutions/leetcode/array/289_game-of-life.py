def solve(board: list[list[int]]) -> None:
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    # State mapping:
    # 0: Dead -> Dead
    # 1: Live -> Live
    # 2: Live -> Dead
    # 3: Dead -> Live

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            # Check all 8 neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Check if neighbor is currently live (1 or 2)
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1
            
            # Apply rules
            if board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 2
            else:
                if live_neighbors == 3:
                    board[r][c] = 3

    # Final pass to normalize states
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == 3:
                board[r][c] = 1
