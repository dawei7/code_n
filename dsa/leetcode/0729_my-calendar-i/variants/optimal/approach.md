## General

**Preserve one crucial invariant: accepted events never overlap**

The calendar accepts a new half-open interval `[start, end)` only when it has no nonempty intersection with any previously accepted event. Rejected events must leave the stored calendar unchanged.

Because accepted events are mutually nonoverlapping, they have a consistent chronological order. If one accepted event ends before another, its start is also earlier. The exact solution exploits this order with a `SortedDict`, but it uses an unusual representation:

- Each key is an accepted event’s `end`.
- The corresponding value is that event’s `start`.

The keys are therefore maintained in increasing ending-time order.

**Half-open intervals may touch**

Two events `[a, b)` and `[c, d)` do not overlap when `b <= c` or `d <= a`. Equality is allowed because the right endpoint is excluded. For example, `[10, 20)` and `[20, 30)` share the written boundary 20 but no actual time point.

They overlap exactly when both `a < d` and `c < b` are true. Every comparison in the solution must preserve these strict versus non-strict boundary meanings.

**Locate the first event that does not finish before the new one**

For a requested `[start, end)`, the code computes

`idx = self.sd.bisect_right(start)`.

Because the sorted keys are existing ending times, this returns the position of the first key strictly greater than `start`. Every event before `idx` has `existing_end <= start`, so it finishes before the new event begins or touches it exactly. None of those earlier events can overlap the new booking.

If `idx == len(self.sd)`, no existing event ends after `start`. Every stored event is safely to the left, so the new event can be accepted.

**Why checking one candidate is enough**

When `idx` is inside the sorted dictionary, the event at that position is the earliest-ending accepted event whose end is greater than the new start. Call its interval `[candidate_start, candidate_end)`.

The first overlap condition, `start < candidate_end`, is already guaranteed because `candidate_end` is the first key greater than `start`. The only remaining question is whether `candidate_start < end`. The code obtains that start through `self.sd.values()[idx]` and rejects when

`candidate_start < end`.

If instead `candidate_start >= end`, the candidate begins at or after the new event ends, so the two do not overlap. All still-later accepted events also begin no earlier than this candidate because accepted intervals are mutually disjoint and chronologically ordered. They cannot overlap either.

Thus a single neighbor-like check rules out every possible conflict. Events before `idx` end too early, and events after `idx` start no earlier than the checked candidate.

**Insert only after the conflict test succeeds**

If the candidate overlaps, the method returns `False` immediately. It performs no assignment, so the failed request does not alter the calendar.

If no conflict exists, it stores

`self.sd[end] = start`

and returns `True`. Since the new event was proved disjoint from every existing event, the invariant needed by future one-candidate searches remains true.

An accepted event cannot accidentally overwrite another event with the same end key. Two positive-length intervals with the same end would overlap near that endpoint unless they were the same rejected duplicate. The validation step prevents accepting such a conflict.

**Trace the standard sequence**

Start with an empty calendar.

- Booking `[10, 20)` finds no key and stores `20 -> 10`.
- Booking `[15, 25)` searches for the first existing end greater than 15 and finds key 20, whose start is 10. Since `10 < 25`, the intervals overlap and the request is rejected.
- Booking `[20, 30)` uses `bisect_right(20)`. The existing key 20 is not strictly greater than the new start, so it lies before the insertion position. No later key exists, and the booking is accepted.

The third call demonstrates why `bisect_right` and the strict key comparison are correct for half-open intervals: an event ending exactly at the new start is compatible.

**Why the method is correct over all calls**

Initially the stored calendar is empty and therefore nonoverlapping. Assume all stored events before a call are pairwise disjoint. Binary search partitions them into events ending no later than the new start and events ending later.

The first group cannot overlap the new event. In the second group, the earliest-ending event is checked. If its start is before the new end, it overlaps and rejection is correct. If its start is at or after the new end, it and every chronologically later disjoint event begin too late to overlap. Acceptance is therefore correct.

Rejected calls make no change. Accepted calls add an interval proved disjoint from all others, preserving the induction invariant. Every returned Boolean consequently matches whether the booking can be added without a double booking.

## Complexity detail

Let `b` be the number of events currently accepted. `SortedDict.bisect_right` takes `O(log b)` time. Indexing its ordered values and inserting a new key also take logarithmic time in the balanced sorted structure. One `book` call therefore costs `O(log b)` time.

Across `q` booking requests, the total is `O(q log q)` in the worst case, because `b <= q`. The exact implementation is based on accepted endpoints, not a dynamic segment tree over a coordinate domain `C`, so `O(q log q)` is the direct bound for this stored code.

The dictionary holds one key-value pair per accepted event, requiring `O(b)` space and at most `O(q)` over the full sequence. It does not allocate storage proportional to the maximum time value of `10^9`.

## Alternatives and edge cases

- **Store intervals by start time:** Search the insertion point and check the immediate predecessor’s end plus the immediate successor’s start. This is the more conventional sorted-calendar representation and has the same balanced-tree complexity.

- **Linear list scan:** Check the new event against every accepted interval. It is simple and uses `O(q)` space, but one call costs `O(q)` and all calls can cost `O(q^2)`.

- **Built-in Python list with binary search:** Finding the position costs `O(log q)`, but insertion shifts elements and costs `O(q)`. A true sorted-tree container is what gives the exact solution logarithmic insertion.

- **Dynamic segment tree:** Query whether the requested coordinate range is already occupied, then update it. This can use `O(log C)` time per call over coordinate range `C`, but it is considerably more machinery than needed when double bookings are entirely forbidden.

- **Touching endpoints:** `[10, 20)` and `[20, 30)` are compatible. Searching with `bisect_right(start)` places an existing end equal to `start` safely on the nonconflicting side.

- **Duplicate booking:** The first stored interval whose end exceeds the repeated start has a start below the repeated end, so the duplicate is rejected.

- **New event before every stored event:** `idx` is zero. The first event is checked; if it starts at or after the new end, every later event is also safe.

- **New event after every stored event:** `idx` equals the dictionary length because all existing ends are at most the new start. Acceptance requires no candidate check.

- **Rejected requests:** The return occurs before assignment, so no endpoint from a failed booking contaminates later searches.

- **Positive interval length:** The contract `start < end` rules out empty events and supports the reasoning that two accepted events cannot share an end key.
