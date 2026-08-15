# Find the Number of Good Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3164 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-good-pairs-ii/) |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, have lengths $n$ and $m$ respectively. You are also given a positive integer `k`.

An index pair $(i,j)$ is good when `nums1[i]` is divisible by `nums2[j] * k`, where $0 \le i < n$ and $0 \le j < m$. Return the total number of good pairs. Values occurring at several indices contribute separately, even when those values are equal.

### Function Contract

**Inputs**

- `nums1`: A nonempty list of positive integers.
- `nums2`: A nonempty list of positive integers.
- `k`: A positive integer multiplier.

Let $n = \lvert\texttt{nums1}\rvert$, $m = \lvert\texttt{nums2}\rvert$, and

$$
V = \left\lfloor \frac{\max(\texttt{nums1})}{\texttt{k}} \right\rfloor.
$$

The constraints satisfy $1 \le n,m \le 10^5$, $1 \le \texttt{nums1[i]},\texttt{nums2[j]} \le 10^6$, and $1 \le \texttt{k} \le 10^3$.

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

Only `nums1[3] = 12` is divisible by both scaled values, `6` and `12`, producing pairs `(3, 0)` and `(3, 1)`.
