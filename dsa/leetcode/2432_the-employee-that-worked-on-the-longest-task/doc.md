# The Employee That Worked on the Longest Task

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2432 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Employee That Worked on the Longest Task](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/) |

## Problem Description

### Goal

There are `n` employees with distinct identifiers from 0 through `n - 1`. Each entry `logs[i] = [id, leaveTime]` records which employee handled task $i$ and the time when that task ended. End times are strictly increasing, and consecutive tasks are handled by different employees.

Task 0 begins at time 0. Every later task begins as soon as the preceding task ends, so its duration is the difference between consecutive recorded end times. Return the employee identifier associated with the single longest task. When several tasks share the maximum duration, return the smallest employee identifier among them.

### Function Contract

**Inputs**

- `n`: The number of employees, whose identifiers lie in $[0,n-1]$.
- `logs`: The chronological task records `[employee_id, leave_time]`.

The constraints are $2 \le n \le 500$ and $1 \le \lvert\texttt{logs}\rvert \le 500$. Every leave time lies in $[1,500]$ and is strictly greater than the preceding one.

**Return value**

- The smallest employee identifier among the tasks having maximum duration.

### Examples

#### Example 1

- **Input:** `n = 10, logs = [[0, 3], [2, 5], [0, 9], [1, 15]]`
- **Output:** `1`

The task durations are 3, 2, 4, and 6, so employee 1 handled the longest one.

#### Example 2

- **Input:** `n = 26, logs = [[1, 1], [3, 7], [2, 12], [7, 17]]`
- **Output:** `3`

Employee 3's task lasts 6 units, longer than the other durations 1, 5, and 5.

#### Example 3

- **Input:** `n = 2, logs = [[0, 10], [1, 20]]`
- **Output:** `0`

Both tasks last 10 units, so the smaller employee identifier wins the tie.
