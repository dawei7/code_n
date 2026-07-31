# Find Indices With Index and Value Difference II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2905 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/) |

## Problem Description
### Goal
Given a 0-indexed integer array `nums` and the non-negative integers `indexDifference` and `valueDifference`, find two in-range indices `i` and `j` such that both

$$
\lvert i-j\rvert\ge \texttt{indexDifference}
$$

and

$$
\lvert \texttt{nums}[i]-\texttt{nums}[j]\rvert\ge \texttt{valueDifference}.
$$

The two indices may be equal. Return any pair satisfying both inequalities. If no such pair exists, return `[-1, -1]`.

### Function Contract
**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le 10^5$ and every value lies from $0$ through $10^9$.
- `indexDifference`: The minimum required absolute index difference, from $0$ through $10^5$.
- `valueDifference`: The minimum required absolute value difference, from $0$ through $10^9$.

**Return value**

Return any valid pair `[i, j]`. Return `[-1, -1]` exactly when no valid pair exists.

### Examples
**Example 1**

- Input: `nums = [5, 1, 4, 1], indexDifference = 2, valueDifference = 4`
- Output: `[0, 3]`
- Explanation: The index difference is $3$ and the value difference is $4$.

**Example 2**

- Input: `nums = [2, 1], indexDifference = 0, valueDifference = 0`
- Output: `[0, 0]`
- Explanation: Because both required differences are zero, the same index is valid.

**Example 3**

- Input: `nums = [1, 2, 3], indexDifference = 2, valueDifference = 4`
- Output: `[-1, -1]`
- Explanation: The only pair far enough apart has value difference $2$, so no pair satisfies both requirements.
