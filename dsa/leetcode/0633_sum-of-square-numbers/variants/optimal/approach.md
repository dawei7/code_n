## General
**Bound both square roots**

Neither component can exceed $\lfloor\sqrt{c}\rfloor$. Start `left` at zero and `right` at that upper bound, so the search begins with the smallest possible first square and largest possible second square.

**Move according to the current sum**

Compare `left ** 2 + right ** 2` with `c`. Equality proves a representation. A sum below `c` can only grow by increasing `left`; a sum above `c` can only shrink by decreasing `right`.

**Why the monotone sweep cannot skip an answer**

For a fixed `right`, every discarded `left` below the current one produces an even smaller sum and therefore cannot reach `c`. For a fixed `left`, every discarded `right` above the current one produces an even larger sum. Each move eliminates only impossible pairs, while both pointers remain within the complete bounded search region. If they cross without equality, no valid pair exists.

**Keep square arithmetic exact**

Use integer square root to initialize the upper pointer. This avoids floating-point rounding near large perfect squares and guarantees that the initial bound is exact.

## Complexity detail
`left` increases at most $floor(\sqrt{c}) + 1$ times and `right` decreases at most that many times. The total running time is $O(\sqrt{c})$, and the two pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **One-root scan with an integer-square test:** enumerate `a` and test whether $c - a^{2}$ is a perfect square; it also achieves $O(\sqrt{c})$ time and $O(1)$ space.
- **Binary search the second root:** search for `b` separately for every `a`; it is correct but costs $O(\sqrt{c} \log c)$ time.
- **Hash set of squares:** store every square through `c` and search for complements in $O(\sqrt{c})$ time, but uses $O(\sqrt{c})$ space.
- **Enumerate both roots:** tests every bounded pair and takes $O(c)$ time.
- $c = 0$ is represented by two zeroes.
- Either component may be zero, so perfect squares must return true.
- The two components may be equal, as in $8 = 2^{2} + 2^{2}$.
- Exact integer arithmetic avoids overflow or rounding traps; fixed-width implementations must widen before squaring.
