# Counting Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1426 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/counting-elements/) |

## Problem Description

### Goal

For every occurrence of a value `x` in `arr`, determine whether the value `x + 1` appears anywhere in the same array. Count the occurrence when such a successor exists.

Return the total count over array positions. Duplicate values are evaluated separately, so if `x` occurs several times and at least one `x + 1` exists, every occurrence of `x` contributes to the answer.

### Function Contract

**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 1000$ and $0 \le \texttt{arr[i]} \le 1000$.

**Return value**

- The number of array elements `x`, counted with multiplicity, for which `x + 1` occurs in `arr`.

### Examples

**Example 1**

- Input: `arr = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `arr = [1,1,3,3,5,5,7,7]`
- Output: `0`

**Example 3**

- Input: `arr = [1,3,2,3,5,0]`
- Output: `3`
