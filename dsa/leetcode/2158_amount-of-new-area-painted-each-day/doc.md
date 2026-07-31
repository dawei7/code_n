# Amount of New Area Painted Each Day

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2158 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/amount-of-new-area-painted-each-day/) |

## Problem Description

### Goal

Represent a long, narrow painting by a number line. On day $i$, the pair
`paint[i] = [start_i, end_i]` requests painting the half-open interval
$[\textit{start}_i,\textit{end}_i)$. Its area is therefore
$\textit{end}_i-\textit{start}_i$.

Previously painted area must not be painted again because overlapping coats
would make the result uneven. For every day, report only the amount of its
requested interval that has never appeared in any earlier day's interval.
Return these daily amounts in their original chronological order.

### Function Contract

**Inputs**

- `paint`: an array of $n$ endpoint pairs, where
  $1 \le n \le 10^5$ and each pair satisfies
  $0 \le \textit{start}_i < \textit{end}_i \le 5\cdot10^4$.

**Return value**

An integer list of length $n$ whose entry $i$ is the newly painted area on day
$i$.

### Examples

**Example 1**

- Input: `paint = [[1, 4], [4, 7], [5, 8]]`
- Output: `[3, 3, 1]`
- Explanation: The first two days add disjoint length-three areas; on the last
  day only `[7, 8)` is new.

**Example 2**

- Input: `paint = [[1, 4], [5, 8], [4, 7]]`
- Output: `[3, 3, 1]`
- Explanation: On day two, `[5, 7)` is already covered, leaving only `[4, 5)`.

**Example 3**

- Input: `paint = [[1, 5], [2, 4]]`
- Output: `[4, 0]`
- Explanation: The second interval lies entirely inside the first.
