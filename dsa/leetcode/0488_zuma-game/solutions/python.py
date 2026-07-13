"""Breadth-first useful-insertion search for LeetCode 488."""

from collections import Counter, deque


COLORS = "RYBGW"


def _collapse(board: str) -> str:
    while board:
        pieces: list[str] = []
        removed = False
        start = 0
        while start < len(board):
            end = start + 1
            while end < len(board) and board[end] == board[start]:
                end += 1
            if end - start >= 3:
                removed = True
            else:
                pieces.append(board[start:end])
            start = end
        if not removed:
            return board
        board = "".join(pieces)
    return ""


def solve(board: str, hand: str) -> int:
    hand_counts = Counter(hand)
    initial_counts = tuple(hand_counts[color] for color in COLORS)
    initial_board = _collapse(board)
    if not initial_board:
        return 0

    queue = deque([(initial_board, initial_counts, 0)])
    visited = {(initial_board, initial_counts)}

    while queue:
        state, counts, used = queue.popleft()
        for position in range(len(state) + 1):
            for color_index, color in enumerate(COLORS):
                if counts[color_index] == 0:
                    continue
                if position > 0 and state[position - 1] == color:
                    continue
                joins_color = position < len(state) and state[position] == color
                splits_pair = (
                    0 < position < len(state)
                    and state[position - 1] == state[position]
                    and state[position] != color
                )
                if not joins_color and not splits_pair:
                    continue

                remaining = list(counts)
                remaining[color_index] -= 1
                next_counts = tuple(remaining)
                next_board = _collapse(state[:position] + color + state[position:])
                if not next_board:
                    return used + 1
                next_state = (next_board, next_counts)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_board, next_counts, used + 1))

    return -1
