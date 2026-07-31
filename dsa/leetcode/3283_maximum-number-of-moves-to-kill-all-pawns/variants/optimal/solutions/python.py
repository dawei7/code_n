from collections import deque
from functools import lru_cache


def solve(kx: int, ky: int, positions: list[list[int]]) -> int:
    pawns = len(positions)
    points = positions + [[kx, ky]]
    moves = (
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1),
    )
    distances = [[0] * (pawns + 1) for _ in range(pawns + 1)]

    for source_index, (source_x, source_y) in enumerate(points[:-1]):
        targets = {
            tuple(points[target_index]): target_index
            for target_index in range(source_index + 1, pawns + 1)
        }
        board = [[-1] * 50 for _ in range(50)]
        board[source_x][source_y] = 0
        queue = deque([(source_x, source_y)])

        while queue:
            x, y = queue.popleft()
            target_index = targets.pop((x, y), None)
            if target_index is not None:
                distance = board[x][y]
                distances[source_index][target_index] = distance
                distances[target_index][source_index] = distance
                if not targets:
                    break

            for dx, dy in moves:
                next_x = x + dx
                next_y = y + dy
                if (
                    0 <= next_x < 50
                    and 0 <= next_y < 50
                    and board[next_x][next_y] == -1
                ):
                    board[next_x][next_y] = board[x][y] + 1
                    queue.append((next_x, next_y))

    @lru_cache(None)
    def play(current: int, remaining: int) -> int:
        if remaining == 0:
            return 0

        alice_turn = (pawns - remaining.bit_count()) % 2 == 0
        result = -1 if alice_turn else float("inf")
        choices = remaining

        while choices:
            pawn_bit = choices & -choices
            pawn_index = pawn_bit.bit_length() - 1
            total = distances[current][pawn_index] + play(
                pawn_index, remaining ^ pawn_bit
            )
            result = max(result, total) if alice_turn else min(result, total)
            choices -= pawn_bit

        return result

    return play(pawns, (1 << pawns) - 1)
