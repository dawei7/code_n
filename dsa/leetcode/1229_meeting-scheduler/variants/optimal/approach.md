## General
**Put both schedules in chronological order.** Sort each list by interval start. Keeping sorted copies avoids changing the caller's inputs and makes the next possible overlap depend only on one current interval from each schedule.

**Measure the current intersection.** For intervals `[a, b]` and `[c, d]`, the shared portion begins at `max(a, c)` and ends at `min(b, d)`. If `end - start >= duration`, this is the earliest feasible overlap among all unprocessed slots, so return `[start, start + duration]` immediately.

**Discard the interval that ends first.** When the overlap is too short, whichever current interval has the smaller end cannot form a longer overlap with any later interval from the other sorted schedule: those later intervals start no earlier than the current opposing interval. Advance that interval's pointer; on equal ends, advancing either is safe.

Every interval discarded by this rule is proven unable to participate in a feasible earlier meeting. The pointers therefore examine all potentially useful pairs in chronological order, and the first returned intersection has the smallest possible start time. Exhausting either list proves no pair remains.

## Complexity detail
Sorting costs $O(n\log n+m\log m)$ time, and the two pointers advance at most $n+m$ times. The sorted copies occupy $O(n+m)$ space.

## Alternatives and edge cases
- **Compare every slot pair:** Testing all $nm$ intersections is correct but quadratic when both schedules are large.
- **Merge all endpoints:** A sweep-line event list can find common availability but uses more state than two pointers.
- **Touching endpoints:** An overlap of zero duration cannot host any positive `duration`.
- **Exact fit:** If `end - start == duration`, return that entire overlap.
- **Unsorted input:** Sorting is required before pointer advancement is valid.
- **Multiple feasible overlaps:** Return immediately at the first one in chronological pointer order.
- **No overlap:** Exhaustion of either schedule returns `[]`.
