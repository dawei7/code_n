# Previous Permutation With One Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1053 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/previous-permutation-with-one-swap/) |

## Problem Description

### Goal

Given an array `arr` of positive integers that are not necessarily distinct, exchange the values at exactly two positions to create a permutation that is lexicographically smaller than `arr`.

Among all smaller arrays obtainable by one swap, return the lexicographically largest one. Lexicographic order is determined by the values at the first position where two arrays differ. If no swap can produce a strictly smaller array, return `arr` unchanged.

### Function Contract

**Inputs**

- `arr`: an array of length $N$, where $1 \le N \le 10^4$ and $1 \le \texttt{arr[i]} \le 10^4$.

**Return value**

- The lexicographically largest array strictly smaller than the input that can be obtained with one swap, or the unchanged array if none exists.

### Examples

**Example 1**

- Input: `arr = [3,2,1]`
- Output: `[3,1,2]`
- Explanation: Swap `2` and `1`.

**Example 2**

- Input: `arr = [1,1,5]`
- Output: `[1,1,5]`
- Explanation: No swap produces a smaller permutation.

**Example 3**

- Input: `arr = [1,9,4,6,7]`
- Output: `[1,7,4,6,9]`
- Explanation: Swap `9` and `7`.
