# Maximize Win From Two Segments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2555 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximize Win From Two Segments](https://leetcode.com/problems/maximize-win-from-two-segments/) |

## Problem Description

### Goal

Prizes lie at integer coordinates on the X-axis. The non-decreasing array `prizePositions` records one coordinate per prize, so several prizes may occupy the same position. You may choose two closed segments with integer endpoints, each having length exactly `k`.

Collect every prize whose coordinate belongs to at least one chosen segment, including prizes on either endpoint. The two segments are allowed to intersect, but a prize covered by both is collected only once. Return the maximum number of prizes obtainable by placing the two segments optimally.

### Function Contract

**Inputs**

- `prizePositions`: A nonempty, non-decreasing list of $n$ prize coordinates, where $1 \le n \le 10^5$ and every coordinate is between $1$ and $10^9$, inclusive.
- `k`: The exact length of each selected segment, with $0 \le k \le 10^9$.

**Return value**

- The greatest number of distinct prizes covered by the union of two valid segments.

### Examples

**Example 1**

- Input: `prizePositions = [1, 1, 2, 2, 3, 3, 5], k = 2`
- Output: `7`
- Explanation: Segments `[1, 3]` and `[3, 5]` together cover every prize.

**Example 2**

- Input: `prizePositions = [1, 2, 3, 4], k = 0`
- Output: `2`
- Explanation: Each zero-length segment covers one coordinate, so choosing two different occupied coordinates collects two prizes.
