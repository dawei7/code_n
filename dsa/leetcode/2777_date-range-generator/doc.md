# Date Range Generator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2777 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/date-range-generator/) |

## Problem Description

### Goal

Given a start date `start`, an end date `end`, and a positive integer `step`, create a generator that yields calendar dates beginning at `start` and continuing toward `end`. Consecutive yielded dates must be exactly `step` days apart.

The range is inclusive: yield `end` when it lies on the progression formed from `start`. If a step passes beyond `end`, stop without yielding that later date. Every yielded value must be a string in `YYYY-MM-DD` format.

### Function Contract

**Inputs**

- `start`: The first date, written as a `YYYY-MM-DD` string.
- `end`: The inclusive upper date, also written as a `YYYY-MM-DD` string, with `new Date(start) <= new Date(end)`.
- `step`: The positive number of days between consecutive yielded values, where $1 \le \textit{step} \le 1000$.

Let $d$ be the difference between `start` and `end` in days, where $0 \le d \le 1500$. The generator yields

$$
k = \left\lfloor \frac{d}{\textit{step}} \right\rfloor + 1
$$

dates.

For the app-local serializable adapter, `summary` may request a compact description of a generated range instead of materializing its entire result in benchmark output.

**Return value**

Return a generator object. Iterating it yields the $k$ dates in increasing order as `YYYY-MM-DD` strings, then finishes.

### Examples

**Example 1**

- Input: `start = "2023-04-01"`, `end = "2023-04-04"`, `step = 1`
- Output: `["2023-04-01","2023-04-02","2023-04-03","2023-04-04"]`
- Explanation: Advancing one day at a time lands exactly on the inclusive endpoint.

**Example 2**

- Input: `start = "2023-04-10"`, `end = "2023-04-20"`, `step = 3`
- Output: `["2023-04-10","2023-04-13","2023-04-16","2023-04-19"]`
- Explanation: The next three-day step would be April 22, which is beyond `end`.

**Example 3**

- Input: `start = "2023-04-10"`, `end = "2023-04-10"`, `step = 1`
- Output: `["2023-04-10"]`
- Explanation: An equal start and end still produces that one inclusive date.
