## General

**Ask whether one candidate maximum is sufficient**

Fix a candidate maximum $x$ and consider only the integers from $1$ through $x$. The first array may use every value except a multiple of `divisor1`, so it has

$$
x-\left\lfloor\frac{x}{\texttt{divisor1}}\right\rfloor
$$

eligible values. The analogous count for the second array replaces `divisor1` with `divisor2`. Each count must reach its corresponding requested size.

Those two checks alone can count the same flexible values for both arrays. Let $L=\operatorname{lcm}(\texttt{divisor1},\texttt{divisor2})$. Only multiples of $L$ are forbidden from both arrays, so the number of values usable by at least one array is

$$
x-\left\lfloor\frac{x}{L}\right\rfloor.
$$

This union must contain at least `uniqueCnt1 + uniqueCnt2` values. The two individual capacity checks and this combined capacity check are also sufficient: values usable by only one array can be assigned there first, and the remaining values usable by both fill whichever requested places remain. These are exactly the capacity conditions for two disjoint selections.

**Binary-search the first feasible maximum**

All three counts are non-decreasing as $x$ grows. Consequently, feasibility changes at most once from false to true, and the first true value is the requested minimum maximum.

Search from `1` through `2 * (uniqueCnt1 + uniqueCnt2)`. This upper bound is always feasible because each divisor is at least $2$: at least half of the prefix is eligible for either individual array, and at least half is usable by their union. A feasible midpoint keeps the lower half; an infeasible midpoint discards it. The remaining endpoint is the smallest feasible maximum.

## Complexity detail

Let $C=\texttt{uniqueCnt1}+\texttt{uniqueCnt2}$ and $D=\min(\texttt{divisor1},\texttt{divisor2})$. Euclid's algorithm computes the greatest common divisor, and hence the least common multiple, in $O(\log D)$ time. Binary search performs $O(\log C)$ constant-time feasibility checks. Total time is $O(\log D+\log C)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Linear candidate search:** Testing maximums `1, 2, 3, ...` with the same predicate is correct but takes $O(C)$ checks in the worst case instead of logarithmically many.
- **Greedy explicit construction:** Assigning actual integers can establish feasibility, but it performs work proportional to the answer and makes contention over values eligible for both arrays harder to reason about.
- **Only individual counts:** Verifying each array separately is insufficient because both checks may rely on the same integers; the least-common-multiple union condition enforces disjointness.
- **Equal divisors:** Both arrays draw from exactly the same eligible pool, so the combined condition becomes the decisive one.
- **One divisor divides the other:** The least common multiple is the larger divisor; computing it through the greatest common divisor handles this without a special case.
- **Very large requested counts:** The answer may approach $2\cdot10^9$, so enumerating values is impractical but binary search still needs only about 31 iterations.
