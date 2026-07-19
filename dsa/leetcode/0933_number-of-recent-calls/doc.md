# Number of Recent Calls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 933 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Design, Queue, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [number-of-recent-calls](https://leetcode.com/problems/number-of-recent-calls/) |

## Problem Description

### Goal

Implement a `RecentCounter` class that tracks requests arriving over time. A newly constructed counter begins with no recorded requests.

Calling `ping(t)` adds a request at time `t`, measured in milliseconds, and returns how many recorded requests have timestamps in the inclusive interval $[t-3000,t]$, including the request just added. Every `ping` call is guaranteed to use a strictly larger timestamp than the preceding call, and at most $10^4$ calls are made.

### Function Contract

**Inputs**

- `operations`: the app-local ordered sequence of `ping` calls, represented as pairs such as `["ping", t]`.
- Each timestamp satisfies $1 \le t \le 10^9$ and timestamps are strictly increasing.

Let $m$ be the number of `ping` operations in the sequence.

**Return value**

Return one integer for each operation: the number of requests, including the current one, whose timestamps lie in its inclusive 3000-millisecond window.

The native LeetCode artifact instead exposes `RecentCounter()` and its stateful `ping(t)` method directly.

### Examples

**Example 1**

- Input: `operations = [["ping",1],["ping",100],["ping",3001],["ping",3002]]`
- Output: `[1,2,3,3]`
- Explanation: At time `3001`, timestamp `1` remains included at the left boundary. At time `3002`, it falls outside the window.
