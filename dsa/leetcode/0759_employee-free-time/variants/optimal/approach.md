## General

**Common free time is the gap between merged busy intervals**

At a time when any employee is working, the group is not commonly free. Therefore first compute the union of every employee’s busy intervals. The finite positive gaps between consecutive components of that union are exactly the times when everyone is free.

The exact solution flattens all employee schedules into one list, sorts it, merges it, and extracts gaps.

**Flattening is valid**

Individual employee identity no longer matters after asking whether at least one person is busy. Every interval contributes to the global busy union in the same way.

The input guarantee that each employee’s own schedule is sorted and nonoverlapping is useful source structure, but the solution does not depend on preserving it. Flattening and globally sorting handles overlaps between different employees.

**Sort by start and then end**

Intervals are ordered by `(start, end)`. When scanning in this order, any interval that can overlap the current merged component appears before intervals that begin farther right.

`merged` starts with the earliest interval. For each next interval `x`:

- If `merged[-1].end < x.start`, a positive gap exists, so `x` starts a new merged component.
- Otherwise the intervals overlap or touch, so the current component’s end becomes the larger end.

Touching intervals are merged. If one ends at time five and another begins at five, the gap `[5, 5]` has zero length and must not be returned.

**Why merging takes the maximum end**

An interval may be completely contained in the current busy component. Replacing the end directly with `x.end` could shrink the union. Using `max` preserves the farthest busy endpoint reached so far.

**The merge invariant**

Before each new interval is processed, `merged` is the exact busy union of all earlier sorted intervals, expressed as disjoint chronological components. The final component is the only one the next interval can possibly touch because all previous components end even earlier.

A strict gap appends a new component. An overlap or endpoint touch extends only the final component. Both actions preserve the invariant, which is why one left-to-right pass is sufficient.

**Extract only finite gaps**

After merging, consecutive components `a` and `b` satisfy `a.end < b.start`. The interval `[a.end, b.start]` has positive length, and no busy interval covers its interior. It is therefore common free time.

`pairwise(merged)` visits every consecutive component pair and creates one `Interval(a.end, b.start)`.

The unbounded time before the first busy component and after the last is not represented because the problem requests finite intervals. Only internal gaps are returned.

**Trace the first example**

Flattened busy intervals include `[1,2]`, `[5,6]`, `[1,3]`, and `[4,10]`. Sorting and merging produces busy components `[1,3]` and `[4,10]`.

Their only internal gap is `[3,4]`, which is returned. The infinite outer free regions are intentionally omitted.

**Why the result is sorted**

Merged components are constructed chronologically. Their consecutive gaps therefore also appear in increasing time order, satisfying the output ordering without another sort.

Every constructed gap has positive length because components were separated only when `previous_end < next_start`. This prevents forbidden intervals such as `[5, 5]` without requiring a later filtering pass.

**Input-object mutation**

The merge list stores references to original `Interval` objects. Extending `merged[-1].end` can mutate an interval inside the supplied schedule. This does not affect the returned mathematical result, but callers should know the exact implementation is not purely read-only.


The sorted merge produces exactly the union of all busy intervals: overlapping or touching intervals form one continuous unavailable component, while a strict separation begins another. A time is commonly free precisely when it lies outside this union.

Every finite positive outside segment lies between two consecutive merged components, and every such gap contains no busy time. Constructing those gaps gives all and only the required common free intervals.

## Complexity detail

Let `N` be the total number of busy intervals across employees. Flattening costs `O(N)`, sorting costs `O(N log N)`, and merging plus gap extraction costs `O(N)`. Total time is `O(N log N)`.

The flattened list, merged references, and returned gaps use `O(N)` space in the worst case. Python sorting may also use linear temporary storage.

## Alternatives and edge cases

- **K-way merge employee schedules:** Because each individual schedule is sorted, a heap can merge them before union processing. This avoids one global sort but adds heap logic.

- **Sweep-line endpoints:** Track active employee intervals through start and end events. It works but is more machinery than merging their union.

- **Keep touching intervals separate:** That would emit a zero-length free interval, which is forbidden.

- **Contained interval:** The merged end must not shrink; use the maximum.

- **Only one merged busy component:** There is no finite internal common free time, so the result is empty.

- **Outer free time:** Infinite intervals before and after all work are deliberately omitted.

- **Object mutation:** Copy intervals first if the original schedules must remain unchanged.

- **Nonempty schedules:** The contract ensures the flattened list has a first interval for initialization.
