# Find Indices With Index and Value Difference I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2903 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and two non-negative integers, `indexDifference` and `valueDifference`.

Find two indices $i$ and $j$ such that both

$$
\lvert i-j\rvert\ge\texttt{indexDifference}
$$

and

$$
\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert\ge\texttt{valueDifference}.
$$

Return `[i, j]` for any pair satisfying both conditions, or `[-1, -1]` if no such pair exists. The two indices are allowed to be equal when the requested differences permit it.

### Function Contract

**Inputs**

- `nums`: A nonempty array of integers from $0$ through $50$.
- `indexDifference`: The minimum allowed absolute gap between the indices.
- `valueDifference`: The minimum allowed absolute gap between their values.

The shared bounds are $1\le n\le100$, $0\le\texttt{indexDifference}\le100$, and $0\le\texttt{valueDifference}\le50$.

**Return value**

Return any qualifying pair `[i, j]`; return `[-1, -1]` only when no qualifying pair exists.

### Examples

#### Example 1

- **Input:** `nums = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4`
- **Output:** `[0, 3]`
- **Explanation:** The index gap is $3$ and the value gap is $4$.

#### Example 2

- **Input:** `nums = [2, 1], indexDifference = 0, valueDifference = 0`
- **Output:** `[0, 0]`
- **Explanation:** Equal indices are permitted, and both required gaps are zero.

#### Example 3

- **Input:** `nums = [1, 2, 3], indexDifference = 2, valueDifference = 4`
- **Output:** `[-1, -1]`
- **Explanation:** The only index pair far enough apart has a value gap of $2$, so no answer exists.
