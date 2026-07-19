def solve(pieces: list[str], positions: list[list[int]]) -> int:
    directions = {
        "rook": ((1, 0), (-1, 0), (0, 1), (0, -1)),
        "bishop": ((1, 1), (1, -1), (-1, 1), (-1, -1)),
        "queen": (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1),
        ),
    }

    all_moves = []
    for piece, (row, column) in zip(pieces, positions):
        moves = [(0, 0, 0)]
        for row_step, column_step in directions[piece]:
            distance = 1
            while (
                1 <= row + row_step * distance <= 8
                and 1 <= column + column_step * distance <= 8
            ):
                moves.append((row_step, column_step, distance))
                distance += 1
        all_moves.append(moves)

    trajectories = [
        [
            tuple(
                (
                    positions[piece_index][0] + move[0] * min(time, move[2]),
                    positions[piece_index][1] + move[1] * min(time, move[2]),
                )
                for time in range(8)
            )
            for move in moves
        ]
        for piece_index, moves in enumerate(all_moves)
    ]

    compatibility = {}
    for first in range(len(pieces)):
        for second in range(first + 1, len(pieces)):
            compatible_pairs = set()
            for first_index, first_move in enumerate(all_moves[first]):
                for second_index, second_move in enumerate(all_moves[second]):
                    if all(
                        first_square != second_square
                        for first_square, second_square in zip(
                            trajectories[first][first_index],
                            trajectories[second][second_index],
                        )
                    ):
                        compatible_pairs.add((first_index, second_index))
            compatibility[first, second] = compatible_pairs

    chosen = []

    def backtrack(piece_index: int) -> int:
        if piece_index == len(pieces):
            return 1

        valid = 0
        for move_index in range(len(all_moves[piece_index])):
            if all(
                (chosen[previous], move_index)
                in compatibility[previous, piece_index]
                for previous in range(piece_index)
            ):
                chosen.append(move_index)
                valid += backtrack(piece_index + 1)
                chosen.pop()
        return valid

    return backtrack(0)
