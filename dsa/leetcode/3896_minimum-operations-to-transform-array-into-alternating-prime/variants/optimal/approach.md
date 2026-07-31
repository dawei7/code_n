## General

**Minimize every position independently**

An increment changes only the selected element, and the required primality at one index does not depend on any other value. Therefore an optimal transformation chooses the cheapest valid final value for each position and sums those independent costs. No operation spent at one index can reduce the cost at another.

For an even index containing $x$, only prime final values are legal. Because values may only increase, the cheapest choice is the smallest prime $p\ge x$, costing $p-x$. For an odd index, a non-prime value already costs zero. If its value is prime, every odd prime is followed by an even number greater than $2$, so one increment makes it non-prime. The sole exception is $2$: its successor $3$ is also prime, and two increments are required to reach $4$.

**Build primality and every next-prime answer once**

Let $M$ be the maximum input value. Construct an Eratosthenes sieve through `2 * M + 2`. For $M\ge2$, Bertrand's postulate guarantees a prime strictly between $M$ and $2M$, while the small case $M=1$ is covered by the same minimum limit. Thus the sieve always contains a legal prime at or above every input value, including values whose answer exceeds $10^5$.

Scan the completed sieve backward while retaining the nearest prime seen so far. For every value through $M$, store that retained prime in `next_prime[value]`; it is exactly the smallest prime at least as large as the value. At each even index, add `next_prime[value] - value`. At each odd index, consult the sieve flag and apply the zero-, one-, or two-operation rule above.

The chosen final value at every even index is the nearest reachable prime, so no valid transformation can spend fewer increments there. The odd-index rule likewise selects the first reachable non-prime. Since the total is the sum of these position-wise minima, the returned number is globally minimal.

## Complexity detail

Let $N$ be the array length and $M$ its maximum value. The sieve takes $O(M\log\log M)$ time, the backward next-prime scan takes $O(M)$ time, and the array scan takes $O(N)$ time. The total is $O(M\log\log M+N)$. The sieve and next-prime table use $O(M)$ auxiliary space.

The benchmark defines size as $N$ while holding $M=99991$ fixed across its three tiers. The accepted-class method pays the same sieve-domain cost and performs constant work per array position. A correct slower control tests divisors independently for every element, adding $\Theta(N\sqrt M)$ work on these prime-heavy inputs.

## Alternatives and edge cases

- **Sorted prime list:** Materialize all primes and binary-search the first prime not smaller than each even-indexed value. This avoids the second $O(M)$ table but makes each such lookup $O(\log M)$.
- **Per-element trial division:** Testing primality separately for every candidate avoids sieve storage but repeats up to $\Theta(\sqrt M)$ divisor checks per value and is the principal slower approach.
- **Prime value two at an odd index:** Incrementing `2` once reaches `3`, which is still prime; the minimum legal target is `4`, costing two operations.
- **One is non-prime:** An odd-indexed `1` already satisfies its requirement, while an even-indexed `1` needs one increment to become `2`.
- **Prime search beyond the input constraint:** `100000` must advance to `100003`; limiting the sieve to $10^5$ would omit the required target.
- **Zero-based parity:** Index $0$ is even and must contain a prime.
- **Input preservation:** The method computes costs without mutating `nums`.
