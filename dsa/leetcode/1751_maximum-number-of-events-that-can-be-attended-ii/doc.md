# Maximum Number of Events That Can Be Attended II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1751 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/) |

## Problem Description

### Goal

You are given `events`, where each event is described by `[startDay, endDay, value]`. Attending an event requires being present for its entire interval and earns its associated value. You may attend at most `k` events, and attending fewer than `k` is allowed.

Only one event may be attended at a time. End days are inclusive, so two events conflict when one starts on the same day that the other ends; a later event is compatible only when its start day is strictly greater than the earlier event's end day. Return the maximum total value obtainable from a compatible selection.

### Function Contract

**Inputs**

- `events`: a nonempty list of triples `[startDay, endDay, value]`, where $1 \le \texttt{startDay} \le \texttt{endDay} \le 10^9$ and $1 \le \texttt{value} \le 10^6$.
- `k`: the maximum number of events that may be selected, with $1 \le k \le n$ and $k n \le 10^6$.

Let $n=\lvert\texttt{events}\rvert$.

**Return value**

- Return the maximum sum of values from at most `k` pairwise non-overlapping events, treating every end day as inclusive.

### Examples

**Example 1**

- Input: `events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]], k = 2`
- Output: `7`
- Explanation: The first and second events are compatible and contribute `4 + 3`.

**Example 2**

- Input: `events = [[1, 2, 4], [3, 4, 3], [2, 3, 10]], k = 2`
- Output: `10`
- Explanation: The value-10 event overlaps both others, and selecting only it is optimal.

**Example 3**

- Input: `events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k = 3`
- Output: `9`
- Explanation: All events are mutually compatible, but only the three highest-valued ones may be selected.
