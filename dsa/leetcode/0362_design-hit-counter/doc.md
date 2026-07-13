# Design Hit Counter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 362 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Design, Queue, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/design-hit-counter/) |

## Problem Description
### Goal
Design a hit counter receiving chronological integer timestamps in seconds. Each `hit(timestamp)` records one occurrence, and several hits may share the same timestamp. Recorded events persist long enough to answer later window queries.

`getHits(timestamp)` returns the number of hits during the preceding five minutes, meaning timestamps in the interval `(timestamp - 300, timestamp]`. A hit exactly 300 seconds old is excluded, while every separate hit inside the window is counted. Process calls in nondecreasing timestamp order and discard or ignore expired history efficiently. The app returns results only for query operations; the native object exposes both methods.

### Function Contract
**Inputs**

- `operations`: for the app adapter, chronological `["hit", timestamp]` and `["getHits", timestamp]` operations

**Return value**

- A list containing the integer result of each `getHits` operation in query order. Native LeetCode calls the corresponding `HitCounter` methods directly.

### Examples
**Example 1**

- Input: `operations = [["hit",1],["hit",2],["hit",3],["getHits",4]]`
- Output: `[3]`

**Example 2**

- Input: `operations = [["hit",1],["hit",2],["hit",3],["hit",300],["getHits",300],["getHits",301]]`
- Output: `[4,3]`

**Example 3**

- Input: `operations = [["getHits",100]]`
- Output: `[0]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Map time onto a fixed 300-second ring**

Only the most recent 300 timestamp values can contribute to a query. Use two arrays of length 300: one records which absolute timestamp currently owns each slot, and the other records the number of hits at that timestamp. Timestamp `t` maps to slot $t \bmod 300$.

**Reset a slot when a later cycle reuses it**

For `hit(t)`, inspect its slot. If the stored timestamp is not `t`, the slot belongs to a time at least 300 seconds older, so overwrite its timestamp and reset its count to one. If it already belongs to `t`, increment the count. This preserves multiple hits in the same second without mixing different ring cycles.

**Sum only timestamps still inside the window**

For `getHits(t)`, examine all 300 slots and include a count exactly when `t - stored_timestamp < 300`. Chronological input ensures stored timestamps are never in the future. The ring contains the aggregated count for every second that could still be relevant; expired slots either fail this comparison or have already been overwritten. Therefore the sum is precisely the hits in `[t - 299, t]`.

#### Complexity detail

A hit performs constant work. A query scans exactly 300 slots, which is $O(1)$ because the five-minute window is fixed rather than input-sized. Both arrays have fixed length 300, so storage is $O(1)$. The app adapter's query-result list is output space.

#### Alternatives and edge cases

- **Queue every hit:** supports amortized $O(1)$ eviction but may store many entries when one second receives a burst of hits.
- **Store timestamp-count pairs in a deque:** compresses same-second bursts and uses space proportional to active seconds, but still requires eviction bookkeeping.
- **Keep all history and binary-search:** gives $O(\log n)$ queries and unbounded $O(n)$ storage.
- Hits at timestamp $t - 299$ are included, while hits at $t - 300$ are expired.
- Multiple hits at the same timestamp accumulate in one ring slot.
- A query before any hit returns zero.
- Slot reuse must reset the old count instead of adding across timestamps 300 seconds apart.

</details>
