## General

**Feasibility is monotone in speed.** At speed `v`, ride `d` takes `d / v` hours. Increasing speed never increases any ride time or any rounded departure time. Therefore speeds form a false-then-true sequence: small speeds may miss the deadline, and once one speed succeeds, every larger speed also succeeds. Binary search can find the first true speed.

**Calculate exact commute time for one speed.** Helper `check(v)` scans rides in order. For every ride except the last, it adds `ceil(d / v)` because the next train cannot depart until an integer hour. For the last ride, it adds the exact fractional `d / v` because arrival at the office does not need to be rounded to another departure.

The helper returns whether total `s` is at most `hour`. Equality is accepted because arriving exactly on time is valid.

**Reject schedules with too little time even at infinite speed.** Before searching, the code checks:

`len(dist) > ceil(hour)`.

The first `n - 1` rides each force departure onto successive integer-hour boundaries. Even as travel times approach zero, the final train cannot effectively finish within a deadline at or below `n - 1`. With hour having at most two decimals, this condition identifies the impossible timing structure used by the standard solution.

For `n = 3` and `hour = 1.9`, `ceil(hour) = 2` and three is greater than two, so minus one is returned immediately.

**Search speeds one through ten million with Python’s keyed bisection.** `r = 10**7 + 1` is one beyond the promised maximum answer. `range(1, r)` contains candidate speeds one through ten million.

`bisect_left(range(1, r), True, key=check)` conceptually applies `check` to probed speeds. Booleans order as false before true, so keyed lower bound finds the first candidate whose check result is `True`. Only logarithmically many candidates are evaluated; the range itself is lazy and does not allocate ten million integers.

The returned bisection position is zero-based within a range beginning at speed one, so `+ 1` converts it to the actual speed.

If no candidate succeeds, bisection returns the range length ten million. Adding one gives `r`, and the final conditional returns minus one. Otherwise, `ans` is the first feasible speed and therefore the required minimum.

**Trace the fractional sample.** At speed three, rounded times for the first rides are one and one, while the last ride takes two-thirds. Total time is about 2.6667, which fits 2.7. Speed two takes rounded first portions one and two plus a final one, so it fails. The false-to-true boundary is therefore speed three.
`check` exactly implements waiting rules for a fixed speed. Travel and rounded times are non-increasing as speed rises, establishing monotonicity. Lower-bound bisection returns the first feasible candidate in the promised search domain. The preliminary impossible check handles deadlines that no finite speed can satisfy, and the sentinel handles absence of a feasible promised-domain speed.

**Why keyed bisection returns a position rather than a speed.** The searched sequence is the range of actual speed values, but `bisect_left` reports an index into that sequence. Range index zero contains speed one, index one contains speed two, and so on. Adding one is therefore not an arbitrary adjustment; it is the exact index-to-value conversion.

The monotonic Boolean view can be imagined as `[False, False, ..., True, True]`. Lower bound for `True` identifies the first successful check. If every entry is false, the insertion point lies just after the sequence, producing the sentinel.

**Floating-point detail.** The exact code uses Python floating division and `ceil`. The test constraints limit `hour` to two decimal places and the implementation is the checked-in behavior. An integer-scaled or rational comparison could avoid floating-point boundary concerns, but is not used here.

## Complexity detail

Let `N` be the number of rides and `U = 10^7` the speed bound. Binary search performs `O(log U)` checks, each scanning `N` distances. Total time is `O(N log U)`.

`range` is lazy, and `check` uses only scalar variables. Auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Manual binary search:** It expresses the same monotone search without relying on the keyed `bisect_left` API.
- **Linear speed scan:** Trying every speed can require ten million full commute scans.
- **Integer-scaled timing:** With at most two decimal digits, careful integer arithmetic can reduce floating-point risk, though ceiling terms remain important.
- **One train:** No waiting-rounding term exists; only its exact travel time matters.
- **Exact integer ride time:** `ceil` leaves it unchanged.
- **Fractional early ride:** It rounds upward to the next integer departure hour.
- **Fractional last ride:** It is not rounded because the journey ends there.
- **Arrival exactly at `hour`:** `<=` accepts it.
- **Impossible departure structure:** The preliminary length-versus-ceiling test returns minus one early.
- **Answer at ten million:** It is included because the range ends just before `10^7 + 1`.
- **No feasible bounded speed:** The sentinel answer equals `r` and maps to minus one.
- **Lazy search domain:** Creating `range` uses constant space despite its numeric size.
- **Monotone rounded terms:** `ceil(d / v)` cannot increase when `v` increases, so waiting rules do not break binary-search monotonicity.
- **Large allowed hour:** Speed one may already pass, and lower bound correctly returns range index zero plus one.
- **Preliminary rejection versus sentinel:** The first detects a structural timing impossibility; the sentinel handles a failed bounded search even when that quick condition does not fire.
- **Check scans all rides:** The exact helper has no early return when accumulated time exceeds `hour`, so every probe remains `O(N)`.
