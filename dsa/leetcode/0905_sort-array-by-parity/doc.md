# Sort Array By Parity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 905 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-parity/) |

## Problem Description
### Goal
Given an integer array `nums`, rearrange its elements so that all even integers appear at the beginning of the array and all odd integers follow them.

Return any array that satisfies this parity partition. The relative order within the even group and within the odd group does not matter, but the returned array must contain exactly the same values, with the same multiplicities, as `nums`.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 5000$ and $0 \leq \texttt{nums}[i] \leq 5000$.

**Return value**

Return a permutation of `nums` in which no odd integer occurs before an even integer.

### Examples
**Example 1**

- Input: `nums = [3,1,2,4]`
- Output: `[2,4,3,1]`

Outputs such as `[4,2,1,3]` are also valid because every even value still precedes every odd value.

**Example 2**

- Input: `nums = [0]`
- Output: `[0]`
