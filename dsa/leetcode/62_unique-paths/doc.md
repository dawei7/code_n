# Unique Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 62 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-paths/) |

## Problem Description
### Goal
Imagine a robot at the top-left cell of an $m \times n$ rectangular grid. Its destination is the bottom-right cell, and each move advances exactly one cell either to the right or downward; it cannot move left, upward, or outside the grid.

Return the number of unique paths that reach the destination. Paths are distinguished by their ordered choices of right and down moves. When the grid has one row or one column, only one path exists because every move is forced.

### Function Contract
**Inputs**

- `m`: the positive number of rows
- `n`: the positive number of columns

**Return value**

The integer number of valid movement sequences.

### Examples
**Example 1**

- Input: `m = 3, n = 7`
- Output: `28`

**Example 2**

- Input: `m = 3, n = 2`
- Output: `3`

**Example 3**

- Input: `m = 1, n = 8`
- Output: `1`

### Required Complexity

- **Time:** $O(\min(m,n))$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A path is completely determined by the positions of one move type**

Every path contains exactly $m - 1$ downward moves and $n - 1$ rightward moves, in some order. Once the positions of all downward moves are chosen, every remaining position must be a right move, so the movement sequence is determined. The answer is a binomial coefficient over $m + n - 2$ total positions.

**Choose the smaller move group to minimize arithmetic steps**

Let $N=m+n-2$ be the total number of moves. Use symmetry $\binom{N}{r} = \binom{N}{N-r}$ and let $r = \min(m - 1, n - 1)$. Compute the coefficient incrementally rather than constructing two factorials. At step `i`, multiply by `total - r + i` and divide by `i`.

The chosen recurrence yields an integer after every complete step, so arbitrary-precision implementations remain exact. Fixed-width implementations should use a sufficiently wide intermediate type or divide common factors safely before multiplication.

**Every intermediate value is a smaller binomial coefficient**

After iteration $i$, the running result equals $\binom{N-r+i}{i}$. Multiplying by `total - r + i` and dividing by `i` applies the standard neighboring-binomial recurrence, preserving integrality.

**Trace a rectangular grid**

For a 3-by-7 grid there are 8 moves, including 2 downward moves. Choosing their positions gives $\binom{8}{2} = 8 \cdot 7 / 2 = 28$ paths.

**Paths are in bijection with move-position choices**

Every valid route contains exactly $m - 1$ downward moves and $n - 1$ rightward moves. Recording which positions in the complete move sequence are downward uniquely determines every remaining position as rightward, so it reconstructs one path.

Conversely, any choice of that many positions yields a legal monotone route ending at the destination. The mapping is one-to-one, making the path count the corresponding binomial coefficient; the incremental product evaluates that coefficient exactly.

#### Complexity detail

The loop uses the smaller of the two move counts, taking $O(\min(m,n))$ arithmetic steps and $O(1)$ auxiliary variables.

#### Alternatives and edge cases

- **Grid dynamic programming:** is straightforward and takes $O(mn)$ time, reducible to $O(\min(m,n))$ storage.
- **Unmemoized recursion:** follows the movement definition directly but recomputes overlapping states exponentially.
- **Factorials:** express the formula compactly but create larger intermediate values and may overflow fixed-width types sooner.
- If either dimension is one, $r = 0$, the loop performs no work, and the single straight path is returned.
- This combinatorial shortcut depends on every cell being available. Obstacles destroy the equal move-order counting and require dynamic programming as in problem 63.

</details>
