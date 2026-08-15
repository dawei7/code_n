# Find the Number of Good Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3162 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-good-pairs-i/) |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, have lengths $n$ and $m$ respectively. You are also given a positive integer `k`.

An index pair $(i,j)$ is good when `nums1[i]` is divisible by `nums2[j] * k`, where $0 \le i < n$ and $0 \le j < m$. Count all good index pairs. Equal values at different indices still form separate pairs.

### Function Contract

**Inputs**

- `nums1`: A nonempty list of positive integers.
- `nums2`: A nonempty list of positive integers.
- `k`: A positive integer multiplier.

Let $n = \lvert\texttt{nums1}\rvert$ and $m = \lvert\texttt{nums2}\rvert$. The constraints satisfy $1 \le n,m \le 50$ and every array value and `k` is between $1$ and $50$ inclusive.

**Return value**

- The total number of good index pairs.

### Examples

#### Example 1

- **Input:** `nums1 = [1, 3, 4], nums2 = [1, 3, 4], k = 1`
- **Output:** `5`

The good pairs are `(0, 0)`, `(1, 0)`, `(1, 1)`, `(2, 0)`, and `(2, 2)`.

#### Example 2

- **Input:** `nums1 = [1, 2, 4, 12], nums2 = [2, 4], k = 3`
- **Output:** `2`

Only `nums1[3] = 12` is divisible by the scaled values `6` and `12`, producing pairs `(3, 0)` and `(3, 1)`.
