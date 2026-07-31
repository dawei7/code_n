## General

The answer requires many primality queries over the same bounded interval. Testing each candidate independently would repeat divisibility work, so first compute primality for every integer from $0$ through `n` with the Sieve of Eratosthenes.

Create a byte array whose entries initially mark every value as potentially prime, then clear $0$ and $1$. Process each still-marked candidate $p$ through $\lfloor\sqrt n\rfloor$. All smaller multiples of $p$ were already handled by smaller prime factors, so marking can begin at $p^2$. Clearing `p * p, p * p + p, ...` removes exactly the composites divisible by $p$. After all such $p$ are processed, an index remains marked precisely when it is prime.

Now enumerate `first` from $2$ through $\lfloor n/2\rfloor$. Restricting the scan to half the target enforces `first <= n - first`, so each unordered pair appears exactly once. Constant-time sieve lookups determine whether both `first` and `n - first` are prime. Appending discoveries during this increasing scan automatically produces the required order.

The sieve is correct because every composite $c \leq n$ has a prime factor at most $\sqrt c \leq \sqrt n$ and is therefore cleared when that factor is processed, while no marking step ever clears a prime. The final scan consequently includes exactly the requested pairs.

## Complexity detail

Let the input value itself be $n$. Sieve marking takes $O(n \log\log n)$ time, and the subsequent half-range scan takes $O(n)$ time. The combined bound is $O(n \log\log n)$. The returned pairs add output-sensitive storage, while the primality table requires $O(n)$ auxiliary space; the manifest records $O(n)$ space.

The benchmark tiers use increasing even targets. A correct slower comparison tests primality by trial division for candidate pairs and completes every tier, but its repeated square-root work scales substantially worse than the one-time sieve.

## Alternatives and edge cases

- **Trial division for every pair candidate:** This avoids a table but repeats divisor checks and can take $O(n\sqrt n)$ time across the half-range scan.
- **List all primes then use two pointers:** This is correct after sieve construction, but the extra prime list is unnecessary because direct table lookups already test complements in constant time.
- **Small targets:** Values below $4$ have no representation as a sum of two primes; the initialized table and empty scan handle them naturally.
- **Equal pair members:** When `n` is twice a prime, the pair `[n / 2, n / 2]` is valid and must appear once.
- **Odd targets:** Since $2$ is the only even prime, an odd target has at most the pair `[2, n - 2]`.
- **Ordering and duplicates:** Scanning only through $\lfloor n/2\rfloor$ prevents reversed duplicates and yields increasing first coordinates.

