# Snakes and Ladders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 909 |
| Difficulty | Medium |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/snakes-and-ladders/) |

## Problem Description
### Goal
An $n\times n$ board has squares labeled from $1$ through $n^2$ in Boustrophedon order: labeling begins at `board[n - 1][0]` in the bottom-left corner, proceeds left to right across that row, and reverses horizontal direction on every row above it. You start on square $1$.

From a current square `curr`, one dice roll lets you choose any square `next` from `curr + 1` through $\min(\texttt{curr}+6,n^2)$. If that square starts a snake or ladder, you must move to its recorded destination; otherwise you remain on `next`. Apply at most one snake or ladder per roll, even when its destination starts another transition. The game ends upon reaching square $n^2$.

Return the least number of dice rolls needed to reach the final square. Return $-1$ when no sequence of rolls can reach it.

### Function Contract
Let $n=\lvert\texttt{board}\rvert$.

**Inputs**

- `board`: an $n\times n$ integer matrix with $2 \leq n \leq 20$. Each cell is $-1$ or a destination label in $[1,n^2]$. A value other than $-1$ marks the start of a snake or ladder. Squares $1$ and $n^2$ do not start transitions.

**Return value**

Return the minimum number of rolls required to reach square $n^2$, or $-1$ if it is unreachable.

### Examples
**Example 1**

- Input: `board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]`
- Output: `4`

One optimal route uses the transitions $2\to15$, $17\to13$, and $14\to35$, then reaches square $36$.

**Example 2**

- Input: `board = [[-1,-1],[-1,3]]`
- Output: `1`

The final square is reachable with one roll.

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Translate the Boustrophedon matrix into labels**

Read matrix rows from bottom to top, traversing the bottom row left to right and reversing the column order after every row. Append the encountered cell values to a one-indexed array `cells`. Then `cells[label]` directly tells whether a labeled square has a snake or ladder, avoiding repeated row-and-column conversion during the search.

**Treat each dice roll as an unweighted graph edge**

Every labeled square is a graph vertex. From `curr`, each of the at most six legal roll results creates one edge. Let `next` be the selected label. Its actual destination is `cells[next]` when that value is not `-1`, and `next` otherwise. Do not inspect the destination cell for another transition, because the rules permit only one snake or ladder per roll.

Run breadth-first search from square $1$. The queue processes all positions reached in fewer rolls before positions reached in more rolls, so the first time square $n^2$ is reached gives the least possible number of dice rolls. Mark each actual destination visited when it is enqueued. Reaching the same square later cannot improve its distance, and suppressing those revisits also prevents cycles caused by snakes. If the queue empties without reaching the target, no legal path exists.

Each generated edge matches exactly one legal roll and its mandatory transition. Conversely, every legal roll appears among the six candidates examined from its current square. Breadth-first search therefore explores precisely the game's reachable states in nondecreasing roll count, establishing both the returned minimum and the $-1$ result.

#### Complexity detail

There are $n^2$ squares. Flattening visits each cell once, and breadth-first search visits each reachable square once while examining at most six rolls, for $O(n^2)$ time. The flattened board, visited set, and queue each hold at most $n^2$ entries, so auxiliary space is $O(n^2)$.

#### Alternatives and edge cases

- **Depth-first search over roll sequences:** It can eventually find routes but does not naturally discover the fewest rolls and may explore exponentially many cyclic paths.
- **Repeated full-board relaxation:** Updating tentative distances until no value changes is correct but can take $O(n^4)$ time over $n^2$ squares.
- **Formula-only movement count:** Dividing the remaining labels by six works only when no snake or ladder changes the graph.
- **Alternating row direction:** Forgetting to reverse every other row attaches transitions to the wrong labels.
- **One transition per roll:** A ladder destination that starts another ladder must not be followed until a later roll lands there directly.
- **Snakes back to visited squares:** The visited set prevents those cycles from making the search infinite.
- **Transition to the target:** Reaching $n^2$ through a snake or ladder finishes the game on that same roll.
- **Unreachable target:** If all possible advances are redirected into an already visited region, return $-1$ after the queue is exhausted.

</details>
