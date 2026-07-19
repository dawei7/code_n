# Kth Missing Positive Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1539 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/) |

## Problem Description
### Goal
You are given a strictly increasing array `arr` of positive integers and a positive integer `k`. Some positive integers may be absent before the first stored value, between consecutive entries, or after the final entry.

List every positive integer that does not occur in `arr` in increasing order. Using one-based rank, return the $k$th value in that missing sequence. Values already present in the array never count toward the rank, even when the answer lies beyond the array's largest element.

### Function Contract
**Inputs**

- `arr`: a strictly increasing array of positive integers, with length $n$ between $1$ and $1000$ and values at most $1000$.
- `k`: the one-based rank of the missing positive integer to find, where $1 \le k \le 1000$.

**Return value**

The $k$th positive integer absent from `arr`.

### Examples
**Example 1**

- Input: `arr = [2, 3, 4, 7, 11], k = 5`
- Output: `9`
- Explanation: The missing sequence starts `1, 5, 6, 8, 9`, so its fifth value is `9`.

**Example 2**

- Input: `arr = [1, 2, 3, 4], k = 2`
- Output: `6`
- Explanation: The first two missing positives are `5` and `6`.
