# Describe the Painting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1943 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/describe-the-painting/) |

## Problem Description
### Goal
A long, narrow painting is represented by a number line. Each input entry
paints a unique color over a half-open segment `[start, end)`. The left endpoint
belongs to the segment, while the right endpoint does not. Wherever segments
overlap, their colors form a set, represented in the output by the sum of the
distinct color values in that set.

Describe every painted portion using the minimum number of non-overlapping
half-open segments. Each result entry gives a left endpoint, a right endpoint,
and the mixed-color sum throughout that span. Unpainted gaps must be omitted.
A boundary where the underlying color set changes must remain a boundary even
if the sums on its two sides happen to be equal.

### Function Contract
**Inputs**

- `segments`: between 1 and $2\cdot 10^4$ entries of the form
  `[start, end, color]`, where
  $1 \le \textit{start} < \textit{end} \le 10^5$ and
  $1 \le \textit{color} \le 10^9$. Every color value is unique.

**Return value**

- A description `[left, right, mixedColor]` for each nonempty painted span
  `[left, right)`, excluding unpainted regions. The entries may be returned in
  any order.

### Examples
**Example 1**

- Input: `segments = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]`
- Output: `[[1, 4, 14], [4, 7, 16]]`

**Example 2**

- Input: `segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]`
- Output: `[[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]`

**Example 3**

- Input: `segments = [[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]`
- Output: `[[1, 4, 12], [4, 7, 12]]`
- Explanation: The equal sums cannot be merged because their color sets differ.
