## General

**One operation replaces a number by its smallest prime factor.** Let $x$ be composite and let $p$ be its smallest prime factor. Its greatest proper divisor is $x/p$: any larger proper divisor would correspond to a smaller factor than $p$. Dividing $x$ by that greatest proper divisor therefore gives

$$
\frac{x}{x/p}=p.
$$

For a prime $x$, the greatest proper divisor is one, so the operation leaves $x$ unchanged. Thus each element has only two useful states: its original value or its smallest prime factor. Repeating the operation after reaching a prime cannot reduce it further.

**Precompute smallest prime factors.** Global array `lpf` is filled by a sieve. When an unmarked `i` is encountered, it is prime. The inner loop visits its multiples and writes `i` only into still-unmarked entries. Because primes are processed ascending, the first factor written is the smallest prime factor.

This work occurs when the module is loaded, not inside `minOperations`. All method calls reuse the table.

**Process constraints from right to left.** A non-decreasing array needs `nums[i] <= nums[i+1]`. Starting at the second-last element means the right neighbor has already been finalized. If the current value already fits, changing it would add an unnecessary operation and can only make it smaller, so the source leaves it alone.

If `nums[i] > nums[i+1]`, some reduction is mandatory. The only useful reduction sets it to `lpf[nums[i]]`, the smallest value reachable by operations. If even that value remains larger than the finalized neighbor, no operation sequence can repair this pair and the method returns `-1`. Otherwise exactly one operation is both sufficient and necessary, so `ans` increases.

**Why local greedy decisions are globally safe.** Reducing an element can make its relation to the element on its left easier, because the left element must be no greater than it; a smaller right bound is actually stricter for the left. Could reducing unnecessarily hurt? The source reduces only when the current pair is already invalid, so every valid solution must change this current element. Its post-operation value is forced to the smallest prime factor. There is no alternative intermediate divisor result.

Inductively, the suffix to the right is non-decreasing and uses the minimum mandatory operations. The current comparison either needs no action or has one forced action. Failure after the forced reduction proves impossibility. This establishes minimality.

For `[25,7]`, 25 exceeds 7, its smallest prime factor is 5, and one operation creates `[5,7]`. For `[7,7,6]`, the middle prime 7 exceeds 6 but maps to itself, so impossibility is detected.

**Input mutation and global cost.** The source overwrites every reduced `nums[i]`. Callers therefore see the transformed array on success and a partially transformed array if the method returns `-1` late. The sieve also allocates and computes a table slightly above $10^6$ at import time.

## Complexity detail

Let $U=10^6$ be the supported maximum. The smallest-prime-factor sieve takes $O(U\log\log U)$ conventional sieve time and $O(U)$ space. Once initialized, one method call scans the array once in $O(n)$ time and uses $O(1)$ additional working space while mutating the input.

Including shared preprocessing, the manifest's $O(U\log\log U+n)$ time and $O(U+n)$ accounting is conservative; the method does not allocate a new $O(n)$ array, though the input itself occupies that space.

## Alternatives and edge cases

- **Factor each violating value on demand:** Trial division costs up to $O(\sqrt U)$ per changed element but avoids the large global sieve for few calls.
- **Linear sieve:** It can compute smallest prime factors in $O(U)$ time with comparable storage.
- **Process left to right:** Future right values are not finalized, making greedy decisions unclear. Right-to-left directly enforces each required upper bound.
- **Prime violating value:** Its smallest prime factor equals itself, so it cannot be reduced and the answer is `-1`.
- **Value one:** It never exceeds a positive right neighbor when that neighbor is at least one, so the zero `lpf[1]` entry is not used for a required reduction.
- **Already non-decreasing:** No values change and the method returns zero.
- **Composite becomes its smallest prime:** A second operation cannot reduce that prime, so at most one useful operation per index exists.
- **Equal neighbors:** Equality is permitted and triggers no operation.
- **Partial mutation on failure:** Earlier right-side reductions remain in `nums` when a later impossible pair returns `-1`.
- **Global initialization:** Sieve cost is paid on module import even if the method is never called.
- **Upper-bound dependency:** Access is safe only because all values are at most $10^6$.
- **Minimum count:** Every performed operation repairs a pair that was otherwise invalid, so none of the counted operations can be omitted.
- **Greatest-divisor wording:** The operation may look as though many divisors must be considered, but the quotient is forced to the smallest prime factor. Establishing this equivalence is what collapses repeated-operation search into one greedy check.
