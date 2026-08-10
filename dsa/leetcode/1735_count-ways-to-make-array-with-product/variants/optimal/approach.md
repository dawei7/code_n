## General

**Factor the target product into independent prime exponents**

For a query `[n,k]`, write

$$
k=\prod_r p_r^{e_r}.
$$

Each of the $n$ positive array entries receives some nonnegative exponent of each prime. For one prime exponent $e$, choosing array values is equivalent to choosing

$$
x_1+x_2+\cdots+x_n=e
$$

with every $x_i\ge0$.

By stars and bars, the number of such distributions is

$$
\binom{e+n-1}{n-1}.
$$

Different primes can be distributed independently, so the query answer is the product of this combination over all prime exponents in $k$.

**Precompute factorials for modular combinations**

The module defines `N = 10020`, slightly above the greatest needed combination argument. With `n<=10000` and `k<=10000`, the largest exponent is at most 13, so `e+n-1<=10012`.

`f[i]` stores $i!$ modulo `MOD`. `g[i]` stores its modular inverse, computed as

`pow(f[i], MOD - 2, MOD)`.

Because `MOD = 10^9+7` is prime and all factorial indices are far below it, Fermat's little theorem makes this inverse valid.

The helper returns

`f[n] * g[k] * g[n-k] % MOD`,

which is $\binom nk$ modulo `MOD`.

**Precompute only exponent lists, not prime identities**

For every integer `i` from one through `N-1`, the module trial-divides a copy `x`. Whenever factor `j` divides it, the inner loop counts its exponent and appends only that count to `p[i]`.

If a prime factor greater than the final trial divisor remains, its exponent is one and one is appended.

Prime identities are unnecessary during query evaluation. Each prime contributes the same stars-and-bars formula based solely on its exponent, and contributions are multiplied.

For example, $660=2^2\cdot3^1\cdot5^1\cdot11^1$, so `p[660]` stores exponents `[2,1,1,1]`.

**Answer one query**

`t` starts at one, the multiplicative identity. For each exponent `x` in `p[k]`, the source multiplies

`comb(x + n - 1, n - 1)`

and reduces modulo `MOD`.

After all prime factors, `t` is appended to the answer list. Queries are independent and remain in input order.

**Why stars and bars constructs actual array values**

For each prime $p_r$, assign exponent $x_{r,i}$ to array position $i$. Define that array value as

$$
a_i=\prod_r p_r^{x_{r,i}}.
$$

The product of all $a_i$ has exponent $\sum_i x_{r,i}=e_r$ for every prime, so it equals $k$. Conversely, every positive array with product $k$ determines exactly these exponent distributions.

This is a bijection, so multiplying independent distribution counts neither misses nor duplicates arrays.

**The $k=1$ case**

One has no prime factors, so `p[1]` is empty. The inner loop performs no multiplication and `t` remains one.

That corresponds to the unique array of $n$ ones.

**Trace `[2,6]`**

$6=2^1\cdot3^1$. For each exponent one distributed across two positions, the count is

$$
\binom{1+2-1}{2-1}=\binom21=2.
$$

The two primes contribute independently, giving $2\cdot2=4$: `[1,6]`, `[2,3]`, `[3,2]`, and `[6,1]`.

## Complexity detail

This exact file performs substantial work once at module import. Factorial construction is $O(N)$. It computes each inverse factorial with a separate modular exponentiation, costing $O(N\log MOD)$ modular multiplications rather than the usual one inverse followed by a backward pass.

Trial-dividing every integer up to $N$ costs a coarse $O(N\sqrt N)$ time. The exponent table, factorial arrays, and inverse-factorial arrays use at least $O(N)$ storage; the collected exponent lists total more than constant per integer in a parameterized view.

After preprocessing, one query visits only the distinct prime-exponent entries of `k`, at most $O(\log k)$ and in practice very small for `k<=10000`. Query-phase time is $O(Q\log K)$ with $O(Q)$ output space.

The manifest's $O(Q\sqrt K)$ time is a loose bound consistent with factoring each query separately, but the exact source precomputes factorizations for all values once. Its $O(Q)$ space describes query output while omitting fixed global tables; parameterized total storage is $O(N+\sum_{i<N}\omega(i)+Q)$.

## Alternatives and edge cases

- **Factor each query on demand:** It avoids the all-values exponent table but costs $O(\sqrt k)$ trial division per query, aligning more directly with the manifest.
- **Cache only requested k values:** Factor each distinct requested product once, balancing preprocessing and repeated queries.
- **Compute inverse factorials backward:** One modular exponentiation at `f[N-1]` followed by linear recurrence reduces preprocessing from $O(N\log MOD)$ to $O(N+\log MOD)$.
- **Dynamic programming over product values:** It is much less direct and can be expensive across large `n`.
- **`k=1`:** Empty factorization yields one array, all ones.
- **`n=1`:** Every exponent must go to the sole slot, so every combination factor is one.
- **Prime k:** Exponent one gives $\binom n{n-1}=n$ placements of the prime among otherwise-one entries.
- **Prime power:** One stars-and-bars factor handles the entire exponent.
- **Several primes:** Their choices multiply because exponent allocations are independent.
- **Modulo reduction:** Multiplying and reducing after every factor preserves the final required remainder.
- **Table bound:** `N=10020` safely covers `n-1+e` under the stated constraints.
- **Global initialization:** It runs when the module is imported, before any `Solution` method call.
- **Prime identities omitted:** Only exponent magnitudes affect the combination count.
