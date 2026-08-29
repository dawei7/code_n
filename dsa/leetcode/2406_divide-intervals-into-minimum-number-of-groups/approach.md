## General

**View each group as one reusable resource**

Intervals within one group cannot intersect. After sorting by start, a group can accept the current interval only if the group's most recently assigned interval ends strictly before the current `left`.

Strict inequality is required because intervals are inclusive. End `5` and start `5` share the point five and therefore intersect.

The min-heap `q` stores one end time for each group created so far. Its smallest end identifies the group that becomes reusable earliest.

**Process intervals by starting point**

`sorted(intervals)` orders pairs first by `left` and then by `right`. When considering the next interval, all earlier-starting intervals have already been assigned.

If the minimum group end satisfies:

```python
q[0] < left
```

that group is free. The code pops its old end and pushes the current `right`, reusing the group.

If the earliest-ending group is not free, no other group can be free because every other heap end is at least `q[0]`. A new group is unavoidable, and pushing `right` increases heap size by one.

**Why only one free end is popped**

Several groups may have ends less than `left`. The current interval needs only one group, so the algorithm pops exactly one—specifically, the earliest-ending one—and updates it.

The other heap entries remain as records of other already-created, currently free groups. They are not stale intervals that must be removed; each heap entry represents the latest end assigned to one reusable group. A future interval can reuse them.

This is why returning `len(q)` is meaningful: heap size is the number of groups allocated, not the number of intervals currently intersecting the final processed point.

**Why reusing the earliest-ending group is safe**

If any group is available, assigning the current interval to the one with smallest end preserves groups with later ends for future use. In this problem, any available group would keep the same group count, but selecting the heap minimum provides a consistent exchange-safe policy.

More importantly, the heap minimum test decides whether *some* group is available. If even the smallest end intersects the current start, every existing group does.

**Trace an inclusive endpoint**

Suppose one group ends at five and the next interval begins at five. The test `5 < 5` is false, so a new group is created. This matches the definition that `[1,5]` and `[5,8]` intersect.

If the next interval begins at six, `5 < 6` is true and the same group can be reused.

**Why the greedy group count is minimal**

Whenever the algorithm creates a new group for interval `[left,right]`, every existing group's last interval ends at or after `left`. Those intervals all intersect the current interval at its start or later. Therefore, the current interval and one active interval from each existing group overlap at point `left`, demonstrating that at least one more group is necessary.

Whenever a group is reusable, assigning the interval there does not create an intersection and avoids increasing the count.

Thus, every increase is forced by a simultaneous-overlap lower bound, and every non-increase is feasible. The final number of groups is minimal.

**Relationship to maximum overlap**

For intervals on a line, the minimum number of nonintersecting groups equals the maximum number of intervals sharing any point. Each such overlapping set needs separate groups. The heap algorithm realizes a coloring using exactly that many resources.

**Input preservation**

The code calls `sorted(intervals)` rather than `intervals.sort()`, so it creates a sorted list and leaves the caller's input ordering unchanged.

## Complexity detail

Let $n$ be the number of intervals. Sorting takes $O(n\log n)$ time. Each interval causes one heap push and at most one pop, each $O(\log n)$ in the worst case. Total time is $O(n\log n)$.

The sorted copy and heap can each contain $O(n)$ interval information/endpoints, so auxiliary space is $O(n)$.

The heap size grows only when a new group is forced and never shrinks permanently when a group is reused, making its final length the answer.

## Alternatives and edge cases

- **Line sweep with endpoint events:** Add one at starts and subtract after inclusive ends, then take maximum overlap. It also solves the problem in $O(n\log n)$.
- **Difference array:** With endpoints bounded by `10^6`, mark starts and `right + 1` removals, then scan the domain. This costs $O(n+V)$ time and $O(V)$ space.
- **Pop all free groups:** Unnecessary and would lose the one-entry-per-created-group representation unless their availability were stored elsewhere.
- **Touching endpoints:** Inclusive intervals intersect, so reuse needs `end < start`, not `end <= start`.
- **All intervals disjoint:** One heap entry is repeatedly reused and answer is one.
- **All intervals share a point:** No group is reusable during their starts, so answer is `n`.
- **Identical intervals:** Each requires a separate group.
- **One interval:** One group is created and returned.
- **Sorted copy:** The original input list is not reordered.
