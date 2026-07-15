# Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1284 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix. In one step, choose a cell and flip its value: zero becomes one and one becomes zero. The same step also flips every existing orthogonal neighbor of the chosen cell—those directly above, below, left, or right. Diagonal cells are not neighbors, and cells beyond a matrix boundary are ignored.

Find the minimum number of steps that converts the entire matrix to a zero matrix. If no sequence of allowed flips can make every cell zero, return `-1`.

### Function Contract
**Inputs**

- `mat`: an $m \times n$ matrix containing only zeroes and ones, where $1 \le m,n \le 3$.
- Let $k = mn$ be the number of cells.

**Return value**

The fewest cell-flip steps needed to reach the all-zero matrix, or `-1` when the zero matrix is unreachable.

### Examples
**Example 1**

- Input: `mat = [[0,0],[0,1]]`
- Output: `3`

**Example 2**

- Input: `mat = [[0]]`
- Output: `0`
- Explanation: No step is needed because the input is already a zero matrix.

**Example 3**

- Input: `mat = [[1,0,0],[1,0,0]]`
- Output: `-1`
- Explanation: No combination of legal flips reaches the zero matrix.

### Required Complexity
- **Time:** $O(k2^k)$
- **Space:** $O(2^k)$

<details>
<summary>Approach</summary>

#### General

**Encode matrices as graph states.** Number the $k$ cells and store a matrix as a $k$-bit integer, with a set bit representing a one. Precompute one bit mask per cell containing that cell and all of its valid orthogonal neighbors. Applying a move is then an exclusive-or with the corresponding mask, which toggles exactly the required cells.

**Breadth-first search gives the minimum.** Treat every encoded matrix as a graph vertex and every legal flip as an unweighted edge. Begin at the input mask. Breadth-first search visits states in nondecreasing numbers of moves, so the first time it generates mask zero, that path uses the minimum possible number of flips. A visited set prevents cycles caused by undoing or recombining flips. If the queue empties without reaching zero, every reachable state has been examined and the required answer is `-1`.

#### Complexity detail

There are at most $2^k$ binary matrix states. Expanding one state tries all $k$ cell flips, and each transition is a constant-time bitwise operation, so the worst-case time is $O(k2^k)$. The queue and visited set can hold $O(2^k)$ masks. Because $m,n \le 3$, $k \le 9$; this domain is too small for honest runtime scaling, so exhaustive regression replaces a measured verdict.

#### Alternatives and edge cases

- **Enumerate flip subsets:** Because applying a flip twice cancels it and flip order is irrelevant, all $2^k$ subsets can be tested; this also takes $O(k2^k)$ time but does not naturally discover answers layer by layer.
- **Matrix copies in BFS:** Storing full matrices is correct but makes transitions and state hashing more expensive than bit masks.
- **Already zero:** The start state must return zero before any move is generated.
- **Unreachable state:** Not every board shape makes every binary configuration reachable; exhausting the queue must return `-1`.
- **Corners and edges:** Their flip masks contain fewer than five cells because nonexistent neighbors are ignored.

</details>
