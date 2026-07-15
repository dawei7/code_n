# Score After Flipping Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 861 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/score-after-flipping-matrix/) |

## Problem Description
### Goal
You are given an $m \times n$ binary matrix `grid`. One move chooses an entire row or an entire column and toggles every value in it, changing each `0` to `1` and each `1` to `0`. Any number of moves may be made, including none.

Interpret every row from left to right as an $n$-bit binary number. The matrix score is the sum of those $m$ row values. Determine the greatest score obtainable by choosing a suitable sequence of row and column moves, and return that maximum integer.

### Function Contract
**Inputs**

- `grid`: a rectangular $m \times n$ matrix containing only `0` and `1`, where $1 \leq m,n \leq 20$.

The leftmost entry of each row is its most significant bit, with weight $2^{n-1}$; column $j$ has weight $2^{n-1-j}$.

**Return value**

Return the maximum possible sum of the binary values represented by all rows after any number of row and column toggles.

### Examples
**Example 1**

- Input: `grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]`
- Output: `39`

One optimum has rows `1111`, `1001`, and `1111`, worth $15+9+15=39$.

**Example 2**

- Input: `grid = [[0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1],[0,0]]`
- Output: `6`

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Force every most-significant bit to one**

The leftmost bit of a row is worth $2^{n-1}$, while all remaining positions together are worth only $2^{n-1}-1$. Therefore no arrangement with a leading `0` can be optimal for that row: toggling the row makes its leading bit `1`, and even losing every lower bit would still increase its value. Logically toggle exactly those rows whose first entry is `0`.

The matrix need not be mutated. After this logical row choice, the effective bit at `(row, column)` equals `grid[row][column]` when `grid[row][0] == 1`, and its complement otherwise.

**Optimize each column independently**

Once the row choices are fixed, toggling a column does not affect any other column. If a column currently has $k$ effective ones, leaving it contributes $k$ copies of its positional weight, while toggling it contributes $m-k$ copies. Its maximum contribution is therefore

$$
\max(k,m-k)\,2^{n-1-j}.
$$

Sum this quantity over all columns. The row step is necessary in every optimum because of the dominant leading bit, and the column decisions then attain the largest possible contribution independently at every remaining position. Together they produce a globally maximum score.

#### Complexity detail

Counting effective ones visits each of the $mn$ entries once, so time is $O(mn)$. The dimensions, score, per-column count, and loop indices use a fixed number of integers; because the input is only read, auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Materialize every flip:** Toggling rows and columns in place can still run in $O(mn)$, but it modifies the caller's matrix and is unnecessary for computing the score.
- **Enumerate row or column subsets:** Testing all flip masks is correct, but it requires exponential time even though each column's best choice is independent after the leading bits are fixed.
- **Greedily maximize raw ones before fixing rows:** Columns cannot be judged from their original counts because the mandatory row toggles may complement selected entries.
- **Single cell:** A lone `0` can be toggled to `1`, so the maximum is `1`.
- **Single column:** Every row can make its only bit `1`, giving score $m$.
- **Tied column counts:** Either column orientation contributes the same amount when exactly half the effective bits are `1`.
- **Already optimal grid:** Zero moves are allowed, and the contribution calculation leaves every beneficial orientation unchanged.

</details>
