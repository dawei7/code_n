## General

Let $n$ be the string length and $z$ its number of zeros. After $t$ operations, every initial zero must have been flipped an odd number of times, while every initial one must have been flipped an even number of times. Because each operation flips exactly $k$ distinct indices, the sum of all per-index flip counts is exactly $tk$.

The minimum possible total with the required final parities is $z$: flip every zero once and every one zero times. Hence every feasible $t$ satisfies $tk\ge z$ and the parity condition

$$
tk\equiv z\pmod 2.
$$

**Even operation count.** If $t$ is even, a zero's largest allowed odd count is $t-1$, while a one's largest even count is $t$. The maximum compatible total is therefore

$$
z(t-1)+(n-z)t=nt-z.
$$

Thus $tk\le nt-z$, or equivalently $t(n-k)\ge z$. Since $tk$ is even, this branch also requires even $z$. The smallest even candidate is the smallest even integer at least both $\lceil z/k\rceil$ and $\lceil z/(n-k)\rceil$.

**Odd operation count.** If $t$ is odd, a zero may be flipped at most $t$ times and a one at most $t-1$ times. The maximum is

$$
zt+(n-z)(t-1)=nt-(n-z).
$$

This gives $t(n-k)\ge n-z$. The parity condition becomes $z\equiv k\pmod2$. The smallest odd candidate is the smallest odd integer at least $\lceil z/k\rceil$ and $\lceil(n-z)/(n-k)\rceil$.

These bounds are sufficient, not only necessary. Start with flip counts one for every zero and zero for every one. The desired total differs from $z$ by an even amount, and the maximum inequalities guarantee enough capacity to add flips in pairs without exceeding $t$ or violating any index's parity. The resulting column counts are at most $t$ and sum to $tk$.

They can be scheduled into $t$ operations of $k$ distinct indices: view operations and indices as the two sides of a bipartite graph, with every operation needing degree $k$ and each index needing its chosen flip count. For fewer than $k$ indices, their total demand is at most $t$ per index; for at least $k$, demand is at most the global $tk$. These capacity conditions establish a valid incidence schedule.

Handle $k=n$ separately because $n-k=0$: every operation flips the whole string, so a non-complete string is solvable only when all bits are zero, in one operation. Return the smaller feasible parity candidate, or `-1` if neither exists.

## Complexity detail

Counting the zeros in a length-$n$ string takes $O(n)$ time. All parity checks, ceiling divisions, and candidate adjustments take constant time, so total time is $O(n)$. The method stores only scalar counts and candidates, using $O(1)$ auxiliary space.

The benchmark defines its size as $n$ and uses $z=k=n/2$. The accepted formula scans the string once. A calibrated correct alternative performs BFS over possible zero counts and enumerates every legal mix of zero and one flips from each state, producing quadratic worst-case work while returning the same minimum.

## Alternatives and edge cases

- **BFS over zero counts:** The next zero count depends only on the current count and how many selected indices are zeros, but exploring all transitions costs $O(n^2)$ in the worst case.
- **BFS over bit strings:** This has up to $2^n$ states and is unnecessary because positions with equal current bits are symmetric.
- **Already all ones:** Return zero without performing an operation.
- **k equals n:** Only the all-zero string can reach all ones from a non-target state.
- **Parity mismatch:** If neither the even nor odd branch matches $z$, the target is unreachable.
- **Exactly one zero:** Depending on $k$ and $n-k$, correcting it may require several operations rather than one.
- **Arrangement of bits:** Only the number of zeros matters; their positions do not change feasibility or the minimum.
- **Ceiling bounds:** Round each branch upward to its required parity after taking the maximum lower bound.
