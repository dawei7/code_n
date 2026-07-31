# Count Zero Request Servers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2747 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-zero-request-servers/) |

## Problem Description

### Goal

There are `n` servers whose identifiers range from $1$ through $n$. Each entry `logs[i] = [server_id, time]` records one request received by `server_id` at `time`. A server may appear in multiple entries, and neither the log entries nor the query times are guaranteed to be sorted.

For every value `queries[i]`, consider the inclusive time interval `[queries[i] - x, queries[i]]`. Count how many of the `n` servers have no request log whose time lies in that interval. Return these counts in the original order of `queries`; sorting queries for processing must not reorder the result.

### Function Contract

Let $m$ be the number of logs and $q$ the number of queries.

**Inputs**

- `n`: The total number of servers, where $1 \le n \le 10^5$.
- `logs`: An array of $m$ pairs `[server_id, time]`, where $1 \le m \le 10^5$, $1 \le \texttt{server_id} \le n$, and $1 \le \texttt{time} \le 10^6$.
- `x`: The window width, where $1 \le x \le 10^5$.
- `queries`: An array of $q$ query times, where $1 \le q \le 10^5$ and $x < \texttt{queries[i]} \le 10^6$.

**Return value**

Return an array of length $q$ whose $i$-th value is the number of servers with zero requests during the inclusive interval `[queries[i] - x, queries[i]]`.

### Examples

**Example 1**

- Input: `n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]`
- Output: `[1,2]`
- Explanation: Servers `1` and `2` are active in `[5,10]`, while only server `2` is active in `[6,11]`.

**Example 2**

- Input: `n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]`
- Output: `[0,1]`
- Explanation: All servers appear in `[1,3]`; server `3` is absent from `[2,4]`.
