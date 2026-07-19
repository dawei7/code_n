# K Closest Points to Origin

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 973 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/k-closest-points-to-origin/) |

## Problem Description

### Goal

An array `points` describes points on the X-Y plane, where `points[i] = [x_i, y_i]`, and an integer `k` specifies how many points to choose. Return the `k` points that are closest to the origin `[0, 0]`.

Closeness is measured by Euclidean distance. For a point $(x_i,y_i)$, that distance is $\sqrt{x_i^2+y_i^2}$. The answer may list the selected points in any order. The selected set is guaranteed to be unique, although its ordering is not.

### Function Contract

**Inputs**

- `points`: a list of $N$ integer coordinate pairs `[x_i, y_i]`, with $1 \le N \le 10^4$ and $-10^4 \le x_i,y_i \le 10^4$.
- `k`: the number of points to return, where $1 \le K = \texttt{k} \le N$.

For comparison, define the squared distance

$$
d_i = x_i^2 + y_i^2.
$$

Because the square-root function is increasing on nonnegative values, ordering points by $d_i$ gives the same order as their Euclidean distances.

**Return value**

- A list containing exactly the $K$ closest points. Their order does not matter.

### Examples

**Example 1**

- Input: `points = [[1, 3], [-2, 2]], k = 1`
- Output: `[[-2, 2]]`
- Explanation: the squared distances are $10$ and $8$, so `[-2, 2]` is closer.

**Example 2**

- Input: `points = [[3, 3], [5, -1], [-2, 4]], k = 2`
- Output: `[[3, 3], [-2, 4]]`
- Explanation: `[[-2, 4], [3, 3]]` is equally valid because answer order is unrestricted.
