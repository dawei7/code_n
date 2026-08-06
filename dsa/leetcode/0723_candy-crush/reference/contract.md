## Function Contract

`solve(board: list[list[int]]) -> list[list[int]]`

Let $m$ be the number of rows and $n$ the number of columns.

**Inputs**

- `board`: an $m \times n$ rectangular matrix of positive candy-type integers representing the post-move game state.

**Return value**

Return the stable matrix after every required simultaneous crush and gravity round. A returned `0` denotes an empty cell; empty cells remain above all surviving candies in their column because no new candies enter the board.
