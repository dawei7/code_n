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

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Store only timestamps that can still be recent.** Maintain a double-ended queue in increasing timestamp order. On `ping(t)`, append `t`, then compute the inclusive lower boundary `t - 3000`.

**Expire requests from the front.** While the oldest timestamp is strictly less than the lower boundary, remove it from the left of the queue. Strict comparison is essential: a request exactly at `t - 3000` is still inside the inclusive interval and must remain. Because timestamps arrive in increasing order, once the oldest request is valid, every later queued timestamp is valid as well.

**Return the active queue size.** After expiration, the queue contains exactly the requests in $[t-3000,t]$, so its length is the required answer. Each timestamp is appended once and removed at most once over the entire operation sequence. This gives constant amortized work per call even if one call removes many old requests.

#### Complexity detail

Across $m$ calls, every timestamp enters and leaves the queue at most once, so the total time is $O(m)$. In the worst case all $m$ requests fall within one 3000-millisecond interval and remain stored, requiring $O(m)$ space.

#### Alternatives and edge cases

- **Scan all previous timestamps:** Count qualifying requests from the complete history after every ping. It is correct but costs $O(m^2)$ total time.
- **Binary search in retained full history:** Find the first qualifying timestamp in $O(\log m)$ per call, but never discarding obsolete history uses $O(m)$ space and is slower than the queue's amortized bound.
- **Inclusive left boundary:** A timestamp equal to `t - 3000` must be counted; remove only smaller values.
- **Large gap between calls:** One ping may empty the old queue, after which the new request still makes the answer at least one.
- **First request:** With no older timestamps, the result is exactly one.

</details>
