# Make K-Subarray Sums Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2607 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-k-subarray-sums-equal/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `arr` and an integer `k`. Treat `arr` as circular: the element after its last position is the first element, and the element before its first position is the last element.

In one operation, choose any element and increase or decrease it by exactly $1$. You may perform this operation any number of times on any positions.

Return the minimum number of operations required to make the sums of all circular subarrays of length `k` equal. A subarray is a contiguous segment, with wrapping allowed by the circular interpretation.

### Function Contract

**Inputs**

- `arr`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$ and $1 \leq \texttt{arr[i]} \leq 10^9$.
- `k`: The circular subarray length, where $1 \leq k \leq n$.

**Return value**

- The minimum total number of unit increments and decrements needed to equalize every length-`k` circular subarray sum.

### Examples

**Example 1**

- Input: `arr = [1,4,1,3], k = 2`
- Output: `1`

Decreasing the value at index $1$ from $4$ to $3$ produces `[1,3,1,3]`; every circular length-$2$ subarray then sums to $4$.

**Example 2**

- Input: `arr = [2,5,5,7], k = 3`
- Output: `5`

Changing the first and last values to $5$ costs $3+2=5$ and makes the array constant, so every circular length-$3$ sum is equal.
