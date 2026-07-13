# My Calendar II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 731 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/my-calendar-ii/) |

## Problem Description
### Goal
Design `MyCalendarTwo` for events represented by half-open intervals `[startTime, endTime)`. A double booking is allowed, but a triple booking occurs when three accepted events share a nonempty interval of time.

For each `book(startTime, endTime)` call, return `True` and store the event unless doing so would create a triple booking. If any time would then belong to three events, return `False` and leave the calendar unchanged. Events that only meet at an excluded right endpoint do not overlap.

### Function Contract
**Inputs**

- `operations`: an ordered list of `["book", start, end]` calls representing times `start <= t < end`

**Return value**

- One boolean per operation: `True` if the interval can be stored without creating a triple booking, otherwise `False` with the calendar unchanged

### Examples
**Example 1**

- Input: `operations = [["book",10,20],["book",50,60],["book",10,40],["book",5,15],["book",5,10],["book",25,55]]`
- Output: `[true,true,true,false,true,true]`

**Example 2**

- Input: `operations = [["book",5,10],["book",5,10],["book",5,10]]`
- Output: `[true,true,false]`

**Example 3**

- Input: `operations = [["book",1,5],["book",5,9],["book",3,7],["book",4,6]]`
- Output: `[true,true,true,false]`

### Required Complexity

- **Time:** $O(q \log C)$
- **Space:** $O(q \log C)$

<details>
<summary>Approach</summary>

#### General

**Store the maximum overlap over the time domain**

Use a dynamic lazy segment tree over integer coordinates from `0` through $10^{9} - 1$. Each node stores the greatest accepted-booking count anywhere in its segment and a lazy value shared by the whole segment. Nodes are created only along ranges that bookings actually touch, so the enormous coordinate domain is never materialized.

**Translate half-open bookings exactly**

A booking `[start, end)` covers the inclusive integer range `[start, end - 1]`. Query the maximum on that range before changing the tree. If it is already `2`, accepting the request would create a triple-booked point, so reject it and leave the tree untouched. Otherwise add one across the range.

**Combine lazy and child information**

A full-cover update increments both the node's maximum and its lazy value. After a partial update, the node maximum is its lazy value plus the larger maximum held by either child; a missing child contributes zero beyond the inherited lazy value. Queries similarly add the current lazy value to the best intersecting child result.

**Why every decision is correct**

The root initially represents zero accepted bookings at every time. Each successful range addition increases precisely the points covered by that half-open booking, so every node maximum remains the true greatest overlap in its segment. A queried maximum below two means adding one keeps every covered point at most double-booked. A maximum of two identifies a point that would reach three, and rejection preserves all established counts.

#### Complexity detail

Let `q` be the number of booking calls and $C = 10^{9}$ the coordinate-domain size. A range-maximum query and range addition visit $O(\log C)$ boundary paths, so all calls take $O(q \log C)$ time. Each accepted update creates at most $O(\log C)$ sparse nodes, giving $O(q \log C)$ space.

#### Alternatives and edge cases

- **Accepted intervals plus double-booked intersections:** reject a request that intersects any stored double-booked range, then add its intersections with every accepted booking; this is simple and correct but takes $O(q^2)$ time overall.
- **Ordered sweep-line deltas:** tentatively add endpoint deltas and scan their prefix sums, rolling back if the maximum reaches three; without an augmented balanced tree, every booking can require a full ordered scan.
- **Coordinate compression:** a segment tree over all endpoints is efficient when every operation is known in advance, but the native calendar must answer calls online.
- **Touching endpoints:** `[a,b)` and `[b,c)` share no time and never increase one another's overlap.
- **Duplicate intervals:** the first two identical bookings are accepted and the third is rejected.
- **Partial triple overlap:** even one point reaching an overlap count of three forces the entire new request to be rejected.
- **Rejected booking:** no part of a failed request may remain in the calendar.
- **Coordinate extremes:** `start = 0` and `end = 10 ** 9` must map safely to the segment-tree boundaries.

</details>
