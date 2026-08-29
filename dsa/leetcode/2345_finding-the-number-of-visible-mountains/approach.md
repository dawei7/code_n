## General

**Transform each mountain into a base interval**

A mountain with peak `(x, y)` and slopes 1 and -1 reaches the x-axis at

`x - y` and `x + y`.

Represent it by interval `(l, r) = (x-y, x+y)`.

This transformation turns geometric containment into interval containment. A peak `(x_1,y_1)` lies inside or on mountain `(x_2,y_2)` exactly when

`x_2-y_2 <= x_1-y_1` and `x_1+y_1 <= x_2+y_2`.

In interval terms, the first mountain's interval is contained in the second's interval. Therefore a mountain is invisible when some other interval contains its interval.

**Count duplicates before scanning**

`cnt = Counter(arr)` records how many mountains have each identical interval.

Two identical peaks produce identical mountains. Each peak lies on or inside the other mountain, so neither copy is visible. Even if their interval is not contained by a larger interval, a duplicated interval must contribute zero to the answer.

The Counter lets the scan distinguish a unique exposed interval from overlapping duplicate mountains.

**Sort possible containers before contained intervals**

The array is sorted by increasing left endpoint and, for equal left endpoints, decreasing right endpoint:

`(l ascending, r descending)`.

A containing interval must start no later and end no earlier than the contained interval. Increasing `l` ensures any possible earlier-starting container is processed first. Decreasing `r` for equal left endpoints ensures the widest interval is processed before narrower intervals sharing that start.

Without the descending tie rule, a narrow interval might temporarily look visible before its equal-left wider container is encountered.

**Track the farthest right endpoint already covered**

`cur` is the greatest right endpoint among intervals processed so far. It begins at negative infinity.

For current `(l,r)`:

- if `r <= cur`, some earlier interval starts at or before `l` and ends at or after `r`, so the current mountain is contained and invisible;
- if `r > cur`, no prior interval contains it, so it establishes a new farthest reach and `cur` becomes `r`.

In the second case, the mountain is counted only if `cnt[(l,r)] == 1`. A unique interval whose right endpoint exceeds all earlier endpoints is visible. Duplicate copies establish coverage but do not count.

**Why one scalar is enough**

All earlier intervals have left endpoints no greater than the current one. Among them, only the maximum right endpoint matters for containment. If even the farthest prior endpoint is smaller than `r`, none contains the current interval. If it is at least `r`, the interval achieving `cur` does contain it.

There is no need to retain every earlier interval for the decision.

**Why every counted mountain is visible**

A counted interval has `r > cur` before its update, so no earlier interval contains it. A later interval cannot contain it because later intervals start at `l' >= l`. If `l' > l`, it starts too late; if `l' = l`, descending-right sorting would have placed any interval with `r' >= r` earlier.

It is also unique, so no identical mountain hides it. Hence its peak lies in no other mountain.

Every uncounted interval is either covered by a prior interval or duplicated, both of which make its peak nonvisible. The scan is exact.

## Complexity detail

Let `n` be the number of peaks. Building intervals and the Counter takes `O(n)` expected time. Sorting costs `O(n \log n)`, and the final scan is `O(n)`. Total time is `O(n \log n)`.

The interval list and Counter each store up to `n` entries, giving `O(n)` auxiliary space. Python sorting may also use linear temporary storage.

The input `peaks` is not modified; `arr` is a new list. Endpoint values can be negative on the left, which ordinary integer sorting handles.

## Alternatives and edge cases

- **Compare every pair of mountains:** Direct geometric containment is easy to state but costs `O(n^2)`.
- **Sweep with explicit interval stack:** A stack can retain nested intervals, but the farthest-right scalar already decides containment after the chosen sort.
- **Sort right endpoints ascending on equal left:** This can process contained intervals before their container and count incorrectly.
- **Ignore duplicate counts:** The first of two identical mountains might be counted even though each hides the other.
- **One mountain:** Its interval is unique and uncovered, so the answer is one.
- **Two identical peaks:** The Counter is two; neither is counted.
- **Same left endpoint, different right endpoints:** The widest comes first and hides every narrower one.
- **Same right endpoint, later left endpoint:** The later interval is contained because `r <= cur`.
- **Touching border:** Containment uses non-strict inequalities, so `r == cur` is invisible as required.
- **Overlapping without containment:** If the current interval extends farther right, it remains visible even when its bases overlap.
- **Negative left endpoint:** Mountains may extend left of zero in coordinates; interval arithmetic remains valid.
- **A duplicate interval contained by a larger one:** It is invisible for both reasons; the scan skips it through coverage.
- **Input preservation:** Only transformed interval storage is sorted.
