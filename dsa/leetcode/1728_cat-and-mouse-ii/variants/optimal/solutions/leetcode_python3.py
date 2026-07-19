from collections import deque
from typing import List


class Solution:
    def canMouseWin(
        self, grid: List[str], catJump: int, mouseJump: int
    ) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        cells = []
        index = {}
        mouse_start = cat_start = food = -1

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "#":
                    continue
                node = len(cells)
                cells.append((row, column))
                index[(row, column)] = node
                if grid[row][column] == "M":
                    mouse_start = node
                elif grid[row][column] == "C":
                    cat_start = node
                elif grid[row][column] == "F":
                    food = node

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def build_moves(jump: int) -> List[List[int]]:
            moves = []
            for node, (row, column) in enumerate(cells):
                reachable = [node]
                for row_step, column_step in directions:
                    for distance in range(1, jump + 1):
                        next_row = row + row_step * distance
                        next_column = column + column_step * distance
                        if (
                            next_row < 0
                            or next_row >= rows
                            or next_column < 0
                            or next_column >= columns
                            or grid[next_row][next_column] == "#"
                        ):
                            break
                        reachable.append(index[(next_row, next_column)])
                moves.append(reachable)
            return moves

        mouse_moves = build_moves(mouseJump)
        cat_moves = build_moves(catJump)
        nodes = len(cells)
        states = nodes * nodes * 2
        winner = [0] * states
        distance = [0] * states
        remaining = [0] * states
        longest_child = [0] * states
        queue = deque()

        def state(mouse: int, cat: int, turn: int) -> int:
            return ((mouse * nodes + cat) << 1) | turn

        for mouse in range(nodes):
            for cat in range(nodes):
                for turn in range(2):
                    current = state(mouse, cat, turn)
                    remaining[current] = (
                        len(mouse_moves[mouse])
                        if turn == 0
                        else len(cat_moves[cat])
                    )

                    if cat == food or cat == mouse:
                        winner[current] = 2
                        queue.append(current)
                    elif mouse == food:
                        winner[current] = 1
                        queue.append(current)

        while queue:
            child = queue.popleft()
            child_distance = distance[child]
            turn = child & 1
            pair = child >> 1
            cat = pair % nodes
            mouse = pair // nodes
            child_winner = winner[child]

            if turn == 1:
                predecessors = (
                    state(previous_mouse, cat, 0)
                    for previous_mouse in mouse_moves[mouse]
                )
                mover = 1
            else:
                predecessors = (
                    state(mouse, previous_cat, 1)
                    for previous_cat in cat_moves[cat]
                )
                mover = 2

            for previous in predecessors:
                if winner[previous] != 0:
                    continue

                if child_winner == mover:
                    winner[previous] = mover
                    distance[previous] = child_distance + 1
                    queue.append(previous)
                    continue

                remaining[previous] -= 1
                longest_child[previous] = max(
                    longest_child[previous], child_distance
                )
                if remaining[previous] == 0:
                    winner[previous] = child_winner
                    distance[previous] = longest_child[previous] + 1
                    queue.append(previous)

        start = state(mouse_start, cat_start, 0)
        return winner[start] == 1 and distance[start] <= 1000
