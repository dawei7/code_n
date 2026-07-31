# Maximum Frequency Score of a Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2524 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Stack, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. For any array, its frequency score is formed by considering each distinct value $x$, raising $x$ to the number of times it occurs, summing those terms, and reducing the sum modulo $10^9 + 7$. For example, `[5, 4, 5, 7, 4, 4]` has score $(5^2 + 4^3 + 7^1) \bmod (10^9 + 7) = 96$.

Consider every contiguous subarray of `nums` whose length is exactly `k`. Return the largest of their frequency scores. The comparison is between the values after applying the modulus; the unreduced mathematical sums are not what must be maximized.

### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The required subarray length.

Let $n = \lvert\texttt{nums}\rvert$. The inputs satisfy $1 \le k \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return the maximum frequency score, modulo $10^9 + 7$, among all length-`k` subarrays.

### Examples

**Example 1**

- Input: `nums = [1, 1, 1, 2, 1, 2], k = 3`
- Output: `5`
- Explanation: The window `[2, 1, 2]` contributes $2^2 + 1^1 = 5$, which is the maximum score.

**Example 2**

- Input: `nums = [1, 1, 1, 1, 1, 1], k = 4`
- Output: `1`
- Explanation: Every length-four window contains only `1`, so each score is $1^4 = 1$.
