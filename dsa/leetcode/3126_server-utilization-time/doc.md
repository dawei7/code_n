# Server Utilization Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3126 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/server-utilization-time/) |

## Problem Description

### Goal

The `Servers` table records when identified servers start and stop running. Each row contains a server identifier, the time of the event, and a `session_status` value of either `start` or `stop`. For each server, its chronologically corresponding start and stop events delimit running sessions.

Find the total running time accumulated across every session of every server. Convert that combined duration to days and round it down, so only complete 24-hour periods are counted. Return the resulting number as `total_uptime_days`; the result has one row, so row order is immaterial.

### Function Contract

**Inputs**

The query reads `Servers(server_id, status_time, session_status)`. The combination `(server_id, status_time, session_status)` is unique, `status_time` is a datetime, and `session_status` is either `start` or `stop`.

**Return value**

Return one column named `total_uptime_days` containing the floor of the total server uptime in seconds divided by 86,400.

### Examples

**Example 1**

- Input: `Servers` contains ten start/stop pairs across server IDs 1, 3, 4, and 5, including three sessions for server 3 and four for server 4.
- Output: `[[1]]`
- Explanation: The sessions total approximately 44.46 hours. This contains one complete day, with the remaining hours discarded.
