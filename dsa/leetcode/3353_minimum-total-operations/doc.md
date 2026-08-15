# Minimum Total Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3353 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-total-operations/) |

## Problem Description

### Goal

You are given an integer array `nums`. In one operation, select any nonempty prefix: a contiguous portion that begins at index $0$ and ends at any chosen position. Then choose an arbitrary integer `k`, which may be positive, zero, or negative, and add it to every element of that prefix.

You may perform as many such operations as necessary. Determine the minimum number of operations needed to make every element of the array equal. A single operation uses one common adjustment for its entire chosen prefix; it cannot change different positions by different amounts.

### Function Contract

**Inputs**

- `nums`: The integer array whose elements must be made equal.

Let $n=\lvert\texttt{nums}\rvert$. The source guarantees $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the minimum number of prefix-addition operations required to make all elements equal.

### Examples

#### Example 1

- **Input:** `nums = [1, 4, 2]`
- **Output:** `2`
- **Explanation:** Add $-2$ to the first two elements, producing `[-1, 2, 2]`, and then add $3$ to the first element.

#### Example 2

- **Input:** `nums = [10, 10, 10]`
- **Output:** `0`
- **Explanation:** The array is already constant, so no operation is needed.
