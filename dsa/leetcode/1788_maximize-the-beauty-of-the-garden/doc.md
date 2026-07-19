# Maximize the Beauty of the Garden

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximize-the-beauty-of-the-garden/) |
| Frontend ID | 1788 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A garden contains `n` flowers arranged in a line. The integer `flowers[i]` is the beauty of the flower at index `i`.

You may remove any number of flowers, including none, while preserving the relative order of those that remain. The resulting garden is valid only if it contains at least two flowers and its first and last flowers have equal beauty values. The garden's total beauty is the sum of all retained values.

Return the maximum total beauty obtainable from any valid remaining garden. The input guarantees that at least one valid garden can be formed.

### Function Contract

**Input**

- `flowers`: an array of length $n$, where $2 \le n \le 10^5$ and $-10^4 \le \texttt{flowers[i]} \le 10^4$.
- At least one beauty value occurs at least twice, so valid equal endpoints exist.

Let $U$ be the number of distinct beauty values.

**Return value**

- Return the maximum sum of a subsequence with at least two elements whose first and last values are equal.

### Examples

**Example 1**

- Input: `flowers = [1,2,3,1,2]`
- Output: `8`

Keeping `[2,3,1,2]` gives equal endpoints and total beauty `8`.

**Example 2**

- Input: `flowers = [100,1,1,-3,1]`
- Output: `3`

Remove `100` and `-3`, leaving `[1,1,1]`.

**Example 3**

- Input: `flowers = [-1,-2,0,-1]`
- Output: `-2`

The best valid garden is `[-1,-1]`; the interior nonpositive flowers are removed.
