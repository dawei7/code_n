# Maximum Element After Decreasing and Rearranging

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/) |
| Frontend ID | 1846 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You may rearrange the positive integers in `arr` in any order. You may also replace any element by a smaller positive integer, repeating this decrease operation as often as necessary; increasing a value is never allowed.

Choose those operations so that the first resulting value is $1$ and the absolute difference between every adjacent pair is at most $1$. Among all arrays satisfying those conditions, return the greatest value that any element can attain.

### Function Contract

**Inputs**

- `arr`: a nonempty list of positive integers.
- $1 \le \lvert\texttt{arr}\rvert \le 10^5$.
- $1 \le \texttt{arr}[i] \le 10^9$.
- Let $n=\lvert\texttt{arr}\rvert$.

**Return value**

- Rearrangement may be arbitrary.
- Each value may stay unchanged or decrease to another positive integer.
- The final first value must equal $1$.
- Every adjacent absolute difference must be at most $1$.
- Return the maximum possible element value among all valid final arrays.

### Examples

**Example 1**

- Input: `arr = [2, 2, 1, 2, 1]`
- Output: `2`

There are too many small values to build a valid step above 2.

**Example 2**

- Input: `arr = [100, 1, 1000]`
- Output: `3`

After sorting, the large values may be decreased to 2 and 3, producing `[1, 2, 3]`.

**Example 3**

- Input: `arr = [1, 2, 3, 4, 5]`
- Output: `5`

The array already forms the fastest permitted rise from 1.
