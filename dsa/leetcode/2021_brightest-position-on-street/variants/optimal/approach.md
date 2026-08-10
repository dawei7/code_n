## General

**Convert each inclusive interval into two events**

A lamp at position `i` with range `j` covers integer positions from

`l = i - j`

through

`r = i + j`,

both inclusive.

The difference map adds one at `l` and subtracts one at `r + 1`. The extra one is what preserves coverage at `r`: the lamp stops contributing only at the next integer position.

**Sweep coordinates in increasing order**

`s` is the brightness after applying all events at the current coordinate. Starting from zero, the loop visits sorted event keys and executes `s += d[k]`.

Between this event coordinate and the next one, brightness remains constant because no lamp begins or ends.

Only event coordinates need inspection. A new maximum brightness can first appear exactly where positive events are applied, not in the middle of an unchanged region.

**Preserve the smallest position on ties**

`mx` stores the greatest brightness seen. The source updates `ans=k` only when `mx < s`, a strict improvement.

Because event coordinates are processed from smallest to largest, the first coordinate attaining the global maximum is the smallest brightest position. Later equal values do not overwrite it.

**Trace the first example**

The lamp intervals are `[-5,-1]`, `[-1,3]`, and `[0,6]`. Events add at -5, -1, and zero, and subtract at zero, four, and seven respectively.

At -5, brightness becomes one and answer becomes -5. At -1, brightness becomes two and answer becomes -1. At zero, one lamp ends just as another begins, so the net brightness remains two. The strict update keeps -1, the smallest position with maximum brightness.

**Why simultaneous events must be combined**

`defaultdict(int)` accumulates all starts and ends at the same coordinate. Applying their net change together gives the correct brightness for that coordinate.

For inclusive integer intervals, an interval ending at $k-1$ contributes a negative event at $k$, while a new interval starting at $k$ contributes positive one there. Their sum correctly describes which lamps cover $k$.

Consider three changes at the same coordinate $k$: two lamps begin there and one lamp whose right endpoint is $k-1$ stops contributing. The event map stores a single net change of $+1$. If brightness immediately before $k$ was four, brightness at $k$ is therefore five. Processing the three changes in an arbitrary order and checking the maximum after each individual change could briefly report six, a brightness that never exists at any integer position. Combining equal-coordinate events before comparing avoids that false intermediate state.

**Why the returned coordinate is correct**

The difference prefix sum equals the number of intervals containing each integer coordinate. Every brightness change happens at a stored event.

The sweep observes each constant-brightness region at its smallest coordinate and records only strict global increases. Therefore `mx` becomes the maximum brightness and `ans` its smallest position.

More formally, just before an event coordinate $x$, `s` represents the brightness on the preceding constant segment. Adding `d[x]` removes every interval ending at $x-1$ and adds every interval beginning at $x$. It therefore makes `s` equal to the number of intervals containing $x$. No event occurs between $x$ and the next key, so that count remains unchanged throughout the gap. Inspecting $x$ consequently represents the entire following constant segment. Since every integer lies in one such represented segment, the sweep cannot miss a larger value.

**Initial zero values**

`ans=s=mx=0` might appear to bias the answer toward coordinate zero. However at least one lamp exists, and the first start event raises `s` to a positive value, causing `ans` to be replaced by that possibly negative coordinate. The initialization is safe.

**Discrete-coordinate assumption**

Using `r+1` expresses inclusive coverage on integer positions. It would not represent a continuous real line, where one would use an event just after $r$ conceptually. The problem's integer lamp positions and returned position align with this discrete sweep.

## Complexity detail

Let $N$ be number of lamps and $E\le2N$ distinct event coordinates. Building the map takes expected $O(N)$ time. Sorting keys costs $O(E\log E)=O(N\log N)$, and sweeping costs $O(E)$.

The event map and sorted keys use $O(N)$ space. Scalar brightness state uses $O(1)$.

The magnitude of a coordinate does not enter these bounds. A lamp might illuminate coordinates separated by hundreds of millions, yet it still contributes only two map entries. This is the key advantage over visiting every point in the illuminated span.

## Alternatives and edge cases

- **Explicitly visit every illuminated position:** Impossible when ranges span up to $10^8$; event compression avoids coordinate-range dependence.
- **Separate sorted start and end arrays:** A two-list sweep is possible, but difference events are simpler.
- **Use a heap of active intervals:** More machinery than needed when only counts and endpoints matter.
- **Zero range:** Produces +1 at the lamp position and -1 at the next integer.
- **Negative positions:** Sorted dictionary keys handle them naturally.
- **Several lamps start together:** Their positive changes accumulate.
- **One lamp ends where another starts:** Net event gives correct brightness and tie logic keeps the earliest maximum.
- **Long constant maximum interval:** Its left endpoint is recorded.
- **Several separated maximum regions:** Strict update keeps the first/smallest.
- **Inclusive right endpoint:** Requires subtraction at `r+1`, not `r`.
- **At least one lamp:** Ensures the zero answer initialization is replaced.
- **Input preservation:** The source builds a separate event map.
