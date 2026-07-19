# Exam Room

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 855 |
| Difficulty | Medium |
| Topics | Design, Heap (Priority Queue), Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/exam-room/) |

## Problem Description
### Goal
An exam room has $n$ seats in one row, labeled from $0$ through $n-1$. When a student enters, they choose an empty seat that maximizes the distance to the closest seated student. If several seats provide the same maximum distance, the student must take the lowest-numbered one. An empty room always assigns seat `0`.

Design `ExamRoom` to preserve this rule across arrivals and departures. `seat()` places the next student and returns the chosen label. `leave(p)` removes the student at seat `p`; each departure is guaranteed to name an occupied seat.

### Function Contract
**Inputs**

- `n`: the number of seats, where $1 \leq n \leq 10^9$.
- `operations`: an app-local trace of $q$ calls, where $1 \leq q \leq 10^4$. Each entry is `["seat"]` or `["leave", p]`. A `seat` call occurs only while a seat is available.

**Return value**

Return one result per operation: the assigned seat for `seat`, and `null` for `leave`.

The native LeetCode artifact instead implements constructor `ExamRoom(n)` and the methods `seat()` and `leave(p)` directly.

### Examples
**Example 1**

- Input: `n = 10, operations = [["seat"],["seat"],["seat"],["seat"],["leave",4],["seat"]]`
- Output: `[0,9,4,2,null,5]`

**Example 2**

- Input: `n = 1, operations = [["seat"],["leave",0],["seat"]]`
- Output: `[0,null,0]`

**Example 3**

- Input: `n = 4, operations = [["seat"],["seat"],["seat"],["seat"]]`
- Output: `[0,3,1,2]`
