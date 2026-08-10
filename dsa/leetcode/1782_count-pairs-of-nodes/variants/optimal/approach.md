## General

**Start from node degrees, then correct shared edges**

For nodes `a` and `b`, adding their degrees counts every edge incident to either node. However, an edge directly connecting `a` and `b` appears once in each degree, while `incident(a,b)` should count that edge only once.

If `shared(a,b)` is the number of parallel edges between the pair, then:

$$
\operatorname{incident}(a,b)
=
\deg(a)+\deg(b)-\operatorname{shared}(a,b).
$$

The exact solution first counts pairs using the easier raw degree sum, then subtracts pairs that were false positives because of shared-edge double counting.

**Build degrees and edge multiplicities**

`cnt` stores each node's degree. Every input edge increments both endpoint degrees, including parallel edges.

Endpoints are converted to zero-based indices and normalized with smaller endpoint first. `g[(a,b)]` then records how many parallel edges connect that unordered pair.

Normalization ensures edges `(u,v)` and `(v,u)` would use the same key. Only connected pairs appear in `g`; unconnected pairs have shared multiplicity zero and never need correction.

**Sort degrees for query counting**

`s = sorted(cnt)` loses node identity but preserves the multiset of degrees. For the initial raw condition, only the two degree values matter.

For query threshold `t` and a degree `x = s[j]`, the solution needs later indices whose degree is strictly greater than `t - x`.

`bisect_right(s, t - x, lo=j + 1)` returns the first later index `k` with value greater than `t - x`. All indices from `k` through `n - 1` form raw sums greater than `t`, so `n - k` is added.

Starting at `j + 1` enforces two distinct sorted positions and counts each unordered node pair exactly once.

**Why bisect_right matches strict greater-than**

The condition is `degree1 + degree2 > t`. A second degree equal to `t - x` gives sum exactly `t` and must not count.

`bisect_right` skips all values equal to the search target and points after them. A left bisect would incorrectly include equality.

**Correct pairs connected by parallel edges**

The raw sorted count uses `cnt[a] + cnt[b]`. For every connected unordered pair with multiplicity `v`, the source checks:

- raw sum is greater than `t`, so the pair was counted;
- corrected sum `cnt[a] + cnt[b] - v` is at most `t`, so it should not count.

When both hold, it subtracts one from the query answer.

Only one is subtracted regardless of `v` because the answer counts the node pair once. The multiplicity affects whether that one pair crosses the threshold.

If raw sum is not above the threshold, the pair was never added. If corrected sum remains above it, the raw inclusion was valid. No other case needs adjustment.

**Trace the shared-edge issue**

Suppose two nodes have degrees five and four and share two parallel edges. Their raw sum is nine, but incident count is seven.

For threshold eight, sorted degree counting includes the pair because nine is greater than eight. The correction sees seven is at most eight and subtracts it.

For threshold six, both nine and seven are greater than six, so the pair remains counted.

**Why every query result is correct**

Binary-search counting includes exactly all unordered pairs whose raw degree sum exceeds the query. Unconnected pairs have no shared edge, so raw sum already equals incident count.

For connected pairs, the correction removes exactly those and only those whose raw sum passes while the true shared-edge-adjusted count does not. Therefore the final number equals the pairs satisfying the true incident condition.

## Complexity detail

Let $E$ be the number of edges, $P$ the number of distinct connected node pairs, $Q$ the number of queries, and $n$ the node count.

Building degrees and multiplicities takes expected $O(E)$ time. Sorting degrees takes $O(n\log n)$. For each query, the exact source performs $n$ binary searches, costing $O(n\log n)$, then scans $P$ multiplicity entries for corrections. Total exact time is:

$$
O(E+n\log n+Q(n\log n+P)).
$$

This differs from the manifest's $O(E+n\log n+Q(n+P))$ claim. That tighter per-query node term requires a two-pointer scan over sorted degrees; the exact `solution.py` uses per-node binary search.

The degree arrays use $O(n)$ and the multiplicity dictionary uses $O(P)$ space. Answers use $O(Q)$, with $Q$ bounded by 20. Peak space is $O(n+P)$, matching the manifest.

## Alternatives and edge cases

- **Two pointers per query:** Count raw degree pairs in $O(n)$ after sorting, achieving the manifest's tighter query bound.
- **Check every node pair:** It costs $O(Qn^2)$ and is too slow.
- **Ignore shared edges:** It overcounts connected pairs because their mutual edges appear in both degrees.
- **Single edge between pair:** Subtract one from raw degree sum for true incident count.
- **Multiple parallel edges:** Subtract the full multiplicity, but adjust the answer count by one pair.
- **Unconnected pair:** Multiplicity is zero, so no correction entry is needed.
- **Strict threshold:** Sum equal to the query does not count; `bisect_right` handles this.
- **Normalized endpoints:** Smaller-first keys combine all parallel edges consistently.
- **Equal degree nodes:** Sorted positions remain distinct and are counted once through `j + 1`.
- **Several identical queries:** The exact source recomputes each independently.
- **Node identities after sorting:** They are unnecessary for raw count but retained in `cnt` for shared-edge corrections.
- **One false positive:** Each dictionary pair can cause at most one subtraction per query.
- **Zero threshold:** Every pair with at least one incident edge may qualify according to the same formula.
- **Input preservation:** Endpoints are normalized in local variables; `edges` is not changed.
