## General

**Each lamp contributes one to an inclusive interval**

A lamp at position `p` with range `r` illuminates from

`i = max(0, p - r)`

through

`j = min(n - 1, p + r)`,

including both endpoints. The brightness at a street position is the number of these intervals covering it.

Incrementing every position in every lamp interval would be too slow when both the street and number of lamps are large. The solution records only where each interval's contribution begins and where it stops, using a difference array.

**Represent an interval with two events**

The list `d` has length `n + 1`. For one inclusive interval `[i, j]`, the code performs:

- `d[i] += 1` to begin one additional active lamp;
- `d[j + 1] -= 1` to end that contribution immediately after `j`.

When cumulative sums are later taken, the added one remains active from `i` through `j`. At `j + 1`, the subtraction cancels it.

The extra sentinel position at index `n` makes `j + 1` valid even when `j = n - 1`. Without that slot, a lamp reaching the street's final position would require a separate branch.

**Clipping preserves the finite street**

`max(0, p - r)` prevents a lamp's mathematical range from extending below position zero. `min(n - 1, p + r)` prevents it from extending beyond the last street position.

Only clipped endpoints create events. Light outside the represented street contributes to no requested brightness and should not occupy any array position.

**Prefix sums recover exact brightness**

`accumulate(d)` lazily produces cumulative totals. At position `q`, that total is

$$
\sum_{t=0}^{q} d[t].
$$

Every lamp whose start is at or before `q` has added one. A lamp whose interval ended before `q` has also contributed its negative event and canceled out. Lamps covering `q` have started but not ended. Therefore, the cumulative value is exactly the number of lamps illuminating `q`.

This is the central difference-array invariant: point events become range coverage after a prefix sum.

**Compare brightness with each requirement**

The return expression pairs cumulative brightness values with `requirement`:

`zip(accumulate(d), requirement)`.

Although `accumulate(d)` can produce `n + 1` values, `requirement` has length `n`. `zip` stops when the shorter iterable ends, so the sentinel cumulative value at index `n` is ignored automatically.

For each pair `s, r`, the Boolean `s >= r` is true exactly when that street position meets its minimum brightness. In Python, Booleans behave as integers one and zero in `sum`. Consequently,

`sum(s >= r for s, r in ...)`

counts the passing positions.

The loop variable `r` inside this generator represents a requirement value. It is separate from the lamp-range variable `r` used in the earlier loop; the earlier loop has already finished.

**Why every lamp is counted at every correct position**

For a lamp interval `[i, j]`, its start event contributes one to every prefix sum from `i` onward. Its end event at `j + 1` removes that one from all later prefix sums. Thus, its net contribution is one exactly for indices `i <= q <= j` and zero elsewhere.

Difference events from multiple lamps add linearly, so the prefix total is the sum of all individual zero-or-one coverage contributions. That sum is the brightness definition.

The final comparison includes equality, matching “at least.” A position with requirement zero always passes because brightness cannot be negative.

**Trace the event idea**

For an interval `[1, 3]`, add one at `d[1]` and subtract one at `d[4]`. Prefix totals gain one at positions one, two, and three, then return to the earlier level at four.

If another interval covers `[0, 1]`, its events overlap. Prefix totals at position one include both start contributions, correctly producing brightness two.

**Input behavior**

The method does not modify `lights` or `requirement`. It allocates `d` as its working representation. `accumulate` and the generator are lazy and do not create another length-`n` brightness list.

## Complexity detail

Let `m = len(lights)`. Processing each lamp performs constant endpoint and event work, taking `O(m)` time. The cumulative scan and requirement comparisons process `n` positions, taking `O(n)` time. Total time is `O(n + m)`.

The difference array has `n + 1` integers and therefore uses `O(n)` space. The lazy iterators and scalar loop values use `O(1)` additional space.

The count and brightness values are at most `m` and fit safely in Python integers.

## Alternatives and edge cases

- **Increment every illuminated position per lamp:** This direct simulation can take `O(nm)` time when many lamps cover most of the street.
- **Sweep sorted interval endpoints:** A general event map can work, but positions are already a dense range from zero to `n - 1`, making an array simpler.
- **Segment tree:** Range additions and point queries are supported, but all updates occur before one full scan, so a difference array is lighter and faster.
- **Lamp with zero range:** It creates events at `p` and `p + 1` and contributes only at its own position.
- **Lamp covering the entire street:** Its clipped interval is `[0, n - 1]` and its negative event uses sentinel index `n`.
- **Position requirement zero:** It always passes, even with no covering lamp.
- **Brightness exactly equal to requirement:** `>=` includes the position.
- **Overlapping lamps:** Their event contributions add, producing the correct larger brightness.
- **Street length one:** Events use indices zero and one; `zip` evaluates only position zero.
- **Range extending left or right:** Endpoint clipping prevents invalid indices without losing any on-street illumination.
- **Sentinel value:** It is needed to terminate final-position intervals but is intentionally not paired with a requirement.
- **Input preservation:** Neither source array is changed.
