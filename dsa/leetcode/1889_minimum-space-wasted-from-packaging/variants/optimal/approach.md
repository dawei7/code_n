## General
**Assign greedily within one supplier**

Once a supplier is fixed, each package should use that supplier's smallest box that can contain it. Any larger choice only increases waste and cannot help another package because every offered size has unlimited supply. Thus the remaining task is to evaluate this forced optimal assignment efficiently for every feasible supplier.

Sort the packages and each supplier's box sizes. A supplier whose largest box is smaller than the largest package is immediately infeasible. For any other supplier, process box sizes in ascending order. If the previous sizes have already covered the first `packed` packages, binary-search for the first remaining package larger than the current box size. Every package in the newly covered block uses this box size.

**Compare total capacity**

For a block of $c$ packages assigned to size $b$, add $bc$ to the supplier's total box capacity. The package-size sum is identical for every supplier, so minimizing total capacity also minimizes waste. After evaluating all feasible suppliers, subtract the sum of the package sizes once and apply the modulus.

The sorted blocks partition all packages: binary search assigns a package to the first box size that can hold it, which is precisely its smallest adequate size. Therefore each evaluated supplier receives its minimum possible waste, and taking the least such total over all feasible suppliers is globally optimal.

## Complexity detail
Sorting the $N$ packages costs $O(N\log N)$. If supplier $j$ has $k_j$ sizes, sorting it costs $O(k_j\log k_j)$ and its binary searches cost $O(k_j\log N)$. Since $\sum_j k_j=B$, these totals are bounded by $O(B\log B)$ and $O(B\log N)$. A sorted package copy and one sorted supplier copy require $O(N+K)$ auxiliary space.

## Alternatives and edge cases
- **Per-package linear box search:** Testing every offered box size for every package is correct but can take $O(NB)$ time.
- **Prefix sums of packages:** Segment waste may be computed directly as box capacity minus a package prefix-sum difference; minimizing capacity first avoids needing those prefix sums.
- **Infeasible supplier:** Its largest box cannot hold the largest package, so it must be skipped entirely.
- **Unlimited supply:** The same box size may serve any number of packages even though each supplier's listed sizes are distinct.
- **Exact fits:** A package assigned to an equal-sized box contributes zero waste.
- **Modulo timing:** Compare full supplier totals before applying the modulus; reducing candidates early could change their ordering.
