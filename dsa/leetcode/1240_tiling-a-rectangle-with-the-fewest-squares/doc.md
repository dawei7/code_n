# Tiling a Rectangle with the Fewest Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1240 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) |

## Problem Description

### Goal

Given an `n` by `m` rectangle, tile its entire area with axis-aligned squares whose side lengths are positive integers. Squares may have different sizes, but they must remain inside the rectangle, must not overlap, and must leave no uncovered area.

Return the minimum number of squares required. Rotating the rectangle does not change the problem, and a square matching the whole rectangle counts as one tile. The objective concerns the number of squares rather than their total area, since every valid tiling necessarily covers the same area.

### Function Contract

**Inputs**

- `n`: One rectangle dimension, where $1\le n\le13$.
- `m`: The other rectangle dimension, where $1\le m\le13$.

Define $h=\min(n,m)$ and $w=\max(n,m)$.

**Return value**

- The minimum number of integer-sided squares in a complete tiling of the rectangle.

### Examples

**Example 1**

- Input: `n = 2`, `m = 3`
- Output: `3`

One $2$ by $2$ square and two $1$ by $1$ squares tile the rectangle.

**Example 2**

- Input: `n = 5`, `m = 8`
- Output: `5`

No tiling with four squares exists, while five appropriately sized squares suffice.

**Example 3**

- Input: `n = 11`, `m = 13`
- Output: `6`

This rectangle has a six-square tiling, which is optimal.

### Required Complexity

- **Time:** $O\left(wh(h+1)^w\right)$
- **Space:** $O\left((h+1)^w\right)$

<details>
<summary>Approach</summary>

#### General

**Represent only the exposed skyline.** Normalize the rectangle so its height is $h$ and width is $w$. Store `heights[column]`, the filled height of each column. A skyline with every entry equal to $h$ is a complete tiling; no cell-level board is needed.

**Fill the first lowest segment.** Find the leftmost column having the minimum height and the consecutive run of columns sharing that height. Any completion must cover the first exposed cell there. A square placed with its lower edge on this segment can have side at most the run length and at most `h - minimum_height`. Try every such side length from largest to smallest by adding it to the affected heights, then backtrack.

**Prune repeated and uncompetitive states.** Track the fewest squares previously used to reach each skyline. If the same skyline is reached with no fewer squares, it cannot improve the final answer. Also stop a branch once its used count reaches the best complete tiling found so far. Every legal tiling has a square covering the chosen first exposed cell, and the search tries every possible size for that square, so pruning never removes a potentially better completion.

#### Complexity detail

Each of the $w$ skyline entries has $h+1$ possible heights, giving at most $(h+1)^w$ states. Processing a state scans $w$ columns and tries at most $h$ square sizes, yielding the conservative time bound $O\left(wh(h+1)^w\right)$. Memoized skyline costs dominate the recursion stack, so space is $O\left((h+1)^w\right)$.

#### Alternatives and edge cases

- **Cell-grid backtracking:** Filling the first uncovered cell is exact, but copying or scanning an $n$ by $m$ board creates substantially more state and repeated configurations.
- **Skyline search without memoization:** Branch-and-bound remains correct but can rediscover the same skyline through many different square orders.
- **Greedy largest square:** Always taking the largest currently fitting square is fast but does not guarantee the fewest squares for irregular remaining regions.
- **Dynamic programming by straight cuts:** Splitting only across the full width or height misses optimal non-guillotine tilings, including important hard cases.
- **Square rectangle:** When `n == m`, one square is immediately optimal.
- **Unit dimension:** A $1$ by $m$ rectangle requires exactly $m$ unit squares.
- **Rotated dimensions:** Normalizing to $h\le w$ reduces the skyline-state exponent without changing the answer.

</details>
