## General

The minimum number of rooms is the greatest number of meetings active at the same time. If five meetings overlap at one instant, at least five rooms are unavoidable. Conversely, if the maximum simultaneous count is five, assigning a free room whenever a meeting starts never needs more than five rooms. The scheduling problem can therefore be reduced to finding the peak overlap.

The exact solution treats every meeting as two changes on a discrete timeline:

- at its start time `l`, the active-meeting count increases by one;
- at its end time `r`, the active-meeting count decreases by one.

It stores those changes in a difference array `d`, then takes prefix sums across time. The running prefix `s` is the number of meetings active at that time, and the largest value ever reached is the required room count.

**Choose the timeline size**

The source first computes

```text
m = max(e[1] for e in intervals)
```

so `m` is the latest end time. No event occurs after `m`, and all starts are smaller than their corresponding ends, so every relevant coordinate lies from `0` through `m`. The array `d = [0] * (m + 1)` provides one cell for each of those integer times.

The problem guarantees at least one interval, which is why `max` is safe without an empty-input branch. It also bounds every endpoint by $10^6$, making this direct timeline allocation feasible.

**Encode intervals as boundary events**

For each `[l, r]`, the code performs

```text
d[l] += 1
d[r] -= 1
```

This represents a half-open meeting interval $[l,r)$: the room is occupied starting at `l` and becomes free at `r`. That convention matches scheduling semantics. A meeting ending at time `10` can share a room with one starting at time `10`.

If several events occur at one coordinate, the difference array combines them before the prefix is examined. For example, two meetings ending and three starting at time `t` contribute a net change of `+1`. The two released rooms are immediately reusable, so the active count grows by only one. There is no incorrect moment where all five boundary events are treated as simultaneous occupancy.

**Recover active counts with a prefix sum**

The variables `ans` and `s` begin at zero. Scanning `d` from time `0` to time `m`, the solution adds the current delta into `s`. After processing coordinate `t`,

$$
s=\sum_{x=0}^{t}d[x].
$$

Every meeting with start at most `t` has contributed `+1`. Every meeting with end at most `t` has contributed `-1`. Their difference is exactly the number of meetings whose start has occurred but whose end has not left them active—in other words, meetings satisfying $l\le t<r$.

After each update, `ans = max(ans, s)` remembers the greatest simultaneous count seen so far. The method returns that peak after all event times are processed.

**Trace through the first example**

For `[[0, 30], [5, 10], [15, 20]]`, the nonzero deltas are:

| Time | Change | Explanation |
|---:|---:|---|
| 0 | +1 | `[0, 30]` starts |
| 5 | +1 | `[5, 10]` starts |
| 10 | -1 | `[5, 10]` ends |
| 15 | +1 | `[15, 20]` starts |
| 20 | -1 | `[15, 20]` ends |
| 30 | -1 | `[0, 30]` ends |

The prefix count is one from time `0`, rises to two at time `5`, falls to one at `10`, rises to two again at `15`, and eventually returns to zero. The maximum is two, so two rooms are both necessary and sufficient.

For `[[7, 10], [2, 4]]`, the first meeting has already ended before the second chronological start. The prefix count never exceeds one, even though the input intervals arrive in the opposite order. Event accumulation makes input order irrelevant.

**Why the peak equals the minimum room count**

At any time where `s = p`, there are $p$ ongoing meetings. One room cannot host two ongoing meetings, so every valid schedule needs at least $p$ rooms. In particular, it needs at least `ans`, the maximum such $p$.

For the matching upper bound, process start and end events chronologically. An end releases a room, and a start occupies one. Maintaining exactly the current active count is always possible because a start either reuses a room released at that time or increases the number simultaneously occupied. Since that count never exceeds `ans`, `ans` rooms suffice. Being both a lower bound and an achievable upper bound, `ans` is the minimum.

**Exact source versus the manifest summary**

The manifest describes separately sorted starts and ends with an $O(n\log n)$ sweep. That is a standard solution, but it is not the protected Python implementation. The exact source uses a dense difference array indexed by time. Its performance depends on the maximum endpoint, and its true complexity must reflect that coordinate range.

## Complexity detail

Let $n$ be the number of meetings and $M$ be the maximum end time. Finding `m` scans all intervals in $O(n)$ time. Allocating the difference array takes $O(M)$ time and space, recording all boundaries takes $O(n)$ time, and scanning the timeline takes $O(M)$ time. The total time is

$$
O(n+M),
$$

and auxiliary space is $O(M)$.

Under the supplied constraint $M\le10^6$, this is a bounded and practical allocation. It can outperform comparison sorting when many meetings share a moderate coordinate range. It is not accurately described as the manifest's $O(n\log n)$ time and $O(n)$ space: if only one meeting ends at a very large coordinate, the dense array still contains every intervening time cell.

The scan uses only constant scalar state beyond `d`. The input intervals are read but neither sorted nor modified.

## Alternatives and edge cases

- **Sorted start and end arrays:** Sort the two event lists and sweep them with pointers, reusing a room when an end is no later than the next start. This gives $O(n\log n)$ time and $O(n)$ space independent of coordinate magnitude and is the algorithm summarized by the manifest.
- **Min-heap of room end times:** Sort meetings by start, reuse the room with the earliest end when possible, and push each current end. It takes $O(n\log n)$ time and up to $O(n)$ space and can also support explicit room assignments.
- **Sparse event map:** Store deltas only at observed times, sort those keys, and prefix-sum them. It avoids $O(M)$ dense storage while retaining the event-count idea, at the cost of $O(n\log n)$ sorting.
- **Meetings touching at an endpoint:** `d[r] -= 1` and `d[r] += 1` from another start combine at the same coordinate, so the ending room is immediately reused and no extra room is counted.
- **Several identical intervals:** Their start deltas and end deltas accumulate, causing the peak to equal the number of identical meetings, as required.
- **Nested intervals:** Every contained meeting increases the prefix while the outer meeting remains active, so nested concurrency is counted naturally.
- **Unsorted input:** No sorting is needed; additions to `d` commute, and the later timeline scan supplies chronological order.
- **Start time zero:** Index zero exists, its positive delta is included in the first prefix step, and the meeting is counted immediately.
- **Latest end time:** The array includes index `m`, so all final negative events are applied and the active count returns to zero after the last meetings end.
- **One meeting:** Its prefix count peaks at one and returns to zero, so exactly one room is returned.
- **Empty input:** The formal constraints require at least one meeting. Outside the contract, `max` would raise an exception, so supporting emptiness would require an early `return 0`.
- **Very sparse huge coordinates:** Dense allocation becomes undesirable if endpoint bounds are relaxed. A sorted-event or heap approach would then be more memory-efficient.
