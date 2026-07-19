## General
**Treating the next rain as a deadline**

Once a lake is full, it needs drying only if it will rain there again. Its next rain day is a deadline: the lake must be emptied on some zero day strictly before that date. When several full lakes need drying, the one with the earliest deadline is the most urgent.

Precompute a queue of rain indices for every lake. As the scan reaches a rainy day, remove that current index from the lake's queue; the new queue front, if one exists, is its next deadline.

**Tracking which lakes are currently full**

Maintain a set `full`. On a positive day, the answer is `-1`. If the lake is already in `full`, it was not dried since its preceding rain, so flooding is unavoidable and the algorithm returns `[]`.

Otherwise add the lake to `full`. If its occurrence queue still has a future index, record that index as the lake's current deadline and push `(deadline, lake)` into a min-heap.

**Using each dry day for the earliest live deadline**

On a zero day, remove stale heap entries until the top describes a lake that is still full and whose recorded current deadline equals the heap entry. If a live entry remains, pop it, dry that lake, remove it from `full`, and write its identifier into the answer.

If no full lake has another scheduled rain, drying is unconstrained. Write any positive identifier, such as `1`; drying an empty lake is explicitly allowed.

**Why stale-entry validation is necessary**

Heap deletion is lazy. A lake may be scheduled, dried before its deadline, filled again on a later rainy day, and receive a new deadline. Its old heap entry can remain. Checking both membership in `full` and equality with the lake's recorded deadline prevents an obsolete entry from drying a newly filled incarnation for the wrong reason.

**Why earliest deadline first is safe**

Consider any valid completion that uses the current dry day for lake $b$ while another full lake $a$ has an earlier next-rain deadline. Exchange the choices: dry $a$ now and dry $b$ on the day that the completion used for $a$. The latter day occurs before $a$'s earlier deadline and therefore also before $b$'s later deadline. Both lakes remain safe.

Repeated exchanges transform a valid schedule into one that always dries the earliest-deadline lake. Thus, if the greedy scan later finds rain on a full lake, no alternative assignment of earlier dry days could have prevented that flood.

**Why the returned schedule is valid**

Every rainy position is marked `-1`. A lake leaves `full` only when a zero day explicitly dries it, so encountering it already in the set exactly detects a flood. Every chosen urgent lake is full at that moment and is dried before its recorded next rain. Arbitrary choices occur only when no currently full lake has a future deadline, so they cannot endanger feasibility.

## Complexity detail
Building all future-occurrence queues takes $O(N)$ time and space. Each rainy occurrence creates at most one heap entry, and every entry is pushed and popped at most once. Heap operations cost $O(\log N)$, giving $O(N \log N)$ total time. The queues, full set, deadline map, heap, and answer use $O(N)$ space.

## Alternatives and edge cases
- **Ordered dry-day set:** Scan rain days forward, remember each lake's previous rain, and allocate the earliest unused zero day after it. With a balanced ordered set this also takes $O(N \log N)$ time.
- **Python sorted list of dry days:** Binary search finds a suitable day, but deleting it shifts later elements and can make total time $O(N^2)$.
- **Restart a linear dry-day search:** It is correct but repeatedly scans unusable old zero days and fails to scale.
- **Dry an arbitrary full lake:** This can consume the only available day for a lake with a later deadline while an earlier deadline floods.
- **No repeated rain:** No urgent deadline exists; all rainy outputs are `-1`.
- **All zero days:** Any positive drying identifiers form a valid result.
- **Dry day before a lake fills:** It cannot protect that lake from two later rains.
- **One lake repeated:** At least one zero day must occur between every consecutive pair of its rain days.
- **Competing deadlines:** The earliest next rain determines the correct greedy choice.
- **Unused dry day:** Drying an empty lake is allowed and does not invalidate the schedule.
- **Large lake identifiers:** Maps and sets are keyed by identifier; the country need not allocate storage for all $10^9$ possible lakes.
- **Multiple valid outputs:** Correctness is determined by simulation, not equality with one sample schedule.
- **Impossible result:** Only `[]` signals that every schedule floods.
