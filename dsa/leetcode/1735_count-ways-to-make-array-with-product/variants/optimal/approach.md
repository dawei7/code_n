## General
**Translate products into prime exponents**

Factor a query's target as

$$
k = \prod_j p_j^{e_j}.
$$

Each array entry contributes a nonnegative exponent of every prime. For a fixed prime $p_j$, the exponents assigned to the $n$ ordered positions must sum to $e_j$; no other constraint couples those assignments.

**Distribute one exponent with stars and bars**

The number of nonnegative $n$-tuples summing to $e_j$ is

$$
\binom{n+e_j-1}{e_j}.
$$

Assignments for distinct primes are independent, so multiply these binomial coefficients. Every resulting collection of exponent assignments determines exactly one positive-integer array, and every valid array yields exactly one such collection, making the product exact rather than an overcount.

**Factor only as far as necessary**

Trial divisors need only continue while their square is at most the remaining value. After removing all copies of a divisor, any remainder greater than $1$ is one final prime with exponent $1$. The target $k=1$ has no prime factors, so the empty product correctly gives one all-ones array.

## Complexity detail
Trial division takes $O(\sqrt{k})$ time per query in the worst case, while the number of extracted prime exponents is at most logarithmic in $k$. Each exponent is at most $13$ under $k \le 10^4$, so its binomial coefficient is computed in bounded additional work. Across all queries this is $O(Q\sqrt K)$ time. The returned answers use $O(Q)$ space, while factorization uses constant auxiliary state.

## Alternatives and edge cases
- **Enumerate arrays:** Even for modest $n$ and $k$, trying positive values for every position creates an exponential search space.
- **Test every possible divisor through $k$:** This factors primes correctly but takes $O(QK)$ time instead of stopping at the square root.
- **Dynamic programming over products:** Tracking every achievable product for every position uses substantially more time and memory than distributing prime exponents directly.
- **Product one:** Exactly one array is possible, consisting entirely of ones.
- **Array length one:** The sole entry must equal $k$, so every such query has answer one.
- **Prime target:** Its single exponent can be assigned to any one of the $n$ positions, giving $n$ arrays.
- **Repeated queries:** They remain separate output positions even when their answers coincide.
- **Modulo reduction:** Reduce after each multiplication so large intermediate counts do not affect the required result.
