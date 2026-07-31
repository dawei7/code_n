## General

**Turn a portion size into a feasibility test**

For a positive candidate size $x$, a pile of size $c$ can supply $\lfloor c/x\rfloor$ children. Summing this quantity across all piles determines whether at least `k` equal portions exist. Remainders may be discarded, and no term combines two original piles.

**Exploit monotonicity**

If size $x$ is feasible, every smaller positive size is feasible. If it is not feasible, no larger size can work. Binary-search this monotone boundary. A valid answer cannot exceed either the largest pile or the total candies divided by `k`, which supplies a tighter upper bound and becomes zero immediately when even size one is impossible.

On a feasible midpoint, remember it and search higher; otherwise search lower. When the interval closes, the remembered value is feasible and every larger candidate has been rejected, proving it is maximal.

## Complexity detail

Let $n=\lvert\texttt{candies}\rvert$ and $V=\max(\texttt{candies})$. Each feasibility test scans all piles in $O(n)$ time, and binary search performs $O(\log V)$ tests, for $O(n\log V)$ total time.

Only scalar search bounds and counters are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Test every portion size:** Scanning candidates one by one can take $O(nV)$ time.
- **Sort and distribute greedily:** Pile order does not reveal the optimal equal portion because every pile may create several portions.
- **Merge total candies:** Dividing the total by `k` is only an upper bound; it can be unattainable because different piles cannot be combined.
- **Too many children:** When the total candy count is below `k`, the answer is zero.
- **One child:** The largest original pile is the best allocation because merging is forbidden.
- **Unused remainder:** A pile need not be divisible by the chosen portion size.
- **Very large `k`:** Feasibility counts must support values beyond 32-bit range.
