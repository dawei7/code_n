## General
**Divisors arrive in complementary pairs.** Every divisor $d$ of a value $x$ has a partner $x/d$. Apart from a perfect-square root, one member of each pair is at most $\sqrt{x}$ and the other is at least $\sqrt{x}$. It is therefore enough to test candidate divisors from `2` through `isqrt(x)`; `1` and `x` are always the first pair.

Track whether exactly one additional factor pair has been found. When `x % d == 0`, let `other = x // d`. If `d == other`, then $x$ is a perfect square and this unpaired square root prevents the divisor count from being four. Otherwise add both factors to the tentative sum. A second additional pair proves that the value has more than four divisors, so it contributes zero and its scan can stop.

If the scan ends with exactly one distinct additional pair, the complete divisor set is `1`, `x`, `d`, and `x // d`, so the accumulated sum is valid. With no additional pair, the value is prime or one and has too few divisors. Because every possible pair has a representative in the scanned range, ending with exactly one pair also proves that no omitted divisor can create a fifth divisor.

## Complexity detail
For each of the $m$ values, at most $\lfloor\sqrt{x}\rfloor - 1$ candidates are tested. Since $x \le V$, total time is $O(m\sqrt{V})$. The counters and tentative sum occupy $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every integer through the value:** Testing all candidates from $1$ to $x$ is straightforward and correct, but costs $O(mx)$ in the worst case instead of using paired divisors.
- **Prime factorization:** Exactly four divisors occur for $p^3$ or $pq$ with distinct primes. Factoring each number can exploit that characterization, but trial division has the same asymptotic bound and requires more bookkeeping.
- **Perfect squares:** A discovered pair with equal members contributes only one distinct divisor; such a value cannot have exactly four divisors.
- **More than one interior pair:** The value has at least six divisors and must contribute zero rather than a partial sum.
- **Primes and one:** They have fewer than four divisors and contribute zero.
- **Repeated values:** Every array position contributes independently, even when its value occurred earlier.
