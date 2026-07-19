# Maximum of Absolute Value Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1131 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-of-absolute-value-expression/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`, with the same length. For any two valid indices $i$ and $j$, consider the sum of the absolute difference between their `arr1` values, the absolute difference between their `arr2` values, and the absolute difference between the indices themselves.

Return the maximum possible value of

$$
\lvert \texttt{arr1[i]}-\texttt{arr1[j]} \rvert
+ \lvert \texttt{arr2[i]}-\texttt{arr2[j]} \rvert
+ \lvert i-j \rvert
$$

over every pair satisfying $0 \le i,j < n$. The two indices may be equal, though such a choice contributes zero and cannot beat a positive value from distinct points.

### Function Contract

**Inputs**

- `arr1`: an integer array of length $n$, where $2 \le n \le 4 \times 10^4$ and every value lies in $[-10^6,10^6]$.
- `arr2`: an integer array with the same length and value bounds as `arr1`.

**Return value**

The maximum value of the stated absolute-difference expression over all valid index pairs.

### Examples

**Example 1**

- Input: `arr1 = [1,2,3,4]`, `arr2 = [-1,4,5,6]`
- Output: `13`

**Example 2**

- Input: `arr1 = [1,-2,-5,0,10]`, `arr2 = [0,-2,-1,-7,-4]`
- Output: `20`
