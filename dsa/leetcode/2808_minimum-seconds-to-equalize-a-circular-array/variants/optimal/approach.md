## General

**Choose the final value, then ask how fast it can spread.** In one second, every position may copy a value from either circular neighbor. No operation invents a new value: every copied value already existed at a neighboring position in the previous second. Therefore, if the whole array eventually becomes one value, that final value must be one that appears in the original array.

The algorithm considers each distinct original value as a candidate target. It groups all indices of equal values in a dictionary. Because `enumerate(nums)` visits indices in increasing order, every stored index list is already sorted.

**Propagation happens simultaneously in both directions.** Fix one target value. Its original occurrences are sources. After one second, positions at circular distance one from a source can hold the target. After two seconds, positions at distance two can hold it, and so on. Since all positions update simultaneously, the time for the target to cover the array is the maximum, over all positions, of the distance to the nearest original source.

It is not necessary to simulate those waves second by second. The hardest positions lie in the gaps between consecutive source occurrences around the circle.

**Measure gaps by source-index distance.** Suppose two consecutive target occurrences are at indices $p$ and $q$ with $p<q$. Their index distance is $g=q-p$. There are $g-1$ non-source positions strictly between them. A target wave advances rightward from $p$ and leftward from $q$ at the same time.

The farthest middle position is reached after $\lfloor g/2 \rfloor$ seconds. For example, a source distance of five leaves four interior positions; the two waves cover them in two seconds. A source distance of four leaves three positions; the middle one is distance two from either source.

The exact code computes the largest such $g$ and returns its integer half. It initializes `t` with the wraparound source distance

`idx[0] + n - idx[-1]`.

This is the number of circular steps from the last occurrence forward through index $n-1$, wrapping to zero, and reaching the first occurrence. It then scans ordinary consecutive pairs with `pairwise(idx)` and updates `t = max(t, j - i)`.

**Why the wraparound gap cannot be omitted.** The array is circular, so the last and first occurrence are neighbors in cyclic order. An algorithm that checks only adjacent entries in the sorted list would accidentally treat the ends as boundaries and could miss the largest uncovered arc. The explicit formula closes the circle.

**Convert the worst gap to time.** After all cyclic gaps have been considered, `t` is the maximum distance between consecutive original occurrences of this target. The candidate time is `t // 2`, which equals $\lfloor t/2 \rfloor$ for nonnegative integers.

Why does considering only the largest gap work? Every array position belongs to one cyclic arc between consecutive sources. In an arc of source distance $g$, its time to receive the value is at most $\lfloor g/2 \rfloor$, and some middle position attains that bound. The whole array is ready when its slowest arc is ready, so the target's exact completion time is the maximum of these per-gap halves. Since floor division is monotone, that is $\lfloor \max(g)/2 \rfloor$.

**Choose the best target.** `ans` begins at infinity. For every occurrence list, the algorithm updates `ans` with the smaller candidate time. All possible final values are represented by the dictionary keys, so this minimum selects the fastest feasible equalization.

**A one-source example.** If a target occurs once at index $p$, then `idx[0] == idx[-1]` and the wrap distance is $p+n-p=n$. There are no ordinary pairs. The candidate time is $\lfloor n/2 \rfloor$, exactly the maximum circular distance from the one source.

**Why no newly copied source can beat this calculation.** The distance formula already models new copies propagating outward one edge per second. A value copied at time one can copy onward at time two, so the wave naturally uses intermediate positions. The calculation is not restricted to direct copying from original sources; it computes the earliest possible chain of copies.

**Why simultaneous updates matter.** Values chosen for a second come from the previous array state, not from updates earlier in the same second. That limits propagation to one edge per second and makes graph distance the correct time measure. If updates were sequential and immediately visible, a value could sweep across many positions in one pass, and this gap formula would not apply.

## Complexity detail

Let $n$ be the array length. Building the dictionary visits every element once, taking expected $O(n)$ time and $O(n)$ space. Across all target groups, the total number of stored indices is exactly $n$.

For a group with $r$ occurrences, `pairwise` visits $r-1$ adjacent pairs. Summed over all groups, these iterations are at most $n$ minus the number of distinct values, so the complete gap analysis is $O(n)$. Dictionary operations have expected constant time. Overall expected time is $O(n)$.

The occurrence lists collectively store $n$ integer indices, and the dictionary has at most $n$ keys, so auxiliary space is $O(n)$. The calculations for one group use only constant additional variables.

The method does not sort occurrence lists; their sorted order comes for free from the initial left-to-right enumeration. Sorting each group would add an unnecessary $O(n \log n)$ worst-case cost.

## Alternatives and edge cases

- **Multi-source BFS for each value:** Treat all occurrences of one value as sources and compute the farthest circular distance. This is correct but can take $O(n)$ per distinct value, or $O(n^2)$ overall.
- **Binary search on time:** Check whether some value can cover the circle within a proposed number of seconds. The gap formula already yields each exact time directly, so search is unnecessary.
- **Simulate every second:** Repeatedly copy values until the array is equal. This can be complicated by simultaneous-state handling and does more work than measuring propagation distances.
- **Array already equal:** Every cyclic gap for the sole value is one, so `1 // 2` is zero and no operation is needed.
- **One occurrence of a target:** Its only cyclic gap is $n$, giving $\lfloor n/2 \rfloor$ seconds.
- **Two sources opposite each other:** The largest gap determines how far the two wavefront pairs must travel; equal gaps are handled naturally.
- **Odd largest gap:** Integer division correctly gives the distance of the central positions, such as $5 // 2 = 2$.
- **Even largest gap:** The unique middle position or central boundary is reached in exactly half the source distance.
- **Wraparound largest gap:** The explicit last-to-first distance ensures positions near indices zero and $n-1$ are analyzed as adjacent on the circle.
- **Duplicate values:** More occurrences create more, usually smaller gaps; every position index is retained because source multiplicity and spacing matter.
- **Final value not initially present:** This is impossible because operations only copy existing neighbor values; the dictionary therefore covers every feasible target.
- **Simultaneous copying:** The distance model assumes at most one-edge propagation per second, exactly as required by using the previous second's values.
