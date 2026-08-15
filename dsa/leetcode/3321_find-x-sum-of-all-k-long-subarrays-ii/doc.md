# Find X-Sum of All K-Long Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3321 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/) |

## Problem Description

### Goal

For an integer array, define its x-sum by counting every distinct value, ranking values by decreasing frequency, and retaining every occurrence of the first `x` ranked values. When two values have equal frequencies, the bigger value ranks first. The x-sum is the sum of all retained occurrences. If fewer than `x` distinct values exist, nothing is discarded and the x-sum is the ordinary array sum.

Given `nums` and integers `k` and `x`, examine every contiguous subarray `nums[i..i + k - 1]`. Return an array of length $n-k+1$ whose entry at index $i$ is that window's x-sum. Frequencies and rankings are recomputed for the contents of each window; an occurrence contributes only when its value belongs to the selected top group.

### Function Contract

**Inputs**

- `nums`: The integer array whose length is $n$, where $1\leq n\leq10^5$ and $1\leq\texttt{nums[i]}\leq10^9$.
- `k`: The fixed subarray length.
- `x`: The number of distinct values retained after ranking.

The parameters satisfy $1\leq x\leq k\leq n$.

**Return value**

Return the $n-k+1$ x-sums in left-to-right window order.

### Examples

#### Example 1

- **Input:** `nums = [1, 1, 2, 2, 3, 4, 2, 3], k = 6, x = 2`
- **Output:** `[6, 10, 12]`
- **Explanation:** The first window keeps values 2 and 1. In the second window, value 2 ranks first and value 4 wins the frequency-one tie; the final window keeps values 2 and 3.

#### Example 2

- **Input:** `nums = [3, 8, 7, 8, 7, 5], k = 2, x = 2`
- **Output:** `[11, 15, 15, 15, 12]`
- **Explanation:** Since `k == x`, every distinct value in every length-two window is retained, so each result is the ordinary window sum.
