## General

**Process intervals by the earliest deadline**

Every interval must contain at least two selected integers. A greedy choice should place new integers as far right as possible, because rightmost points satisfy the current interval while having the best chance of also lying inside later intervals.

The solution sorts intervals by increasing end. When ends are equal, it sorts by decreasing start, so the narrower interval is handled first. Points chosen for that narrower interval also work for every same-end interval that begins earlier.

**Track only the two most recently selected points**

The variables `s` and `e` are the second-largest and largest selected integers, with `s <= e`. They begin at `-1` because all interval starts are nonnegative.

The greedy algorithm always adds points at the current right endpoint or immediately before it. Since interval ends are processed nondecreasingly, all newly selected points are at least as far right as earlier useful points.

For current interval `[a, b]`, only three cases exist.

**Case one: both recent points already lie inside**

If `a <= s`, then both `s` and `e` are at least `a`. They are also at most `b` because they were selected at endpoints no later than the current sorted endpoint.

The interval already contains two selected integers, so nothing is added.

**Case two: no selected point lies inside**

If `a > e`, even the largest selected point is left of the interval. Every older point is smaller still, so the interval currently contains none.

Two new points are mandatory. The solution chooses `b - 1` and `b`, the two farthest-right distinct integers available. It increases the answer by two and assigns

`s, e = b - 1, b`.

The constraint `a < b` guarantees both integers lie inside the interval.

**Case three: exactly one recent point lies inside**

The remaining condition is `s < a <= e`. The largest selected point `e` lies inside, while `s` and all older points lie before `a`. Exactly one additional integer is necessary.

The best choice is the farthest-right point `b`. The two latest selected points become the old `e` and new `b`:

`s, e = e, b`.

The answer increases by one.

**Why older selected points never need inspection**

If `a <= s`, the last two already prove coverage. If `a > s`, every point older than `s` is no larger than `s` and therefore lies outside the interval as well. The last two points contain all information needed for the three cases.

**Why rightmost choices are safe**

Any later interval has an end at least `b`. Among points that can satisfy the current interval, larger points are never less likely to fit a later interval whose start may move right. Replacing a newly required point with a farther-right legal point cannot reduce coverage of future intervals.

When two points are needed, `b - 1` and `b` are the lexicographically farthest-right pair. When one is needed, `b` is the farthest-right possible choice.

**Why the tie order matters**

Consider two intervals with the same end but different starts. The one with the larger start is more restrictive. Processing it first ensures chosen rightmost points lie in both it and the wider same-end interval.

If the wider interval were processed first, its state might appear satisfied by an older point that lies before the narrower interval’s start, forcing less clean reasoning and potentially poor choices. Sorting starts descending removes that problem.


At each interval, the algorithm adds exactly the number of points missing from its intersection with the chosen set: zero, one, or two. Any valid solution must add at least that many relative to the already fixed earlier choices.

The added points are the farthest-right legal ones, so an exchange argument can replace the corresponding new points of any optimal solution with the greedy choices without harming the current or any later interval. Induction through the sorted intervals proves the algorithm retains an optimal-size partial solution at every step. The final count is therefore minimum.

## Complexity detail

Let `n` be the number of intervals. Sorting costs `O(n log n)` time, and the single greedy pass costs `O(n)`. Total time is `O(n log n)`.

The explicit greedy state uses `O(1)` space. Python’s in-place sort may use `O(n)` temporary memory in the worst case, so the implementation-level auxiliary bound is `O(n)`. The interval list is reordered.

## Alternatives and edge cases

- **Store the complete selected set:** It is unnecessary; only the two greatest selected points can matter for a later interval under the sorted order.

- **Choose leftmost missing points:** They satisfy the current interval but are less reusable by intervals starting farther right.

- **Sort only by start:** This loses the earliest-deadline greedy structure and does not justify rightmost selections.

- **Same endpoints:** Larger starts must be processed first.

- **Disjoint intervals:** Each new interval adds two points.

- **Already covered interval:** When `a <= s`, both latest points lie inside and the count remains unchanged.

- **Exactly one covered point:** The middle case adds only `b`, not two redundant points.

- **Shortest legal interval:** Since `a < b`, it contains at least the two distinct integers `a` and `b`.
