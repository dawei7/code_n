## Description

Design a Snake game on a screen with `height` rows and `width` columns. The snake begins at the upper-left cell `(0,0)` with length `1`.

The array `food` lists food positions in appearance order, with `food[i] = [r_i,c_i]`. Eating a piece increases both the snake's length and the score by `1`. Food appears one piece at a time: piece `i + 1` is unavailable until piece `i` has been eaten. A newly appearing piece is guaranteed not to occupy the snake's current body.

The game ends when the head moves beyond the screen or, after a move, occupies a cell still occupied by the snake's body.

Implement the `SnakeGame` class:

- `SnakeGame(int width, int height, int[][] food)` initializes the screen, snake, and ordered food positions.
- `int move(String direction)` moves once in direction `"U"`, `"D"`, `"L"`, or `"R"`. Return the updated score, or `-1` if that move ends the game.
