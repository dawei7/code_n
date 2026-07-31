## General

**Represent each range by two witnesses.** In every positive-range part, choose one position holding its minimum and one holding its maximum. Their absolute value difference equals that part's range. Because partition parts are disjoint cyclic arcs, these witness pairs do not cross one another around the cycle.

Conversely, take any non-crossing collection of disjoint witness pairs. Give each pair its own cyclic arc and assign the unselected gaps to neighboring arcs. Adding positions to an arc cannot reduce the range already witnessed by its pair. Therefore, maximizing the partition score is equivalent to maximizing the sum of absolute differences of at most $q$ non-crossing pairs.

**Account for both cyclic topologies.** Relative to the displayed cut between the last and first array positions, selected endpoints have one of two forms:

- No pair crosses the cut. In increasing index order, endpoints pair consecutively.
- One pair crosses the cut and connects the first selected endpoint to the last. Every endpoint strictly inside that outer pair still pairs consecutively.

There cannot be two crossing pairs because the partition arcs are disjoint. Evaluating these two forms covers every cyclic partition, including the wrapped pair used in Example 1.

**Optimize ordinary pairs.** Let `closed[t]` be the best total after completing `t` pairs. When an endpoint with value $x$ opens the next pair, retain both signed forms `closed[t] + x` and `closed[t] - x`. Closing at a later value $y$ contributes the better of $x-y$ and $y-x$, which is $\lvert x-y\rvert$. Updates use the previous position's states, so one index cannot close one pair and open another.

**Optimize one wrapped pair.** Fix one of the two signs for the outer absolute difference. Keep its first endpoint open while applying the ordinary-pair recurrence to endpoints inside it; a later endpoint then closes the outer pair with the opposite sign. Running both outer signs represents either ordering of its two endpoint values. The best result across the ordinary case and both wrapped signs is the cyclic optimum.

## Complexity detail

Each of the three state scans processes $n$ values and $q$ pair counts, giving $O(nq)$ time. Every scan retains only its current arrays of $q$ states, so the auxiliary space is $O(q)$. The answer can exceed 32-bit range, so fixed-width implementations require a 64-bit result type.

## Alternatives and edge cases

- **Try every cut separately:** Solving a linear partition after all $n$ rotations is correct but repeats the same work and takes $O(n^2q)$ time.
- **Enumerate cut subsets:** Directly constructing every cyclic partition is exponential when `k` grows.
- **Assume the displayed cut is a boundary:** This misses wrapped optimal parts such as `[3,1]` in Example 1.
- **At most, not exactly:** Extra singleton parts add zero range, so the optimum may deliberately use fewer than `k` parts.
- **One-element array:** No positive-range pair exists, and the only possible score is `0`.
- **All values equal:** Every subarray range is zero, regardless of the number or placement of cuts.
- **Large values and score:** Up to $q$ differences near $10^9$ can be added, requiring 64-bit arithmetic in fixed-width languages.
