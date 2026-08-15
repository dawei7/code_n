# Find Maximal Uncovered Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2655 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-maximal-uncovered-ranges/) |

## Problem Description

### Goal

An abstract 0-indexed array `nums` has length `n`. You are given `ranges`, a list of inclusive index intervals; intervals may overlap, and every index contained in at least one interval is covered. The actual values of `nums` are irrelevant because only its index domain $[0,n-1]$ matters.

Partition every uncovered index into maximal contiguous uncovered ranges. Each uncovered index must occur in exactly one returned interval, and no two returned intervals may be adjacent, since adjacent uncovered intervals would form one larger maximal interval. Return these inclusive pairs in ascending order of their starting indices.

### Function Contract

**Inputs**

- `n`: The array length, where $1 \le n \le 10^9$.
- `ranges`: A list of $m$ inclusive pairs `[start, end]`, where $0 \le m \le 10^6$, $0 \le \texttt{start} \le \texttt{end} < n$.

**Return value**

- Return all maximal uncovered inclusive ranges `[start, end]`, sorted by `start` in ascending order.

### Examples

#### Example 1

- **Input:** `n = 10, ranges = [[3,5],[7,8]]`
- **Output:** `[[0,2],[6,6],[9,9]]`
- **Explanation:** The three gaps before, between, and after the covered intervals are maximal.

#### Example 2

- **Input:** `n = 3, ranges = [[0,2]]`
- **Output:** `[]`
- **Explanation:** The complete index domain is covered.

#### Example 3

- **Input:** `n = 7, ranges = [[2,4],[0,3]]`
- **Output:** `[[5,6]]`
- **Explanation:** The overlapping input intervals together cover indices `0` through `4`.
