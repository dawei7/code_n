# Minimum Array Changes to Make Differences Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3224 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/) |

## Problem Description

### Goal

You are given an even-length integer array `nums` and an integer `k`. One change may replace any array element with any integer in the inclusive range $[0,k]$.

Choose changes so that there is one integer $X$ for which every mirrored pair has the same absolute difference: for each index $i$ in the first half, $lvert\texttt{nums[i]}-\texttt{nums[n-1-i]}\rvert=X$. Return the minimum number of changed elements. Making no changes is allowed, and the common target $X$ may be any value from $0$ through $k$.

### Function Contract

**Inputs**

- `nums`: An even-length list with $2 \leq n=\lvert\texttt{nums}\rvert \leq 10^5$ and $0 \leq \texttt{nums[i]} \leq k$.
- `k`: The largest permitted replacement value, with $0 \leq k \leq 10^5$.

**Return value**

Return the minimum number of individual array elements that must be replaced.

### Examples

**Example 1**

- Input: `nums = [1, 0, 1, 2, 4, 3], k = 4`
- Output: `2`
- Explanation: Two replacements can make every mirrored difference equal to `2`.

**Example 2**

- Input: `nums = [0, 1, 2, 3, 3, 6, 5, 4], k = 6`
- Output: `2`
- Explanation: A common difference of `4` is attainable with two changes.

**Example 3**

- Input: `nums = [1, 2, 2, 1], k = 2`
- Output: `0`
- Explanation: Both mirrored pairs already have difference `0`.
