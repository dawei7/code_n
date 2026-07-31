## General

**Separate the machines**

All alloys must come from one machine, so recipes never share a production plan. Evaluate each row of `composition` independently and keep the best result. For a fixed recipe and a proposed count $x$, metal $j$ requires `recipe[j] * x` units. Existing stock covers part or all of that amount, making the purchase cost

$$
\sum_{j=0}^{n-1}
\max\bigl(0,\ \texttt{recipe[j]}x-\texttt{stock[j]}\bigr)
\texttt{cost[j]}.
$$

The count $x$ is feasible exactly when this sum is at most `budget`. Stop accumulating as soon as the sum exceeds the budget because every remaining term is nonnegative.

**Binary-search the monotone boundary**

If a machine can make $x$ alloys, it can also make every smaller number; conversely, an unaffordable count makes every larger count unaffordable. This monotonicity permits binary search for the last feasible count.

For each metal $j$, even pretending the entire budget could be spent only on that metal gives at most

$$
\left\lfloor
\frac{\texttt{stock[j]} + \left\lfloor \texttt{budget}/\texttt{cost[j]} \right\rfloor}
{\texttt{recipe[j]}}
\right\rfloor
$$

alloys. The minimum of these quantities is therefore a safe recipe-specific upper bound. Binary-search from zero through that bound, raising the lower endpoint after a feasible count and lowering the upper endpoint after an infeasible one. The invariant leaves no unchecked feasible count above the recorded answer. Repeating this for every machine and taking the maximum respects the same-machine restriction.

## Complexity detail

Let $M$ be the largest recipe-specific upper bound searched, $k$ the number of machines, and $n$ the number of metals. A feasibility check scans at most $n$ metals, and each machine performs $O(\log M)$ checks. The total time is $O(kn \log M)$ with $O(1)$ auxiliary space, excluding the input.

The benchmark uses the known feasible alloy count as `size`, while keeping legal fixed-size recipes. Binary search grows logarithmically with that count. A correct enumeration implementation tests consecutive counts for every machine, completes all tiers, and exhibits linear growth in `size`, so it fails only the scaling verdict.

## Alternatives and edge cases

- **Enumerate production counts:** Test `0, 1, 2, ...` until a count becomes unaffordable for each machine. Monotonicity makes it correct, but its time depends linearly on the answer rather than logarithmically.
- **Exponential upper-bound search:** Double a feasible count until it fails, then binary-search the discovered interval. This avoids deriving a bound and has the same asymptotic search cost, but the formula above provides a tighter legal interval directly.
- **Zero budget:** Production can still be positive when existing stock covers a recipe; feasibility must always subtract stock before charging for metal.
- **Zero answer:** If no machine can produce one alloy from stock and the budget, binary search must preserve `0` as feasible.
- **One machine only:** The same feasibility search applies without any special case.
- **Large values:** Products and total expenses can exceed 32-bit integer range even though each individual input respects its limit, so implementations must use sufficiently wide arithmetic.
- **Same-machine rule:** Taking favorable metals from different recipe rows is invalid; only complete production counts for one row may be compared.
