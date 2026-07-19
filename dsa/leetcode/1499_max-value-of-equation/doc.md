# Max Value of Equation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1499 |
| Difficulty | Hard |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/max-value-of-equation/) |

## Problem Description
### Goal

The array `points` describes points on a two-dimensional plane. Each entry is `[x_i, y_i]`, and the points are already ordered so their $x$-coordinates are strictly increasing.

Choose two distinct points with indices $i<j$ whose horizontal distance satisfies $lvert x_i-x_j\rvert \le k$. Among all such pairs, maximize

$$
y_i+y_j+lvert x_i-x_j\rvert.
$$

At least one pair is guaranteed to satisfy the distance restriction. Return the largest equation value, which may be negative.

### Function Contract
**Inputs**

Let $N$ be the number of points.

- `points`: a list of $N$ coordinate pairs with $2 \le N \le 10^5$.
- Every point has the form `[x_i, y_i]`, where $-10^8 \le x_i,y_i \le 10^8$.
- The $x$-coordinates are strictly increasing: $x_i < x_j$ whenever $i<j$.
- `k`: an integer with $0 \le \texttt{k} \le 2\cdot10^8$.
- At least one index pair satisfies the horizontal-distance limit.

**Return value**

Return the maximum value of $y_i+y_j+lvert x_i-x_j\rvert$ over all valid pairs $i<j$.

### Examples
**Example 1**

- Input: `points = [[1,3],[2,0],[5,10],[6,-10]], k = 1`
- Output: `4`
- Explanation: The valid pairs produce $3+0+1=4$ and $10-10+1=1$; the larger value is $4$.

**Example 2**

- Input: `points = [[0,0],[3,0],[9,2]], k = 3`
- Output: `3`
- Explanation: Only the first two points satisfy the distance limit, and their equation value is $3$.

**Example 3**

- Input: `points = [[1,1],[2,2],[3,3]], k = 2`
- Output: `6`
- Explanation: The first and third points give $1+3+2=6$.
