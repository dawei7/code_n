## General

**Represent intervals by changes at their endpoints**

The calendar permits a time to be covered by one or two accepted events, but never three. The exact solution uses a sweep-line difference map stored in a `SortedDict`.

For every tentative half-open booking `[startTime, endTime)`:

- Add `1` at `startTime` because one more active event begins there.
- Add `-1` at `endTime` because that event stops being active there.

If the endpoint deltas are processed in increasing time order, their running prefix sum equals the number of active accepted events between the current coordinate and the next coordinate.

This sparse representation is crucial because endpoint values may be as large as `10^9` while there are at most a few thousand endpoint occurrences. The solution stores only coordinates that actually appear.

**Why the half-open convention matches the deltas**

An event is active at its start but inactive at its end. When one event ends at time 20 and another begins at 20, their deltas are combined at the same map key: one contributes `-1` and the other `+1`. The running count after processing that coordinate reflects the events active immediately after 20, without falsely counting the two touching intervals as overlapping.

There is no need to process an “end event” and a “start event” in a special order because all changes at an equal coordinate are accumulated into one net dictionary value.

**Tentatively insert, then validate**

The method first changes the map as if the new event were accepted:

`self.sd[startTime] += 1`

and

`self.sd[endTime] -= 1`.

It then scans `self.sd.values()` in sorted-key order. Starting from `s = 0`, it adds each delta. If `s` ever becomes greater than two, the tentative booking creates a triple-booked segment.

The scan checks the complete timeline, not just the new event’s endpoints. A triple overlap may occur anywhere inside the requested interval where two existing events already overlap.

**Rollback a rejected booking**

If the running count exceeds two, the method reverses exactly the two tentative changes:

- Subtract one from the start delta.
- Add one to the end delta.

It then returns `False`. These inverse operations restore every prefix sum to its pre-call value, so a rejected booking has no semantic effect on future calls.

The exact code leaves keys whose restored delta becomes zero in the `SortedDict`. A zero delta does not change any prefix sum, so this is correct. It may retain endpoint coordinates from rejected requests, but their number is still linear in the number of calls.

If the sweep finishes without exceeding two, the tentative changes remain in the map and the method returns `True`.

**Trace a rejection**

Suppose `[10, 20)` and `[10, 40)` are already accepted. Between times 10 and 20, the running sweep count is two.

Tentatively adding `[5, 15)` contributes `+1` at 5 and `-1` at 15. During the ordered scan:

- From 5 to 10, the active count is one.
- At 10, the two existing starts raise it to three.

The method detects `s > 2`, reverses the new deltas at 5 and 15, and returns false. The two earlier bookings remain exactly as before.

By contrast, `[5, 10)` ends at the coordinate where the other events begin. Its `-1` at 10 combines with their positive deltas, so no segment receives coverage from all three. The half-open booking can be accepted.

**Why a prefix sum gives the exact overlap count**

Before a coordinate, every accepted event has contributed its start delta if it has begun, and its end delta if it has already ended. Summing these changes therefore adds one for exactly those events whose start has been crossed but whose end has not. Those are precisely the events active on the following time segment.

The count can change only at stored endpoints. If it never exceeds two while sweeping all endpoint coordinates, it cannot exceed two at any time between them because it is constant there.

**Why the complete operation is correct**

Assume the difference map represents all previously accepted bookings and its prefix sums never exceed two. Adding the two tentative deltas creates exactly the difference representation of the old bookings plus the requested one.

If any prefix exceeds two, some nonempty segment is covered by at least three events, so rejection is necessary; rollback restores the old valid state. If no prefix exceeds two, no time is triple booked, so retaining the deltas is safe. By induction across calls, the calendar accepts exactly the requests that preserve the no-triple-booking rule.

## Complexity detail

Let `M` be the number of distinct endpoint keys currently retained. Updating each of the two keys in a `SortedDict` costs `O(log M)`. The validation sweep visits all `M` ordered values, so one `book` call costs `O(M)` time overall.

After `q` calls, including failed calls whose zero-valued keys remain, `M <= 2q`. Thus one call is `O(q)` in the worst case and the full sequence of `q` calls is `O(q^2)`.

This is the complexity of the exact sweep implementation. A dynamic segment tree can achieve `O(log C)` per call over coordinate domain `C`, matching an `O(q log C)` campaign-style bound, but that data structure is not used by this source.

The sorted difference map stores at most two coordinates per call, so space is `O(q)`.

## Alternatives and edge cases

- **List of bookings plus double-overlap intervals:** Store all accepted events and separately store every region already covered twice. Reject a new event if it intersects a double-covered region; otherwise add its overlaps with existing events. This is intuitive and uses linear space, with linear work per call under the problem bounds.

- **Dynamic segment tree with lazy propagation:** Range-query the current maximum and range-add one only when safe. This gives `O(log C)` work per call and `O(q log C)` dynamic nodes, but implementation and rollback logic are more complex.

- **Recompute coverage from raw bookings:** Sorting all start and end events on every call also works, but rebuilding the events adds avoidable sorting work. The sorted difference map retains aggregated endpoints.

- **Forget rollback:** Leaving a rejected booking’s deltas in the map would corrupt all future decisions. Both endpoint changes must be reversed before returning false.

- **Zero delta keys after rollback:** They are harmless because adding zero changes no prefix sum. Deleting them would reduce the map size but is not required for correctness.

- **Touching intervals:** An end and a start at the same coordinate combine before the following segment is evaluated, respecting the half-open convention.

- **Double booking:** A running count of exactly two is allowed. Rejection occurs only for `s > 2`.

- **Repeated identical event:** The first two copies can be accepted because they produce coverage two; a third identical copy makes the prefix reach three and is rejected.

- **Sparse huge coordinates:** Storage depends on observed endpoints, not on the numeric size of the timeline.

- **Rejected call followed by another call:** The inverse deltas restore all coverage counts, so later results are as if the rejected request never existed.
