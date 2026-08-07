## Description

According to <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by under-population.

- Any live cell with two or three live neighbors lives on to the next generation.

- Any live cell with more than three live neighbors dies, as if by over-population.

- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.

Given the current state of the `board`, **update** the `board` to reflect its next state.

**Note** that you do not need to return anything.
### Function Contract

**Inputs**

- `board`: A mutable rectangular matrix whose entries are `0` for dead cells and `1` for live cells.

**Return value**

Return `None`. Mutate `board` in place to the next simultaneously computed generation.

### Examples

#### Example 1

![](images/grid1.jpg)

- **Input:** $board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]$
- **Output:** `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`
#### Example 2

![](images/grid2.jpg)

- **Input:** $board = [[1,1],[1,0]]$
- **Output:** `[[1,1],[1,1]]`
### Constraints

- $m = \text{board.length}$

- $n = \text{board}[i].length$

- $1 \le m, n \le 25$

- $\text{board}[i][j]$ is `0` or `1`.

**Follow up:**

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.

- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?