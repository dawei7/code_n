## Description

You have `n` unique candies and `k` bags. You want to distribute **all** the candies into the bags such that every bag contains **at least** one candy.

There is no order among the bags (the bags are unlabeled), and the candies inside each bag are unordered.

Return *the number of ways to distribute the candies*. As the answer may be large, return it **modulo** $10^9 + 7$.

### Mathematical Relation

The number of ways to partition a set of $n$ distinct elements into $k$ non-empty unlabeled subsets is given by the Stirling numbers of the second kind, $S(n, k)$, satisfying the recurrence relation:

$$
S(n, k) = k \cdot S(n - 1, k) + S(n - 1, k - 1)
$$

with base conditions $S(0, 0) = 1$ and $S(n, 0) = S(0, k) = 0$ for $n, k > 0$.
