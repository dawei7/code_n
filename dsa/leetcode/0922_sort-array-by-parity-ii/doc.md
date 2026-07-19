# Sort Array By Parity II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 922 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-parity-ii/) |

## Problem Description
### Goal

You are given an even-length integer array `nums`. Exactly half of its values are even and the other half are odd.

Rearrange the array so that every even index contains an even value and every odd index contains an odd value. Return any permutation of the original array that satisfies this condition. An in-place solution is preferred by the follow-up.

### Function Contract
**Inputs**

- `nums`: an even-length array of $n$ integers, where $2 \le n \le 2\cdot10^4$ and $0 \le \textit{nums}[i] \le 1000$.
- Exactly $n/2$ values are even and exactly $n/2$ values are odd.

**Return value**

Any permutation of `nums` satisfying $\textit{answer}[i] \bmod 2 = i \bmod 2$ for every index $i$.

### Examples
**Example 1**

- Input: `nums = [4,2,5,7]`
- Output: `[4,5,2,7]`
- Explanation: Other arrangements such as `[2,7,4,5]` are equally valid.

**Example 2**

- Input: `nums = [2,3]`
- Output: `[2,3]`

**Example 3**

- Input: `nums = [3,2]`
- Output: `[2,3]`
