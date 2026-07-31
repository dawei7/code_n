## General

The offers are weighted inclusive intervals. A choice ending at house `end` is compatible only with choices whose sold houses all lie before `start`; an offer beginning at `start` may therefore extend the best result for the prefix ending just before that house.

Group every offer by its ending house. Define `best[p]` as the maximum gold obtainable using only houses with indices less than $p$. Thus `best[0] = 0`, and after processing house `end`, the state written at `best[end + 1]` covers houses `0` through `end`.

There are two ways to obtain that state:

- leave house `end` unused, preserving `best[end]`; or
- accept an offer `[start, end, gold]`, adding its gold to `best[start]`.

Evaluate every offer in the second transition and keep the maximum.

**Sparse-house safeguard**

The app-local adapter must also remain usable under its execution-step guard when `n` is very large but only a few offers exist. In that regime it evaluates the same recurrence over offers sorted by end house and uses binary search to find the prefix ending before each `start`. It selects this route only when $m(\lfloor \log_2 m \rfloor+2) < n$, so its $O(m \log m)$ work is bounded by $O(n)$. Otherwise it uses the direct house-prefix scan above. The exact remotely accepted native artifact uses the direct scan.

**Why the prefix transition is complete**

Consider an optimal valid selection restricted to houses through `end`. If it accepts no offer ending at `end`, the same selection is represented by `best[end]`. Otherwise, take its offer `[start, end, gold]`. Every other accepted offer must end before `start`, because house intervals are inclusive and cannot overlap. Those earlier offers form a valid solution represented by `best[start]`, so this optimum appears among the transition candidates.

Conversely, `best[end]` is already valid for the larger prefix, and combining `best[start]` with an offer starting at `start` cannot reuse a house. Every transition is therefore valid, and induction over increasing end houses proves that `best[n]` is the maximum obtainable gold.

## Complexity detail

Let $m$ be the number of offers. Building the end groups takes $O(m)$ time. The direct house scan visits $n$ positions, and every offer is evaluated exactly once. The sparse route costs $O(m \log m)$ only under a condition that bounds that quantity by $O(n)$. Thus the app-local method and the native direct scan both satisfy total time $O(n+m)$. Their arrays and grouped offers use $O(n+m)$ space.

The benchmark uses $m$ as `size`, keeps all offers mutually overlapping, and forces a conventional offer-index dynamic program to inspect every earlier offer before concluding that none is compatible.

## Alternatives and edge cases

- **Sort plus binary search:** Sort offers by an endpoint and binary-search the previous compatible interval. This weighted-interval method takes $O(m \log m)$ time and $O(m)$ space and can avoid scanning unused houses.
- **Quadratic offer dynamic programming:** For every offer, scan all earlier offers to find compatible predecessors. It is correct but takes $O(m^2)$ time.
- **Shared endpoint:** Offers `[a, x, ...]` and `[x, b, ...]` overlap at house `x`; compatibility requires the earlier end to be strictly less than the later start.
- **Adjacent intervals:** An offer ending at `x` and another starting at `x + 1` are compatible.
- **Unsold houses:** Carrying `best[end]` forward permits arbitrary gaps between accepted offers.
- **Competing equal ranges:** Multiple buyers may request the same houses; only the most profitable compatible transition survives.
- **Inclusive indexing:** `best[start]` represents houses strictly before `start`, which is why no subtraction is needed in the transition.
- **Sparse offers:** Houses without an ending offer only copy the preceding prefix optimum.
