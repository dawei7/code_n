## General

**Record only where the active color set changes**

Between two consecutive segment endpoints, no segment begins or ends. The set of active colors, and therefore its sum, is constant throughout that interval. This makes a sweep over endpoints sufficient; inspecting every coordinate is unnecessary.

For each half-open segment `[l, r)` with color `c`, the solution records `d[l] += c` and `d[r] -= c`. Adding at `l` includes the color from that coordinate onward. Subtracting at `r` removes it before the interval beginning at `r`, exactly matching half-open semantics.

Several events may share a coordinate. `defaultdict(int)` combines their signed changes, so all starts and ends at that location take effect together.

**Sort events and form prefix sums**

The dictionary is converted to pairs `[coordinate, delta]` and sorted by coordinate. The loop changes each delta into a cumulative active-color sum:

`s[i][1] += s[i - 1][1]`.

After this prefix computation, `s[i][1]` is the sum of all colors active on the interval from `s[i][0]` up to, but not including, the next event coordinate `s[i + 1][0]`.

The result comprehension emits exactly that interval and sum when the sum is nonzero. A zero sum denotes an unpainted gap because all color values are positive, so excluding it correctly removes unpainted regions.

For segments `[1, 4, 5]` and `[1, 7, 7]`, the event deltas are $+12$ at one, $-5$ at four, and $-7$ at seven. Prefix sums give 12 on `[1, 4)` and 7 on `[4, 7)`.

**Why endpoint boundaries must be preserved even when sums match**

The mixed color is conceptually a set, but only its sum is output. Different color sets can have the same sum. If one set ends and another equal-sum set begins at the same coordinate, combining the adjacent pieces would be incorrect even though their numeric `mix` values match.

The exact solution does not merge adjacent output intervals merely because their sums are equal. Every distinct input endpoint remains in `s`, even if its net numeric delta is zero. Therefore a change from colors `{5,7}` to `{1,11}` retains the boundary although both sums are 12.

This works with the unique-color guarantee. Every start or end changes the active set, and recording all endpoint coordinates preserves those changes. The prefix value supplies the requested sum without pretending that the sum uniquely identifies the set.

**Why the sweep is correct and minimal**

On any open span between consecutive sorted endpoints, the active segment set cannot change, so one output segment is sufficient if that span is painted. At an endpoint, at least one color begins or ends, so the underlying mixed-color set changes. Such a boundary cannot be crossed by one valid descriptive segment, even when the old and new sums happen to match.

The difference events add exactly every segment whose start has been reached and subtract exactly every segment whose end has been reached. Thus the prefix sum on each span is the correct sum of its active color set. Emitting every nonempty span gives full coverage without overlap, and preserving every genuine set-change boundary gives the minimum valid description.

## Complexity detail

Let $N$ be the number of input segments and $E$ the number of distinct endpoint coordinates, with $E\le2N$.

Building the difference dictionary takes expected $O(N)$ time. Sorting its $E$ entries takes $O(E\log E)$, and the prefix pass plus result construction take $O(E)$. Total time is $O(N+E\log E)=O(N\log N)$ in the worst case.

The dictionary, sorted event list, and returned painting each contain $O(E)$ entries, so auxiliary and output storage are $O(N)$. The prefix sums are performed in place within the sorted event list.

## Alternatives and edge cases

- **Coordinate-array difference sweep:** Since endpoints are bounded by $10^5$, a fixed array can replace the dictionary and sorting. It scans the whole coordinate range and trades domain-dependent memory for simpler indexing.
- **Explicit active-color set:** Sweep start and end events while maintaining actual colors. This can distinguish sets directly but is unnecessary for sums when all endpoint boundaries are retained.
- **Merge adjacent equal sums:** This is incorrect because different unique-color sets may have the same sum, as the statement's example demonstrates.
- **Touching segments:** At a shared endpoint, the ending color is removed and the starting color added before the next half-open interval begins.
- **Overlapping segments:** Their signed contributions accumulate in the prefix sum.
- **Unpainted gap:** The active sum becomes zero and the result comprehension omits that interval.
- **Net-zero delta at an endpoint:** The numeric sum remains equal, but the coordinate stays in the sorted event list, preserving a possible set change.
- **Several starts or ends together:** Dictionary accumulation applies all changes at the same coordinate atomically.
- **Single segment:** Its two events produce one output interval with its color value.
- **Positive unique colors:** A zero prefix unambiguously means no active segment; cancellation between positive active colors cannot create zero.
- **Any output order:** The method naturally returns increasing coordinate order, which is valid even though order is unrestricted.
- **Imported dictionary type:** The exact source assumes `defaultdict` is available.
