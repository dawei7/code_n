# Minimum Cost to Make Arrays Identical

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/) |
| Frontend ID | 3424 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You receive two integer arrays, `arr` and `brr`, with the same length. Transform `arr` until it equals `brr` while minimizing the total cost.

You may split `arr` into any number of contiguous subarrays and place those subarrays in any order. Performing this rearrangement operation costs the fixed amount `k`, independent of how many blocks are used. You may also choose an element of `arr` and add or subtract any positive integer $x$; that adjustment costs $x$. Either operation may be performed any number of times.

Return the minimum cost needed to make every position of `arr` equal to the corresponding position of `brr`.

### Function Contract

**Inputs**

- `arr`: The integer array to transform.
- `brr`: The equally long target array.
- `k`: The fixed cost of one subarray rearrangement.

Let $n$ be the common length of `arr` and `brr`.

- $1 \le n \le 10^5$
- $0 \le k \le 2 \cdot 10^{10}$
- $-10^5 \le \texttt{arr[i]}, \texttt{brr[i]} \le 10^5$

**Return value**

Return the minimum total cost as an integer.

### Examples

**Example 1**

- Input: `arr = [-7, 9, 5], brr = [7, -2, -5], k = 2`
- Output: `13`
- Explanation: Pay `2` to rearrange `arr` to `[9, 5, -7]`. Adjusting its elements by `-2`, `-7`, and `+2` then costs `11`, for a total of `13`.

**Example 2**

- Input: `arr = [2, 1], brr = [2, 1], k = 0`
- Output: `0`
- Explanation: The arrays are already identical, so no operation is necessary.
