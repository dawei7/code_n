# Shortest Path in a Grid with Obstacles Elimination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1293 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix in which zero is an empty cell and one is an obstacle. Starting at the empty upper-left cell, one step moves up, down, left, or right to an in-bounds neighboring cell.

Reach the empty lower-right cell in the minimum number of steps. During the walk you may eliminate at most `k` obstacles, allowing those obstacle cells to be entered. Return `-1` if no walk satisfies the elimination budget.

### Function Contract
**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 40$ and both endpoint cells are zero.
- `k`: an integer satisfying $1 \le k \le mn$.
- Let $S = mn(k+1)$ be the maximum number of position-and-budget states.

**Return value**

The fewest four-direction steps from $(0,0)$ to $(m-1,n-1)$ using at most `k` obstacle eliminations, or `-1` when no such walk exists.

### Examples
**Example 1**

- Input: `grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]`, `k = 1`
- Output: `6`

**Example 2**

- Input: `grid = [[0,1,1],[1,1,1],[1,0,0]]`, `k = 1`
- Output: `-1`

**Example 3**

- Input: `grid = [[0,1],[0,0]]`, `k = 1`
- Output: `2`

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

A position alone is not a complete search state: reaching the same cell with more eliminations remaining may enable a path that a depleted arrival cannot follow. Breadth-first search therefore carries `(row, column, remaining)`, and entering an obstacle decreases `remaining` by one.

**Dominance at one cell.** For each cell, remember the greatest remaining budget seen there. If a new arrival has no more budget than that record, it is dominated: it occurs no earlier than the recorded BFS arrival and has no additional future choices. Discard it. An arrival with more remaining budget can be useful, so update the record and enqueue it.

Breadth-first layers contain walks in increasing step count. Consequently, the first generated target state has minimum length. Dominance pruning never removes a uniquely useful continuation, because the earlier state at that cell has at least the same budget. If `k` is at least the number of intermediate cells on a Manhattan route, obstacles cannot prevent the direct length $m+n-2$; this safe shortcut also handles large budgets.

#### Complexity detail

There are at most $S=mn(k+1)$ distinct position-and-remaining-budget states, and each has four constant-time transitions, giving $O(S)$ worst-case time. The queue may contain $O(S)$ states; the dominance table itself uses only $O(mn)$ entries, so the overall auxiliary-space bound is $O(S)$.

#### Alternatives and edge cases

- **Visited positions only:** Marking a cell visited without its budget can discard a later arrival that retains more eliminations and is necessary for a solution.
- **List-based Dijkstra:** Unit edge costs make BFS sufficient; repeatedly scanning an unsorted state list for the minimum distance adds quadratic selection work.
- **Single-cell grid:** Start already equals target, so the answer is zero.
- **Large elimination budget:** When a Manhattan route's intermediate cells can all be removed, return $m+n-2$ immediately.
- **Unreachable target:** Exhausting every nondominated state without reaching the target requires returning `-1`.

</details>
