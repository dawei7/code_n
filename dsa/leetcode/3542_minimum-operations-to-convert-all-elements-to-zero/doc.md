# Minimum Operations to Convert All Elements to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3542 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/) |

## Problem Description

### Goal

You are given an array of non-negative integers and may perform any number of operations. In one operation, choose a nonempty contiguous subarray and find its minimum non-negative value. Every occurrence of that minimum within the chosen subarray is then replaced by `0`; the other values remain unchanged.

Selecting a range whose minimum is already `0` cannot change the array, so a useful operation acts inside a positive segment. Determine the fewest operations needed to make every array element zero.

### Function Contract

**Inputs**

- `nums`: A list of non-negative integers.

Let $n$ be the length of `nums`. The constraints are $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.

**Return value**

Return the minimum number of allowed subarray operations required to turn every element into `0`.

### Examples

**Example 1**

- Input: `nums = [0, 2]`
- Output: `1`
- Explanation: Choosing the one-element subarray containing `2` changes it to `0`.

**Example 2**

- Input: `nums = [3, 1, 2, 1]`
- Output: `3`
- Explanation: One operation removes both occurrences of `1`; the remaining isolated values `3` and `2` each require one operation.

**Example 3**

- Input: `nums = [1, 2, 1, 2, 1, 2]`
- Output: `4`
- Explanation: The three `1` values can be removed together. They then separate the three `2` values, which require one operation each.

---
