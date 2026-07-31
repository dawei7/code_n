# Minimum Operations to Make Elements Within K Subarrays Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3505 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/) |

## Problem Description

### Goal

You may repeatedly increase or decrease any single element of `nums` by $1$. Choose at least $k$ pairwise non-overlapping subarrays, each containing exactly $x$ consecutive elements, and make all values inside every chosen subarray equal. Different chosen subarrays do not need to share the same final value.

Return the smallest total number of unit changes needed. The subarrays are selected as part of the optimization: they may be adjacent, but their index ranges cannot intersect. Elements outside the selected ranges may remain unchanged, and performing no operation on an already uniform selected range is allowed.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers.
- `x`: The exact length required for every selected subarray.
- `k`: The minimum number of pairwise non-overlapping qualifying subarrays.

The constraints are $2 \le n \le 10^5$, $-10^6 \le \texttt{nums[i]} \le 10^6$, $2 \le x \le n$, $1 \le k \le 15$, and $2 \le kx \le n$.

**Return value**

Return the minimum total number of increment or decrement operations that makes at least $k$ selected length-$x$ subarrays internally constant.

### Examples

**Example 1**

- Input: `nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2`
- Output: `8`
- Explanation: Indices $1$ through $3$ can become all $1$ at cost $5$, and indices $5$ through $7$ can become all $4$ at cost $3$.

**Example 2**

- Input: `nums = [9,-2,-2,-2,1,5], x = 2, k = 2`
- Output: `3`
- Explanation: The pair at indices $1$ and $2$ already matches. Changing the value at index $4$ from $1$ to $-2$ makes indices $3$ and $4$ a second disjoint equal pair.
