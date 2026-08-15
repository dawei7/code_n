# Handling Sum Queries After Update

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2569 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [handling-sum-queries-after-update](https://leetcode.com/problems/handling-sum-queries-after-update/) |

## Problem Description

### Goal

You are given two zero-indexed arrays of equal length, `nums1` and `nums2`, together with a sequence of three-field queries. `nums1` is binary, while `nums2` contains non-negative integers. Process every query in order, preserving the effects of earlier updates.

A query `[1, l, r]` flips every bit of `nums1` from index `l` through `r`, inclusive. A query `[2, p, 0]` updates every position by setting `nums2[i] = nums2[i] + nums1[i] * p`. A query `[3, 0, 0]` asks for the current sum of all values in `nums2`. Return the answers to type-3 queries in their original order.

### Function Contract

**Inputs**

- `nums1`: A binary list of length $n$, where $1 \le n \le 10^5$.
- `nums2`: A list of the same length, where $0 \le \texttt{nums2[i]} \le 10^9$.
- `queries`: A list of $q$ three-integer queries, where $1 \le q \le 10^5$. Type-1 endpoints satisfy $0 \le l \le r < n$, and a type-2 multiplier satisfies $0 \le p \le 10^6$.

**Return value**

- A list containing the current sum of `nums2` for each type-3 query, in processing order.

### Examples

#### Example 1

- **Input:** `nums1 = [1, 0, 1], nums2 = [0, 0, 0], queries = [[1, 1, 1], [2, 1, 0], [3, 0, 0]]`
- **Output:** `[3]`
- **Explanation:** The flip makes `nums1 = [1, 1, 1]`; the type-2 query then adds $1$ at all three positions of `nums2`.

#### Example 2

- **Input:** `nums1 = [1], nums2 = [5], queries = [[2, 0, 0], [3, 0, 0]]`
- **Output:** `[5]`
- **Explanation:** A zero multiplier leaves the sum unchanged.

#### Example 3

- **Input:** `nums1 = [0, 1], nums2 = [2, 3], queries = [[3, 0, 0], [1, 0, 1], [2, 2, 0], [3, 0, 0]]`
- **Output:** `[5, 7]`
- **Explanation:** After the flip, only the first bit is one, so the type-2 query increases the total by $2$.
