# Count Days Without Meetings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3169 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-days-without-meetings/) |

## Problem Description

### Goal

An employee is available for work on every integer-numbered day from 1 through `days`. Each pair `[start, end]` in `meetings` schedules a meeting on both endpoint days and every day between them.

Count the available work days on which no meeting is scheduled. Meeting intervals may overlap, so a day covered by several intervals must still be counted as busy only once.

### Function Contract

**Inputs**

- `days`: The final day in the employee's inclusive work period.
- `meetings`: A nonempty list of inclusive meeting intervals `[start, end]`.

Let $n = \lvert\texttt{meetings}\rvert$. The constraints satisfy $1 \le \texttt{days} \le 10^9$ and $1 \le n \le 10^5$. Every interval obeys $1 \le \texttt{start} \le \texttt{end} \le \texttt{days}$.

**Return value**

- The number of days from 1 through `days` that belong to no meeting interval.

### Examples

#### Example 1

- **Input:** `days = 10, meetings = [[5,7],[1,3],[9,10]]`
- **Output:** `2`

Only days 4 and 8 have no scheduled meeting.

#### Example 2

- **Input:** `days = 5, meetings = [[2,4],[1,3]]`
- **Output:** `1`

The overlapping intervals jointly cover days 1 through 4, leaving only day 5 free.

#### Example 3

- **Input:** `days = 6, meetings = [[1,6]]`
- **Output:** `0`

The single meeting covers the entire work period.
