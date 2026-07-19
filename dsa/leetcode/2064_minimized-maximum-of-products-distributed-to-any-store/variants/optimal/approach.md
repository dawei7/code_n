## General
**Turn a proposed maximum into a feasibility test**

Suppose no store may receive more than a positive limit $x$. A product type with quantity $q$ then needs exactly $\lceil q/x\rceil$ stores: fewer cannot hold all its units, and that many suffice by splitting the type. The limit is feasible precisely when the sum of these requirements over all types is at most $n$.

**Exploit the monotone boundary**

If a limit is feasible, every larger limit is also feasible; if it is infeasible, every smaller one is infeasible. Binary-search the first feasible integer between $1$ and $Q$. For a midpoint, compute each ceiling as `(quantity + limit - 1) // limit`. Move the upper boundary to the midpoint when the required-store sum fits, and otherwise discard the midpoint and everything below it.

The feasibility calculation is both necessary and sufficient because stores assigned to different types never need to mix their products. Binary search preserves the first feasible value inside its interval, so when the boundaries meet, that value is exactly the minimum achievable maximum.

## Complexity detail
Each feasibility test scans all $m$ quantities in $O(m)$ time, and binary search performs $O(\log Q)$ tests. The total time is $O(m\log Q)$. Apart from the search boundaries and running store count, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Test limits in increasing order:** The same feasibility test is correct, but trying every value through $Q$ can take $O(mQ)$ time.
- **Priority-queue splitting:** Repeatedly give another store to the type with the largest current share can model the choices, but it needs more bookkeeping and can be slower when many spare stores exist.
- When $m=n$, every type must fit in one store, so the answer is $Q$.
- A type may occupy several stores, but no store may combine even small leftovers from two types.
- Unused stores are allowed; feasibility requires at most $n$ stores rather than exactly $n$.
- Ceiling division is essential when a quantity is not divisible by the tested limit.
