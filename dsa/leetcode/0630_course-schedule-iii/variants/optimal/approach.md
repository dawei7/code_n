## General

**Process deadlines from earliest to latest.** The first greedy decision is `courses.sort(key=lambda x: x[1])`. If two chosen courses have deadlines `d_1 <= d_2`, placing the earlier-deadline course first is never worse: it gives the more constrained course its chance to finish early, while the later-deadline course still has at least as much allowed time. Repeated adjacent exchanges can transform any feasible chosen schedule into nondecreasing deadline order.

Once courses are in that order, the scan only needs to decide which durations to retain.

**Track a candidate set and its total duration.** `pq` contains the durations of currently selected courses. Python provides a min-heap, so the source pushes `-duration`. The most negative number represents the largest positive duration, making `heappop(pq)` remove the longest selected course.

`s` is the sum of all positive durations represented in the heap. For each sorted pair `(duration, last)`, the method first tentatively selects the course:

- push `-duration`;
- add `duration` to `s`.

If `s <= last`, all selected courses can be taken in deadline order through the current course. Nothing must be removed.

**When the deadline is exceeded, discard the longest duration.** If `s > last`, the tentative set cannot fit by the current deadline. The best way to keep as many courses as possible while freeing time for future deadlines is to remove the selected course with maximum duration. That saves at least as much time as removing any other single course.

Because the heap stores negatives, the statement

`s += heappop(pq)`

adds a negative duration, which is equivalent to subtracting the longest positive duration.

The source writes this inside `while s > last`. Under the maintained invariant, one removal is sufficient. Before adding the current course, the old total was feasible for an earlier or equal deadline. If the current course itself is longest, removing it restores the old total. If an older course is longest, replacing that longer duration with the current shorter duration makes the new total no greater than the old feasible total. The loop form is nevertheless robust and directly states “restore feasibility.”

**Why replacement does not reduce the course count unnecessarily.** Tentatively adding and then removing one course leaves the heap size unchanged. The removed course may be the current one, meaning it was simply rejected, or it may be an older longer course, meaning the current course replaces it. A replacement preserves the number selected but reduces total occupied time, giving later courses more room.

For example, suppose selected durations total 12 and a new duration 4 misses its deadline when added, producing 16. If the heap's longest duration is 7, replacing 7 with 4 reduces total time to 9 while keeping the same number of courses. Keeping the shorter set can never hurt any later deadline.

**The core greedy invariant.** After each sorted prefix, the heap represents:

1. a feasible set with the maximum possible number of courses from that prefix; and
2. among maximum-cardinality feasible choices, one with minimum total duration.

When the new course fits, adding it increases cardinality by one, which is obviously best. When it does not fit, no set of the old maximum size plus the new course can beat the shortest-duration representative if even that total exceeds the deadline. Removing the longest duration gives the smallest total obtainable by deleting one member from the tentative set, so it preserves maximum achievable cardinality and the strongest state for future courses.

By induction over all deadline-sorted courses, the final heap size is the maximum number that can be completed.

**Trace the standard sample.** Sorting by last day gives `[100,200]`, `[1000,1250]`, `[200,1300]`, `[2000,3200]`.

- Select 100; total 100 is feasible by day 200.
- Select 1000; total 1100 is feasible by day 1250.
- Select 200; total 1300 is feasible by day 1300.
- Tentatively select 2000; total 3300 exceeds 3200. The longest duration is 2000 itself, so it is popped and total returns to 1300.

Three courses remain.

The method returns only `len(pq)` because the problem asks for the maximum count, not the course identities or schedule.

## Complexity detail

Let $C$ be the number of courses. Sorting by deadline costs $O(C\log C)$. Every course is pushed once, and every pushed duration is popped at most once. Each heap operation costs $O(\log C)$, so the complete scan is $O(C\log C)$.

The heap can hold at most $C$ durations, requiring $O(C)$ auxiliary space. Python's in-place sort may also use up to $O(C)$ temporary workspace. The source mutates the order of the input `courses` list. These bounds match the manifest.

`s` can reach the sum of durations; Python integers avoid overflow. In fixed-width languages, use a sufficiently wide integer type.

## Alternatives and edge cases

- **Dynamic programming by time:** Sort deadlines and choose or skip each course using elapsed time as state. It is much more expensive when deadlines are large.
- **Linear search for the longest selected course:** It preserves the greedy idea but can make the scan quadratic; the heap supplies the longest duration efficiently.
- **Course longer than its own deadline:** It is pushed, immediately becomes infeasible, and is removed if no even longer selected course is a better replacement.
- **One course:** It remains only when its duration does not exceed its last day.
- **Equal deadlines:** Their relative sort order is unimportant because the heap replacement rule chooses the shortest useful collection.
- **Equal durations:** Any tied longest course may be removed; total duration and future feasibility are identical.
- **Current course removed:** This is the ordinary rejection case and restores the previous feasible set.
- **Earlier course removed:** This is a beneficial replacement that preserves count and reduces total time.
- **Input mutation:** `sort` reorders `courses`. Copy first if callers require the original order.
- **Continuous scheduling:** There is no benefit to idle time before a selected course; placing chosen courses back-to-back in deadline order minimizes every completion time.
- **Heap sign convention:** Values are negative only to simulate a max-heap. Adding a popped heap value to `s` subtracts the corresponding duration.
