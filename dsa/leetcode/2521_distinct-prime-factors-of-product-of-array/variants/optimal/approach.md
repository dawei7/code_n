## General

**Factor the elements instead of the product**

Multiplying all values is unnecessary and would create a very large integer. A prime divides the full product exactly when it divides at least one element, so the answer is the union of the elements' prime-factor sets. Maintain one set `factors` across the entire array and factor each `number` independently.

**Remove every copy of a discovered factor**

Try candidate divisors beginning at $2$. When `divisor` divides the current remainder, insert it into `factors`, then divide it out repeatedly. Removing the full prime power prevents duplicate work and ensures that the remaining value has no factor smaller than the next candidate.

Continue while `divisor * divisor <= number`. If the remainder is greater than $1$ afterward, it must be prime: a composite remainder would have a factor no larger than its square root and would already have been found. Insert that final remainder as well. Every inserted value is therefore prime, every prime factor of every input value is eventually inserted, and set uniqueness makes the returned size exactly the number of distinct prime factors of the product.

## Complexity detail

For one value no larger than $M$, trial division tests at most $O(\sqrt{M})$ candidates. Across $n$ values, the time complexity is $O(n\sqrt{M})$. The shared set contains $p$ distinct prime factors, so the auxiliary space complexity is $O(p)$.

## Alternatives and edge cases

- **Construct the full product first:** It preserves the mathematical factor set, but the product can contain tens of thousands of digits and provides no algorithmic benefit.
- **Sieve primes through $M$:** Precomputing all primes up to $M$ and testing which divide an input is valid, but it adds preprocessing and storage that are unnecessary under the small per-value bound.
- **Test every possible divisor:** Scanning all candidates through each value can still be correct when primality is checked, but it takes $O(nM)$ time instead of stopping at square roots.
- Repeated values, repeated prime powers, and primes shared by several elements contribute only once because `factors` is a set.
- A value that remains greater than $1$ after trial division is itself prime and must be recorded; omitting this step fails for prime inputs and large prime factors.
