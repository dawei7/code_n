# Count Submatrices With All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1504 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Matrix, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/count-submatrices-with-all-ones/) |

## Problem Description
### Goal

Given an $m\times n$ binary matrix `mat`, consider every nonempty rectangular submatrix formed by choosing a contiguous range of rows and a contiguous range of columns. Different boundary choices count as different submatrices, even when they contain identical values.

Return the total number of those rectangles whose every cell is `1`. Rectangles of every legal height and width must be included, from individual cells through the entire matrix; any rectangle containing at least one `0` does not contribute.

### Function Contract
**Inputs**

Let $m$ be the row count and $n$ the column count.

- `mat`: a rectangular $m\times n$ matrix with $1\le m,n\le150$.
- Every `mat[row][column]` is either `0` or `1`.

**Return value**

Return an integer equal to the number of nonempty, axis-aligned, contiguous submatrices containing only ones. The app-local implementation does not modify `mat`.

### Examples
**Example 1**

- Input: `mat = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `13`
- Explanation: The total consists of six $1\times1$, two $1\times2$, three $2\times1$, one $2\times2$, and one $3\times1$ all-one rectangles.

**Example 2**

- Input: `mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]`
- Output: `24`
- Explanation: Counting all valid shapes gives eight single cells plus sixteen wider or taller rectangles.

**Example 3**

- Input: `mat = [[1,1,1],[1,1,1]]`
- Output: `18`
- Explanation: An all-one $2\times3$ matrix has $2\cdot3/2=3$ row intervals and $3\cdot4/2=6$ column intervals, producing $3\cdot6=18$ rectangles.

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Convert each row into histogram heights**

Maintain `heights[column]`, the number of consecutive ones ending at the current row in that column. Reading a `1` increments the previous height; reading a `0` resets it to zero.

Fixing the current row as a rectangle's bottom boundary reduces the problem to a histogram. For any contiguous column interval, the minimum height in that interval is exactly the number of possible top boundaries that produce an all-one rectangle with that bottom and horizontal span. Thus the row's contribution is the sum of interval minima over all column intervals.

**Count intervals by their right endpoint**

Process histogram columns from left to right and maintain `ending_here`: the sum of minimum heights over every interval ending at the current column. Adding `ending_here` to the answer counts every all-one rectangle whose bottom-right cell is at the current matrix position exactly once.

A nondecreasing monotonic stack stores pairs `(height, width)`. The `width` is the number of consecutive interval starts currently grouped under that minimum height. When a new height $h$ is no larger than the top height, all those intervals now have minimum $h$. Pop each group, subtract its old `height * width` contribution from `ending_here`, and merge its width into the new group. Then push `(h, merged_width)` and add `h * merged_width`.

Intervals represented by lower stack entries keep their old minimum. Intervals represented by popped entries and the one-cell interval ending at the new column receive the new minimum $h$. Therefore the updated `ending_here` is precisely the sum of minima for all intervals with this right endpoint.

**Why the accumulated total is exact**

Every all-one submatrix has one unique bottom row and rightmost column. At that matrix position, its horizontal interval appears among the histogram intervals ending there, and each allowable top boundary is one unit of that interval's minimum height. It is therefore included once in `ending_here` and then once in the global answer.

Conversely, each unit counted by an interval minimum selects a top row no higher than every column's consecutive-one height. All cells inside the resulting rectangle are ones, so no invalid submatrix is counted. The one-to-one correspondence proves the final total.

#### Complexity detail

Each of the $mn$ cells updates one height. Within a row, every column's stack entry is pushed once and popped at most once, so all stack work is $O(n)$ per row and $O(mn)$ overall.

The height array and monotonic stack each contain at most $n$ entries, giving $O(n)$ auxiliary space. The matrix remains unchanged.

#### Alternatives and edge cases

- **Scan left from every histogram column:** Maintain the minimum height while extending each right endpoint leftward. It is straightforward and correct but costs $O(mn^2)$ time on dense rows.
- **Enumerate row pairs:** Intersect the usable columns for every top/bottom pair and count consecutive-one runs. This takes $O(m^2n)$ time and may be preferable only when one dimension is very small.
- **Enumerate all four boundaries:** Checking every candidate rectangle directly is far more expensive and repeats cell work extensively.
- **All-zero matrix:** Every histogram height and row contribution is zero, so the result is zero.
- **All-one matrix:** Every row interval can pair with every column interval, giving $m(m+1)n(n+1)/4$.
- **Single row:** The task reduces to counting all-one subarrays; a run of length $r$ contributes $r(r+1)/2$.
- **Single column:** A vertical run follows the same triangular-number rule.
- **Zero inside a row:** Its height becomes zero and the stack merges all intervals ending there under minimum zero, preventing rectangles from crossing it.
- **Equal adjacent heights:** Popping on `>=` merges their start groups; this changes representation but not the sum of interval minima.
- **Large answer:** The number of rectangles can exceed the cell count substantially, so accumulate in an integer type capable of the full constraint result.

</details>
