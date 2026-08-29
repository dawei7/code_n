## General

A cheap end removal may also discard legal cars, while an internal illegal car can always be removed for cost two. The exact solution computes the best cost for every prefix and suffix, then combines them at a boundary.

**Define prefix cost**

`pre[i]` is the minimum cost to remove all illegal cars from the first `i` characters, `s[:i]`.

Initially `pre[0] = 0`. For character `s[i]`:

- if it is zero, no new illegal car appears, so `pre[i + 1] = pre[i]`;
- if it is one, either remove this car internally for two after optimally handling the earlier prefix, costing `pre[i] + 2`, or remove the entire prefix from the left, costing `i + 1`.

Thus the recurrence uses `min(pre[i] + 2, i + 1)` for a one.

Removing the whole prefix covers every possible pattern inside it, which is why it competes with the internal-removal plan.

**Define suffix cost symmetrically**

`suf[i]` is the minimum cost to remove illegal cars from `s[i:]`. The backward scan starts with `suf[n] = 0`.

For a zero, the next suffix cost is unchanged. For a one, either remove it internally after handling the rest for `suf[i + 1] + 2`, or remove the entire suffix from the right for `n - i`. The smaller becomes `suf[i]`.

**Combine disjoint regions**

For a boundary `i`, prefix `s[:i]` and suffix `s[i:]` are disjoint and cover the train. Handling their illegal cars independently costs `pre[i] + suf[i]`.

The exact source evaluates indexes one through $n$ by zipping `pre[1:]` with `suf[1:]`. It omits boundary zero, but this cannot lose the optimum:

- if `s[0] == '0'`, `pre[1]=0` and `suf[0]=suf[1]`, so boundary one equals boundary zero;
- if `s[0] == '1'`, `pre[1]=1` and `suf[1]\le n-1`, so the boundary-one cost is at most $n$ and at most the competing `suf[1]+2`; therefore it is no worse than `suf[0]=min(suf[1]+2,n)`.

Every omitted boundary-zero plan has an equally good or better represented boundary.

**Why splitting captures mixed strategies**

End removals from the left affect a prefix, end removals from the right affect a suffix, and remaining illegal cars may be removed internally. The prefix and suffix recurrences already choose between wholesale end removal and individual cost-two removals within their regions. Trying every boundary captures where responsibility shifts between the two sides.

For `"0010"`, a boundary can leave the single illegal car to a suffix plan costing two, matching removal from the right twice or internal removal once.

It is important that a zero does not force either recurrence to pay anything. A legal car inside a region may remain in the train; the goal is only to remove every illegal car. However, an end-removal option can still remove legal cars incidentally when doing so is part of a cheaper route to illegal cars farther inside. The recurrence represents that possibility through the whole-prefix cost `i + 1` and whole-suffix cost `n - i`.

**Why no valid plan can beat the minimum**

Consider `pre[i + 1]` when `s[i]` is illegal. Any plan represented for this prefix either pays for this car as an internal removal, in which case the earlier illegal cars require at least `pre[i]` and the total is at least `pre[i] + 2`, or it removes through this position from the left, which costs `i + 1`. These are exactly the two recurrence candidates. When `s[i]` is legal, it requires no removal, so the optimum stays `pre[i]`. This proves every prefix value is minimal; the same argument in reverse proves every suffix value is minimal.

For any tested boundary, adding those two values gives a real plan because the prefix and suffix are disjoint. Thus the returned minimum can never be smaller than what is achievable. In the other direction, the dynamic programs already include pure left removal, pure right removal, pure internal removal, and every mixture obtained by assigning the two disjoint regions around a boundary. The cheapest full plan therefore appears among the combined candidates. Since the algorithm selects their minimum, it returns exactly the required minimum time.

## Complexity detail

Both scans visit $n$ characters once, and the final zipped minimum examines $n$ pairs. Time is $O(n)$.

The exact source allocates two arrays of length $n+1$, so auxiliary space is $O(n)$, contrary to the manifest's $O(1)$ summary. The generator expression used by `min` produces sums one at a time instead of building another length-$n$ collection, so it adds only constant working space. An optimized formulation can compress one direction into scalar state, but this file documents the stored code.

## Alternatives and edge cases

- **Constant-space one-pass DP:** Maintain the best prefix cost and combine it with the cost of removing the remaining suffix from the right. This achieves the manifest’s $O(1)$ auxiliary space.
- **Remove every illegal car internally:** This costs twice the number of ones but may lose to cheap end removals.
- **Remove the entire train:** Cost $n$ is always a valid upper bound.
- **All zeros:** Both DP arrays remain zero and the answer is zero.
- **All ones:** Removing the entire train from either end costs $n$, often better than individual removals.
- **One character zero:** The result is zero.
- **One character one:** Prefix removal costs one and is optimal.
- **Illegal car at an end:** Removing that end once can beat internal cost two.
- **Long legal prefix:** Left removal may waste time on zeros, so internal or right strategies can win.
- **Long legal suffix:** The symmetric reasoning applies.
- **Negative costs impossible:** All recurrence terms are nonnegative.
- **Empty region:** `pre[0]` and `suf[n]` correctly cost zero.
- **Exact stored space:** Full arrays make state meanings transparent but consume linear memory.
- **Input preservation:** Strings are immutable, and the algorithm stores only numeric costs.
