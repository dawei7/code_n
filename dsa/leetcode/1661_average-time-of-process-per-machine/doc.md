# Average Time of Process per Machine

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1661 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/average-time-of-process-per-machine/) |

## Problem Description
### Goal
The `Activity` table records when each process starts and ends on a factory machine. Every `(machine_id, process_id)` pair has exactly one `start` row and one `end` row, and the start timestamp is earlier. All machines run the same number of processes.

For each machine, calculate every process duration as its end timestamp minus its start timestamp, then average those durations. Return one row per machine with the average named `processing_time` and rounded to three decimal places. Result rows may appear in any order.

### Function Contract
**Input table**

`Activity`

| Column | Type | Meaning |
|---|---|---|
| `machine_id` | integer | Machine identifier. |
| `process_id` | integer | Process identifier within the machine. |
| `activity_type` | enum | Either `start` or `end`. |
| `timestamp` | float | Event time in seconds. |

The composite key is `(machine_id, process_id, activity_type)`. Let $R$ be the number of rows in `Activity`.

**Return value**

Return columns `machine_id` and `processing_time`, with one row per machine and the average duration rounded to three decimal places.

### Examples
**Example 1**

For machine 0, processes lasting `1.520 - 0.712` and `4.120 - 3.140` seconds have average duration `0.894`. Applying the same calculation to machines 1 and 2 produces:

- Output: `[[0, 0.894], [1, 0.995], [2, 1.456]]`
