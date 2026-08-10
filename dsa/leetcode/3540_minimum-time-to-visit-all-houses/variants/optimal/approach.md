## General

**Each required move has only two simple routes**

The houses form one cycle. Between two distinct houses, the two simple paths are:

- travel only in the forward direction around one arc;
- travel only in the backward direction around the other arc.

Could changing direction produce a shorter route? Any route that changes direction on a cycle and is not one of these simple arcs must revisit a house or immediately retrace part of an edge sequence. Since every road length is positive, the repeated section is a positive-cost cycle and can be removed.

Therefore, a shortest route is always one of the two directional arcs. For every requested move, compute both lengths and take their minimum.

**Why moves can be optimized independently**

After visiting one query target, the next required move always starts at that exact house, regardless of which arc was used to arrive. There is no remaining fuel, direction, or path-dependent state.

Thus choosing the shortest route for one leg cannot make a later leg worse. The minimum total is the sum of independently minimum leg distances:

`0 -> queries[0] -> queries[1] -> ...`.

**Build forward prefix distances**

Forward road `i` goes from house `i` to `(i+1) mod n` with cost `forward[i]`.

Define:

`forward_prefix[t] = forward[0] + ... + forward[t-1]`.

Without wraparound, the forward distance from `current` to a later-indexed `target` is:

`forward_prefix[target] - forward_prefix[current]`.

When `target < current`, that difference is negative. Adding the total forward circumference converts it to the wrapped distance.

The source handles both cases with:

`(forward_prefix[target] - forward_prefix[current]) % forward_total`.

Because `forward_total` is positive, Python modulo returns the unique nonnegative distance around the circle.

**Build backward prefix distances**

Backward road `i` goes from house `i` to `(i-1) mod n` with cost `backward[i]`.

The indexing is different because leaving current house `c` backward consumes `backward[c]`. For `current > target` without wrap, the cost is:

`backward[current] + backward[current-1] + ... + backward[target+1]`.

With:

`backward_prefix[t] = backward[0] + ... + backward[t-1]`,

this equals:

`backward_prefix[current+1] - backward_prefix[target+1]`.

The same expression becomes negative when backward travel wraps through house zero, so the source uses:

`(backward_prefix[current+1] - backward_prefix[target+1]) % backward_total`.

The `+1` offsets are essential. Using the same indices as the forward formula would include or exclude the wrong departure edges.

**Trace a backward wrap**

With three houses, moving backward from house zero to house two uses only road `backward[0]`.

The formula gives:

`(prefix[1] - prefix[3]) mod total`

`= (backward[0] - total) mod total`

`= backward[0]`.

This demonstrates how modulo selects the intended wrapped arc rather than treating a negative difference as invalid.

**Process the itinerary**

`current` starts at zero and `answer` at zero. For each `target`:

1. compute forward arc length;
2. compute backward arc length;
3. add the smaller one;
4. assign `current = target`.

Walking speed is one meter per second, so distance in meters equals time in seconds. No conversion factor is needed.

**Why the formulas return exact arc lengths**

Each forward prefix difference sums every forward departure edge encountered from current until target, exactly once. Modulo adds one full circumference precisely when index order crosses the array boundary.

The backward formula analogously sums every backward departure edge while indices decrease, with its shifted endpoints selecting the correct roads. These are the only two simple paths. Taking their minimum is therefore the shortest-path distance for that leg.

Summing exact shortest legs proves the final total is minimum.

## Complexity detail

Let `n` be the number of houses and `Q = len(queries)`. Building each prefix array scans `n` road lengths, taking `O(n)` time. Each query leg uses a constant number of array accesses, arithmetic operations, and comparisons, so all legs take `O(Q)`.

Total time is `O(n+Q)`.

The two prefix arrays each contain `n+1` integers, using `O(n)` auxiliary space. Other state is constant.

The total answer can be much larger than a 32-bit integer: up to many query legs, each potentially traversing a substantial fraction of `n` roads of length `10^5`. Python integers are safe; fixed-width implementations should use 64-bit storage.

## Alternatives and edge cases

- **Run Dijkstra for every leg:** The graph has only a cycle structure, so general shortest-path machinery is unnecessary and much slower.
- **Walk edge by edge per query:** Correct but can cost `O(nQ)`. Prefix sums reduce each arc to constant time.
- **Always choose forward:** Directional costs can differ greatly; both arcs must be compared.
- **Mix forward and backward edges:** Any non-simple mixed route contains removable positive-cost repetition and cannot beat both simple arcs.
- **Use forward prefix indices for backward roads:** Backward cost is attached to the departure house, requiring `current+1` and `target+1` endpoints.
- **Forward wraparound:** Modulo adds the forward circumference when target index is smaller.
- **Backward wraparound:** Modulo similarly resolves the negative backward prefix difference.
- **Current equals target:** Although consecutive queries exclude this and the first target is not zero, both formulas return zero and the source would handle it.
- **Two houses:** There may be distinct forward and backward directed road costs between the same pair; the minimum is chosen.
- **Highly asymmetric directions:** Prefix totals and per-leg comparisons remain valid.
- **Positive edge guarantee:** It is what makes cycle removal safe. Zero weights would still not hurt, but negative weights would invalidate the simple-path argument.
- **Sequential queries:** Only the target house becomes the next state; arrival direction has no effect.
- **Unit walking speed:** Numerical distance equals time, so no division or multiplication is needed.
