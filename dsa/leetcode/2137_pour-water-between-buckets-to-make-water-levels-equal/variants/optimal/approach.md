## General

**Test whether a candidate level is attainable**

For a proposed common level $x$, buckets below $x$ need a total deficit
$\sum\max(0,x-b_i)$. Buckets above $x$ can pour
$\sum\max(0,b_i-x)$ gallons, but only the fraction
$q=1-\texttt{loss}/100$ survives. The level is feasible exactly when the
surviving surplus is at least the deficit.

This condition is monotone. If $x$ is feasible, every lower level is feasible;
raising $x$ increases demand and decreases available supply. Binary-search
between the minimum and maximum initial amounts. At each midpoint, scan all
buckets to compare supply and demand. Keep the feasible half and repeat enough
times to exceed the required $10^{-5}$ accuracy.

Any feasible balance can be realized by pouring from above-level buckets into
below-level buckets, because only total delivered volume matters. Conversely,
no transfer plan can deliver more than the loss-adjusted surplus. The
feasibility test is therefore exact, and binary search converges to the
maximum attainable level.

## Complexity detail

Let $n$ be the bucket count, $R$ the initial level range, and $\varepsilon$ the
precision. Each feasibility scan costs $O(n)$ and binary search needs
$O(\log(R/\varepsilon))$ iterations, for
$O(n\log(R/\varepsilon))$ time. Only scalar totals are stored, so space is
$O(1)$.

## Alternatives and edge cases

- **Repeated pairwise balancing:** Simulating transfers obscures the global
  supply condition and can perform unnecessary work.
- **Redundant feasibility scans:** Recomputing the same total once per bucket
  remains correct but takes quadratic time in $n$.
- With zero loss, the maximum level is the arithmetic mean.
- A single bucket or already equal buckets retain their existing level.
- When every bucket is empty, the answer is zero.
- Near-total loss may make the optimum much closer to the minimum than the
  ordinary mean.
