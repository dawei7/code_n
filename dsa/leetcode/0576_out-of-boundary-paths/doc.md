# Out of Boundary Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 576 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/out-of-boundary-paths/) |

## Problem Description
### Goal
Place a ball at `(startRow, startColumn)` inside an $m \times n$ grid. On each move, the ball may travel one cell up, down, left, or right. Count the paths that move the ball across any grid boundary using at most `maxMove` moves.

Different sequences of directions count as different paths, and a path is counted when it first leaves the grid; no additional moves are made after that exit. Return the total modulo `1,000,000,007`. Paths may leave before all allowed moves are used, while a sequence that remains inside after `maxMove` moves contributes nothing.

### Function Contract
**Inputs**

- `m: int`: number of grid rows
- `n: int`: number of grid columns
- `maxMove: int`: maximum number of moves the ball may make
- `startRow: int`: starting row inside the grid
- `startColumn: int`: starting column inside the grid

**Return value**

- The number of direction sequences that cross the grid boundary within at most `maxMove` moves, modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0`
- Output: `6`

**Example 2**

- Input: `m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1`
- Output: `12`

**Example 3**

- Input: `m = 3, n = 4, maxMove = 0, startRow = 1, startColumn = 2`
- Output: `0`

### Required Complexity

- **Time:** $O(m n maxMove)$
- **Space:** $O(m n)$

<details>
<summary>Approach</summary>

#### General

**Track paths that are still inside**

Let the current grid store how many direction sequences place the ball at each cell after exactly the moves processed so far without having left the board. Initially only the starting cell has count one.

**Advance one move layer**

For every nonzero cell count, consider the four orthogonal directions. Add the count to the corresponding cell in a fresh next grid when the destination remains inside. When the destination is outside, add the count directly to the answer because that direction sequence has now produced a valid path.

**Stop extending escaped paths**

An exited path is accumulated once and never placed into the next grid. Consequently, every counted sequence is classified at its first boundary crossing and cannot be counted again on later layers. Repeating this transition through `maxMove` layers includes exits after any permitted number of moves.

**Why every valid path is counted exactly once**

Before each layer, the grid count at a cell equals the number of still-inside direction prefixes ending there. Extending each prefix by all four possible directions generates every next prefix once. Inside extensions preserve the state invariant; outside extensions are precisely the newly completed valid paths. Induction over the move layers therefore covers every allowed path and no invalid or duplicate path.

#### Complexity detail

Each of at most `maxMove` layers scans `m n` cells and four constant directions, for $O(m n maxMove)$ time. The current and next grids use $O(m n)$ space. Counts are reduced modulo `1,000,000,007` throughout.

#### Alternatives and edge cases

- **Top-down memoization:** cache the number of exits from each `(row, column, movesRemaining)` state; it has the same time bound but uses $O(m n maxMove)$ cache space and recursion.
- **Full three-dimensional table:** makes every move layer explicit but uses $O(m n maxMove)$ space unnecessarily.
- **Unmemoized path enumeration:** is correct for tiny inputs but can explore `4 ** maxMove` direction sequences.
- **Recompute every exact path length separately:** avoids exponential enumeration but repeats earlier layers and takes $O(m n maxMove^2)$ time.
- **Zero moves:** no boundary can be crossed, so the answer is zero.
- **One-cell grid:** each of the four first moves exits immediately; escaped paths are not extended further.
- **Corner and edge starts:** multiple first directions may leave the grid and must each contribute separately.
- **Modulo reduction:** apply it during transitions to keep all intermediate counts bounded.

</details>
