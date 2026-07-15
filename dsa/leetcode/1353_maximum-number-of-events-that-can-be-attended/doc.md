# Maximum Number of Events That Can Be Attended

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1353 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) |

## Problem Description

### Goal

You are given a list of events. Event `i` is described by `[startDay, endDay]` and may be attended on any one integer day $d$ satisfying $startDay \le d \le endDay$.

You may attend at most one event on a given day, and attending an event uses only the chosen day rather than its entire interval. Select which events to attend and assign each selected event a valid day so that the number attended is as large as possible. Return that maximum count.

### Function Contract

**Inputs**

- `events`: a nonempty list of inclusive `[startDay, endDay]` intervals.
- Let $n$ be the number of events.

**Return value**

- Return the maximum number of events that can be assigned distinct valid attendance days.

### Examples

**Example 1**

- Input: `events = [[1,2],[2,3],[3,4]]`
- Output: `3`

**Example 2**

- Input: `events = [[1,2],[2,3],[3,4],[1,2]]`
- Output: `4`

**Example 3**

- Input: `events = [[1,1],[1,1],[1,1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sweep attendance days in increasing order.** Sort events by start day. Maintain an index into that ordering and a min-heap containing the end days of every event that has started but has not been attended.

If the heap is empty, jump the current day directly to the next event's start; empty calendar gaps never help. Push every event whose start is at most the current day, then remove heap entries whose end is before the day because those events have expired.

**Attend the event with the earliest deadline.** If an active event remains, remove the smallest end day, attend that event today, increment the answer, and advance one day. Choosing the earliest deadline cannot reduce the achievable total: if an optimal schedule instead attends a later-ending active event today, swap the earliest-ending event into today. The displaced event can use the day originally assigned to the earlier-ending event, because it started no later than today and ends at least as late. Thus an optimal schedule always exists with the greedy choice.

The sweep repeats until neither unseen nor active events remain, so every counted event has a distinct valid day and the exchange argument proves the count is maximum.

#### Complexity detail

Sorting costs $O(n \log n)$. Each event is pushed into and removed from the heap at most once, adding $O(n \log n)$ time. The sorted list and heap hold at most $n$ events, giving $O(n)$ auxiliary space when the input is not reused.

#### Alternatives and edge cases

- **Repeated linear deadline selection:** Scanning all remaining events to choose one each day is correct with the same greedy rule but costs $O(n^2)$ time.
- **Sort only by end day:** Assigning each event its first free valid day can also be implemented with a successor structure, but a naive search for free days may be slow.
- **Identical one-day events:** At most one can be attended because they share their only valid day.
- **Large gaps between events:** Jumping directly to the next start avoids iterating unused days.
- **Expired events:** They must be removed before choosing today's event.
- **Nested intervals:** The earliest-ending active interval must take priority over a more flexible event.

</details>
