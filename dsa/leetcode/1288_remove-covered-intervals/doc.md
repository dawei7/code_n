# Remove Covered Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1288 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-covered-intervals/) |

## Problem Description
### Goal
You are given a collection of unique half-open intervals `[left, right)`. An interval `[a, b)` is covered by another interval `[c, d)` exactly when $c \le a$ and $b \le d$; equality at either boundary is allowed.

Remove every interval covered by some other interval in the collection. Return the number of intervals that remain after all covered intervals are excluded.

### Function Contract
**Inputs**

- `intervals`: an array of $n$ unique pairs `[left, right]`, representing half-open intervals, where $1 \le n \le 1000$ and $0 \le \texttt{left} < \texttt{right} \le 10^5$.

**Return value**

The number of intervals for which no distinct input interval starts no later and ends no earlier.

### Examples
**Example 1**

- Input: `intervals = [[1,4],[3,6],[2,8]]`
- Output: `2`
- Explanation: `[3,6)` is covered by `[2,8)`; the other two intervals remain.

**Example 2**

- Input: `intervals = [[1,4],[2,3]]`
- Output: `1`

**Example 3**

- Input: `intervals = [[0,10],[5,12]]`
- Output: `2`
- Explanation: The intervals overlap, but neither covers the other.
