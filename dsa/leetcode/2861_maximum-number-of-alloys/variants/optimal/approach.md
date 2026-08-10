## General

**Separate the machine choices.** Every alloy in one production plan must use the same machine. A plan cannot make some alloys with one composition and the rest with another. Therefore, the solution evaluates each row `c` of `composition` independently, finds the largest affordable production count for that machine, and takes the maximum over all machines.

For one fixed machine, suppose the company wants to produce $q$ alloys. If that machine needs `c[j]` units of metal type $j$ per alloy, total demand for that metal is $q\cdot\texttt{c[j]}$. Existing stock covers up to `stock[j]` units. Only a positive shortage must be purchased:

$$
\max(0,\ q\cdot\texttt{c[j]}-\texttt{stock[j]}).
$$

Multiplying the shortage by `cost[j]` gives the purchase cost for metal $j$. Summing across all $n$ metals gives exactly the expression computed as `s`:

$$
C(q)=\sum_{j=0}^{n-1}
\max(0,\ q\cdot\texttt{c[j]}-\texttt{stock[j]})
\cdot\texttt{cost[j]}.
$$

The production count `q` is feasible precisely when $C(q)\le\texttt{budget}$.

**Why binary search applies.** The cost function is monotone non-decreasing. Increasing $q$ never reduces any metal demand, so no shortage can decrease and total purchase cost cannot decrease. Thus feasible counts form one prefix: `0, 1, 2, ..., maximum_feasible`. After the first infeasible count, every larger count is also infeasible. This true-then-false boundary is exactly what binary search needs.

**The search interval is safe.** The implementation uses `l = 0` and `r = budget + stock[0]`. Zero alloys are always feasible. To see why the upper bound is sufficient, focus only on metal type zero. Every composition entry is at least one and every unit cost is at least one. Producing $q$ alloys needs at least $q$ units of metal zero. At most `stock[0]` of those units are free, and at most `budget` additional units can be bought because each costs at least one coin. Therefore no feasible $q$ can exceed `stock[0] + budget`. Other metals may make the real limit smaller, but never larger.

The loop uses the upper midpoint `mid = (l + r + 1) >> 1`. Choosing the upper midpoint matters when `l` and `r` are adjacent: if `mid` is feasible, assigning `l = mid` still makes progress. When the computed cost is within budget, `mid` belongs to the feasible prefix and the search keeps it by moving `l` upward. Otherwise, `mid` and everything above it are rejected with `r = mid - 1`. When the endpoints meet, `l` is the greatest feasible production count for that machine.

**Why taking the maximum afterward is correct.** The loop repeats the complete boundary search for every machine composition. Any legal production plan uses one of those machines, so its alloy count cannot exceed that machine's computed maximum. Conversely, each computed count is a feasible plan for its own machine. The largest of them is consequently the global optimum.

**Trace a simple cost check.** With composition `[1,1,1]`, no stock, costs `[1,2,3]`, and budget `15`, producing two alloys costs `2*1 + 2*2 + 2*3 = 12`, so two is feasible. Producing three costs `18`, so it is infeasible. Binary search locates the boundary at two without testing every count sequentially.

The stock is never subtracted destructively. Each candidate count recomputes shortages from the original stock, which is correct because binary-search probes are hypothetical plans, not production steps being carried out.

## Complexity detail

Let $k$ be the number of machines, $n$ the number of metal types, and let $U=\texttt{budget}+\texttt{stock[0]}$. One feasibility calculation zips through $n$ metal types, so it costs $O(n)$. Binary search performs $O(\log(U+1))$ probes per machine. Across all machines, total time is $O(kn\log(U+1))$, customarily abbreviated $O(kn\log M)$ for the searched production range.

The generator passed to `sum` is consumed lazily and stores no $n$-sized temporary list. Apart from loop variables and arithmetic scalars, the function allocates no structure that grows with the input, so auxiliary space is $O(1)$, excluding the supplied arrays. Python integers expand safely; fixed-width implementations should use 64-bit arithmetic for `mid * x` and the accumulated cost.

## Alternatives and edge cases

- **Linear production simulation:** Incrementing the alloy count one by one can require up to about $2\times10^8$ trials and is unnecessary because affordability is monotone.
- **Exponential upper-bound search:** Doubling an upper bound until infeasible is useful when no direct cap is known. Here `budget + stock[0]` is already a proven safe cap.
- **Zero budget:** Existing stock may still permit alloys. The same formula returns zero purchase cost while all demands fit within stock.
- **Unused surplus stock:** `max(0, demand - stock)` prevents surplus from becoming a negative cost or subsidizing other metals.
- **Different best machines:** Every machine must be searched; a composition that looks expensive in one metal may exploit abundant stock in that metal.
- **All alloys use one machine:** Taking a maximum over machines is correct; combining rows of `composition` within one plan is forbidden.
- **Overflow outside Python:** Products of production counts, composition amounts, and costs require a wide integer type.
- **Input naming:** The parameters `n` and `k` agree with the array dimensions, but the loops correctly derive actual work from `composition` and each row.
