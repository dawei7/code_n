# Minimum Number of Operations to Make String Sorted

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/) |
| Frontend ID | 1830 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Combinatorics, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Starting with a 0-indexed lowercase string `s`, repeatedly perform a prescribed operation until the characters are sorted in ascending order. First find the largest index $i$ with $1 \le i < \lvert s\rvert$ for which `s[i] < s[i - 1]`.

Next choose the largest $j \ge i$ such that every character from index $i$ through $j$ is smaller than `s[i - 1]`. Swap `s[i - 1]` with `s[j]`, then reverse the suffix beginning at $i$. Return how many operations are performed, modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \le n \le 3000$.

**Return value**

- Return the number of prescribed operations required to reach the ascending arrangement, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "cba"`
- Output: `5`

The operation visits the five preceding permutations before reaching `"abc"`.

**Example 2**

- Input: `s = "aabaa"`
- Output: `2`

The successive strings are `"aaaba"` and then `"aaaab"`.

**Example 3**

- Input: `s = "abc"`
- Output: `0`

The string is already sorted, so no operation is needed.
