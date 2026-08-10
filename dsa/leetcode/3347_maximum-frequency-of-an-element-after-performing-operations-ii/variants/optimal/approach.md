## General

**Convert every index into a target interval.** Value $v$ can be changed once by an integer in $[-k,k]$, so it can become exactly the integer targets in $[v-k,v+k]$. For a target $x$, the number of these intervals covering $x$ is the number of array elements capable of becoming $x$.

The larger coordinate bounds rule out scanning every possible target. The exact source uses sparse interval events whose count depends only on $n$.

**Difference-event construction.** For each $v$, `d[v-k] += 1` begins coverage and `d[v+k+1] -= 1` ends coverage after the inclusive right endpoint. When event coordinates are sorted, running sum `s` is the interval overlap at each coordinate.

Using $v+k+1$ is valid because all target values and adjustments are integers. The endpoint $v+k$ must remain reachable.

`cnt[v]` counts original copies. Statement `d[v] += 0` deliberately creates an event coordinate even when no interval boundary lies there. An original target must be evaluated because its unchanged copies receive special operation-budget treatment.

**Derive the achievable frequency at one target.** All `s` covering elements could reach $x$ if operations were unlimited. `cnt[x]` of them already equal $x$ and need no useful operation. At most `numOperations` other indices can be changed. Therefore

$$
F(x)=\min\left(s,\texttt{cnt}[x]+\texttt{numOperations}\right).
$$

The first argument enforces physical reachability; the second enforces how many nonexisting copies can be converted.

**Why sparse coordinates are sufficient.** Between two consecutive interval events, overlap $s$ is constant. If no original value occurs inside that region, `cnt[x]=0` throughout and $F(x)=\min(s,\texttt{numOperations})$ is also constant. It suffices to test an event boundary. If an original value occurs, its zero event ensures the sweep tests it. No unseen coordinate can have a larger objective.

This argument also explains why testing only original values would be incomplete. The best target can be absent from `nums` when several reachable intervals overlap there. Such a target receives no unchanged-copy bonus, but it can still produce the largest frequency when the operation budget is large enough. Interval starts and ends ensure that every distinct overlap level that could support such an absent target is represented.

**Interpret the two caps independently.** If $s=12$, `cnt[x]=5`, and only three operations are allowed, at most eight copies can meet at $x$: five are already present and three can be converted. If instead $s=6$, the answer at that target is six even with a huge budget, because only six indices can reach it. The expression `min(s, cnt[x] + numOperations)` selects the binding physical constraint in either situation.

**Exactly the operation count does not force harmful changes.** Operations must select distinct indices, but adding zero is allowed. Once the useful conversions are made, any remaining operations can select unused indices and add zero, leaving frequency unchanged. Thus the optimization may use up to `numOperations` effective changes.
For every evaluated target, interval overlap exactly counts reachable indices. Keeping original copies and converting any allowed subset of other covering indices realizes the cap formula; no solution can exceed either cap. Sparse-candidate reasoning proves an optimal target is evaluated. Taking the maximum therefore returns the global optimum.

**Why this scales to $10^9$.** Dictionary keys can be large positive or negative integers without allocating intermediate coordinates. Only starts, ends-after, and original values are stored. Sorting at most $O(n)$ keys replaces impossible traversal of a billion-wide range.

The source for versions I and II is identical, but this sparse design is essential under II's enlarged limits.

## Complexity detail

Building `cnt` and `d` takes expected $O(n)$ time. There are at most three event coordinates per distinct occurrence before aggregation, hence $O(n)$ unique keys. Sorting costs $O(n\log n)$ and sweeping costs $O(n)$. Total time is $O(n\log n)$.

Both dictionaries and the sorted event list use $O(n)$ auxiliary space. Coordinate magnitude does not affect the asymptotic storage.

## Alternatives and edge cases

- **Sort plus binary searches:** For each critical target $v$, $v-k$, and $v+k$, count reachable elements with lower/upper bounds. It also gives $O(n\log n)$.
- **Dense difference array:** It is impossible when coordinates and $k$ approach $10^9$.
- **Target not originally present:** Every contributing element consumes an operation, so frequency cannot exceed `numOperations`.
- **Many unchanged copies:** They all contribute without consuming the operation budget.
- **No operations:** Only existing frequencies matter; zero events ensure they are tested.
- **Zero adjustment range:** Intervals collapse to original values, and useful changes cannot alter anything.
- **Unused mandatory operations:** Adding zero to distinct unused indices satisfies the exact count.
- **Duplicate intervals:** Difference events accumulate their multiplicity in overlap `s`.
- **Right-boundary inclusion:** Subtracting at one past the endpoint prevents losing values exactly $k$ away.
- **Negative left endpoints:** They are legal target coordinates in the sweep even though originals are positive.
- **Huge gaps:** No keys are allocated inside them; constant-overlap plateaus need one evaluation only.
- **Original coordinate insertion:** The zero update is required to observe the unchanged-frequency bonus.
- **Version II distinction:** Sparse events make complexity independent of value range, which is the central scaling requirement.
