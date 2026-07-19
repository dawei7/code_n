# Permutation Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 60 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutation-sequence/) |

## Problem Description
### Goal
The set of distinct digits from `1` through `n`, where $1 \le n \le 9$, contains $n!$ unique permutations. Arrange those permutations in lexicographic order. The rank `k` is one-based: $k = 1$ names the increasing permutation, and $k = n!$ names the final one.

Return the digits of the permutation at rank `k` as a string. Each digit must appear exactly once. Determine the ranked arrangement directly from the ordering structure rather than generating and storing every preceding permutation.

### Function Contract
**Inputs**

- `n`: the number of distinct digits, with $1 \le n \le 9$
- `k`: a one-based rank satisfying $1 \le k \le n!$

**Return value**

The ranked permutation as a string.

### Examples
**Example 1**

- Input: `n = 3, k = 3`
- Output: `"213"`

**Example 2**

- Input: `n = 4, k = 9`
- Output: `"2314"`

**Example 3**

- Input: `n = 3, k = 1`
- Output: `"123"`
