## General

**Classify one pair for every target.** For a mirrored pair with values $a$ and $b$, let $d=\lvert a-b\rvert$. Target $X=d$ costs zero changes. After changing one endpoint to any value in $[0,k]$, the largest attainable difference is

$$
T=\max\bigl(a,b,k-a,k-b\bigr).
$$

Consequently, every $X\leq T$ costs at most one change, while $X>T$ requires changing both endpoints. This gives a simple cost profile: zero at $d$, one throughout $[0,T]$ except at $d$, and two throughout $(T,k]$.

**Sweep savings instead of costs.** Begin conceptually with two changes for every pair and target. A pair saves one change on the entire interval $[0,T]$ and saves one additional change at the single point $d$. Record those contributions in a difference array using two range updates. A prefix sum then gives the total savings for each target $X$.

If there are $n/2$ pairs, the baseline is $n$ changes. Subtracting the largest savings seen during the sweep yields the minimum cost. Every pair's profile is exact, so summing profiles and choosing their least-cost common target considers every possible $X$.

## Complexity detail

Processing the $n/2$ mirrored pairs takes $O(n)$ time, and sweeping targets $0$ through $k$ takes $O(k)$ time. The difference array has $k+2$ entries, so auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Try every target against every pair:** This directly evaluates the same cost rule but takes $O(nk)$ time.
- **Choose the most frequent current difference:** Frequency alone ignores whether other pairs need one or two changes to reach that target.
- A pair already at the selected target requires no replacement.
- Target `0` is valid and means every mirrored pair must contain equal values.
- When `k = 0`, every value is already zero and the answer is zero.
- The one-change limit depends on both moving an endpoint upward toward `k` and downward toward `0`.
