# Number of Distinct Binary Strings After Applying Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2450 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Distinct Binary Strings After Applying Operations](https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/) |

## Problem Description

### Goal

You are given a binary string `s` and a positive integer `k`. An operation chooses any contiguous substring of length exactly `k` and flips every character in that substring: each `0` becomes `1`, and each `1` becomes `0`.

You may apply the operation any number of times, including zero, and may reuse the same substring. Count how many distinct strings can be obtained from `s`. Because this count can be large, return it modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: A string of length $n$ containing only `0` and `1`, where $1 \le n \le 10^5$.
- `k`: The exact length of every flipped substring, where $1 \le k \le n$.

**Return value**

- The number of distinct reachable binary strings, modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "1001", k = 3`
- Output: `4`
- Explanation: There are two eligible windows, and independently choosing either, both, or neither produces four strings.

**Example 2**

- Input: `s = "10110", k = 5`
- Output: `2`
- Explanation: The only eligible window is the entire string, so either it is flipped or it is not.
