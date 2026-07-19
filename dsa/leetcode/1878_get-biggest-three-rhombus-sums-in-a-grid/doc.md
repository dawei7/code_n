# Get Biggest Three Rhombus Sums in a Grid

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/) |
| Frontend ID | 1878 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given an $M\times N$ integer matrix `grid`, consider rhombi whose four corners are centered on cells and whose sides follow the two grid diagonals. Such a shape is a square rotated by $45^\circ$. Its rhombus sum includes only cells on the border, not cells strictly inside it.

A rhombus may also have zero area: a single cell then forms both the entire shape and its border. Compute every valid border sum, discard duplicate numerical sums, and return the largest three distinct values in descending order. If the grid produces fewer than three distinct sums, return all that exist.

### Function Contract

**Inputs**

- `grid`: a rectangular $M\times N$ matrix, where $1 \le M,N \le 50$ and $1 \le \texttt{grid[r][c]} \le 10^5$.

**Return value**

- Return up to three distinct rhombus border sums, ordered from largest to smallest.

### Examples

**Example 1**

- Input: `grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]`
- Output: `[228,216,211]`

The three answers come from different valid borders; interior cells do not contribute.

**Example 2**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[20,9,8]`

The nonzero rhombus has border sum $2+4+6+8=20$, followed by two zero-area rhombi.

**Example 3**

- Input: `grid = [[7,7,7]]`
- Output: `[7]`

Only zero-area rhombi fit, and their equal sums count once.

### Required Complexity

- **Time:** $O(MN\min(M,N))$
- **Space:** $O(MN)$

<details>
<summary>Approach</summary>

#### General

**Represent each rhombus by a center and radius**

For a positive radius $K$, a center cell $(r,c)$ determines corners at $(r-K,c)$, $(r,c+K)$, $(r+K,c)$, and $(r,c-K)$. The shape fits exactly when all four coordinates stay inside the matrix. Radius zero is handled separately by recording the center cell itself.

**Precompute both diagonal directions**

Build one prefix table along down-right diagonals and another along down-left diagonals. A subtraction within either table gives the sum of any contiguous diagonal edge in constant time. Combining four such edge queries yields a border sum. The chosen half-open edge ranges must count each of the four corners once: in the implemented formula the bottom corner is initially counted twice and the top corner omitted, so subtracting the former and adding the latter restores the exact border.

**Enumerate every valid border**

Visit every possible center and every radius through the largest one that fits around it. This describes every positive-area rhombus uniquely, while adding each cell covers every zero-area rhombus. Therefore every legal sum is considered and no nonzero shape is generated from two different centers and radii.

**Keep only the largest distinct sums**

Maintain a set containing at most three values. After inserting a new sum, remove the minimum if the set grows past three. At every point the set is exactly the three largest distinct sums seen so far, or all of them when fewer than three exist. Sorting this constant-size set in reverse order produces the required result.

#### Complexity detail

Let $K=\min(M,N)$. Constructing the two diagonal prefix tables takes $O(MN)$ time and space. Across all centers there are at most $O(MNK)$ valid radii, and each border sum plus top-three update costs $O(1)$. The total time is therefore $O(MNK)$, which is $O(MN\min(M,N))$, and the prefix tables require $O(MN)$ space.

#### Alternatives and edge cases

- **Walk every border cell:** It is straightforward and useful as an oracle, but spending $O(K)$ time per rhombus raises the total to $O(MNK^2)$ on square grids.
- **Store and sort every sum:** This is correct but uses space proportional to the number of rhombi and performs unnecessary sorting when only three values are needed.
- **Heap of three values:** A min-heap plus a membership set also maintains the top three distinct sums, with slightly more bookkeeping.
- **One row or one column:** No positive-area rhombus fits, so only distinct cell values can appear.
- **Zero-area shapes:** A single cell is a valid rhombus sum and must not be omitted.
- **Corner accounting:** Summing four closed diagonal edges counts every corner twice; use half-open edges or explicitly correct the duplicates.
- **Repeated sums:** Distinctness concerns numerical sums, not shapes; many different borders may contribute the same value only once.
- **Fewer than three values:** Return the available distinct sums without padding.

</details>
