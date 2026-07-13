# Minesweeper

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 529 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minesweeper/) |

## Problem Description
### Goal
Given a Minesweeper board and a click on an unrevealed mine `M` or empty square `E`, update the board after that one click. If the clicked cell is a mine, change it to `X` and stop.

Otherwise count mines in all eight neighboring directions. An empty cell with at least one adjacent mine becomes the corresponding digit `1` through `8`. A cell with no adjacent mine becomes `B`, and its adjacent unrevealed empty cells are revealed recursively by the same rules. Return the updated board without changing already revealed digits or expanding through numbered boundary cells.

### Function Contract
**Inputs**

- `board`: a rectangular character matrix using `M` for unrevealed mines and `E` for unrevealed empty squares
- `click`: the `[row, column]` position selected by the player

**Return value**

- The board after processing the click and every forced reveal

### Examples
**Example 1**

- Input: `board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]`
- Output: `[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]`

**Example 2**

- Input: `board = [["E","M"],["E","E"]], click = [0,1]`
- Output: `[["E","X"],["E","E"]]`

**Example 3**

- Input: `board = [["E","E","E"],["E","M","E"],["E","E","E"]], click = [0,0]`
- Output: `[["1","E","E"],["E","M","E"],["E","E","E"]]`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Handle a mine before starting a search**

If the clicked cell contains `M`, replace it with `X` and return immediately. No other square changes after a mine is selected.

**Reveal empty cells as a graph traversal**

Treat each empty square as a vertex connected to its up to eight surrounding squares. Start a queue at the clicked empty cell. When a cell is first scheduled, mark it `B` immediately so another neighbor cannot enqueue it again.

**Stop expansion at numbered boundaries**

For each queued square, inspect only its valid neighbors and count unrevealed mines. A positive count replaces the provisional `B` with the corresponding digit and stops that branch. A zero count remains `B`, and every still-unrevealed empty neighbor is marked and queued.

**Why the revealed region is exact**

Every expanded `B` square has zero adjacent mines, so revealing all of its neighboring empty squares follows the game rule. Numbered squares are revealed when reached but never expanded. The traversal therefore reaches every empty square connected to the click through zero-mine squares and nothing beyond a numbered boundary; immediate marking ensures each square is processed once.

#### Complexity detail

Each of the `rows * cols` cells can enter the queue at most once, and processing examines at most eight neighbors. Time is $O(rows \cdot cols)$. The queue can hold $O(rows \cdot cols)$ cells in the worst case, and the board update is in place.

#### Alternatives and edge cases

- **Recursive depth-first search:** implements the same reveal rule compactly but can exceed the call-stack limit on a large blank region.
- **Explicit depth-first stack:** has the same asymptotic bounds as breadth-first search and differs only in reveal order, which does not affect the final board.
- **Scan the whole board for every revealed cell:** counts adjacent mines correctly but can degrade to quadratic time in the number of cells.
- **Clicked mine:** changes only that cell from `M` to `X`.
- **Board boundary:** neighbor coordinates outside the rectangle must be ignored.
- **Diagonal mine:** counts as adjacent just like horizontal and vertical mines.
- **Numbered square:** is revealed but must not propagate the search farther.
- **Mine cells during expansion:** remain `M`; only a directly clicked mine becomes `X`.

</details>
