from collections import deque


class SnakeGame:
    MOVES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def __init__(self, width: int, height: int, food: list[list[int]]) -> None:
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.body = deque([(0, 0)])
        self.occupied = {(0, 0)}
        self.game_over = False

    def move(self, direction: str) -> int:
        if self.game_over:
            return -1

        row, col = self.body[-1]
        row_change, col_change = self.MOVES[direction]
        new_head = (row + row_change, col + col_change)
        new_row, new_col = new_head

        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            self.game_over = True
            return -1

        eating = (
            self.food_index < len(self.food)
            and self.food[self.food_index] == [new_row, new_col]
        )
        if not eating:
            tail = self.body.popleft()
            self.occupied.remove(tail)

        if new_head in self.occupied:
            self.game_over = True
            return -1

        self.body.append(new_head)
        self.occupied.add(new_head)
        if eating:
            self.food_index += 1
        return self.food_index


def solve(width: int, height: int, food: list[list[int]], directions: list[str]) -> list[int]:
    game = SnakeGame(width, height, food)
    return [game.move(direction) for direction in directions]
