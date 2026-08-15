# Beautiful Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2613 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Divide and Conquer, Geometry, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-pairs/) |

## Problem Description

### Goal

Two 0-indexed integer arrays, `nums1` and `nums2`, have the same length. Treat every index $i$ as the point whose coordinates are `(nums1[i], nums2[i])`.

For a pair of indices $(i,j)$ with $i<j$, its Manhattan distance is

$$
\lvert \texttt{nums1}[i]-\texttt{nums1}[j] \rvert
+
\lvert \texttt{nums2}[i]-\texttt{nums2}[j] \rvert.
$$

A pair is beautiful when this value is the minimum among all possible index pairs. Return a beautiful pair. If several pairs attain the same minimum distance, choose the lexicographically smallest one: prefer the smaller first index, and when those are equal, prefer the smaller second index.

### Function Contract

**Inputs**

Let $n$ be the common length of the two arrays.

- `nums1`: The first coordinates of the points, where $2 \leq n \leq 10^5$ and $0 \leq \texttt{nums1}[i] \leq n$.
- `nums2`: The second coordinates of the points, with length $n$ and $0 \leq \texttt{nums2}[i] \leq n$.

**Return value**

Return `[i, j]`, where $i<j$ and the corresponding points have minimum Manhattan distance. Among all pairs with that distance, return the lexicographically smallest pair.

### Examples

#### Example 1

- **Input:** `nums1 = [1, 2, 3, 2, 4], nums2 = [2, 3, 1, 2, 3]`
- **Output:** `[0, 3]`
- **Explanation:** Points $0$ and $3$ have Manhattan distance $1$, the smallest attainable distance.

#### Example 2

- **Input:** `nums1 = [1, 2, 4, 3, 2, 5], nums2 = [1, 4, 2, 3, 5, 1]`
- **Output:** `[1, 4]`
- **Explanation:** Points $1$ and $4$ have Manhattan distance $1$.

#### Example 3

- **Input:** `nums1 = [0, 0, 0], nums2 = [1, 1, 1]`
- **Output:** `[0, 1]`
- **Explanation:** Every pair has distance zero, so lexicographic order selects `[0, 1]`.
