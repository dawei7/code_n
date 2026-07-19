# Array of Doubled Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 954 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [array-of-doubled-pairs](https://leetcode.com/problems/array-of-doubled-pairs/) |

## Problem Description

### Goal

Given an even-length integer array `arr`, decide whether its elements can be reordered into consecutive pairs in which the second value is exactly twice the first.

More precisely, after reordering, every index $i$ from 0 through $\lvert\texttt{arr}\rvert/2-1$ must satisfy `arr[2 * i + 1] = 2 * arr[2 * i]`. Each occurrence must be used exactly once, so duplicate values and zeroes must have sufficient matching multiplicity. Return whether such a reordering exists.

### Function Contract

Let $N$ be the length of `arr`.

**Inputs**

- `arr`: an even-length list of $N$ integers, where $2 \le N \le 3\cdot 10^4$ and `-100000 <= arr[i] <= 100000`.

**Return value**

Return `true` if all occurrences can be partitioned into pairs `(x, 2 * x)`; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [3,1,3,6]`
- Output: `false`

**Example 2**

- Input: `arr = [2,1,2,6]`
- Output: `false`

**Example 3**

- Input: `arr = [4,-2,2,-4]`
- Output: `true`
- Explanation: The occurrences can form `(-2,-4)` and `(2,4)`.
