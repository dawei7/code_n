## General

**Notice that the allowed sums are prefixes, not arbitrary prime ranges**

The consecutive sequence must start at 2. If the primes are

$$
p_1=2,\ p_2=3,\ p_3=5,\ldots,
$$

then the only candidate sums are

$$
S_j=p_1+p_2+\cdots+p_j.
$$

There is no choice of a later starting prime. Once the prime sequence is known, the candidates form one strictly increasing list of prefix sums. The task becomes: keep the prefix sums that are themselves prime, then find the largest retained value not exceeding `n`.

**Precompute primality through the fixed domain limit**

The source sets `mx = 500000`, the maximum legal input, and creates a Boolean array `is_prime` of length `mx + 1`. It explicitly marks zero and one false because neither is prime.

It then performs a Sieve of Eratosthenes. For each `i` from 2 through `mx`:

- if `is_prime[i]` is still true, `i` is appended to `primes`;
- every multiple from `i*i` onward is marked false.

Starting at `i*i` is sufficient. A smaller multiple `i*q` with `q<i` already has the smaller factor `q` and was marked during an earlier sieve step. Avoiding those repeated writes is what gives the sieve its near-linear $O(M\log\log M)$ behavior.

If `i*i > mx`, Python's range is empty, but `i` is still correctly appended when it remains prime. By the time the scan reaches such an `i`, every possible composite has already been marked by a factor no larger than its square root.

After this loop, `is_prime[x]` answers primality for every value in the legal domain, and `primes` contains those primes in increasing order.

**Build only prime prefix sums**

The source initializes cumulative total `t=0` and result-candidate list `s=[0]`. It then visits the prime list in order:

`t += x`

adds the next consecutive prime, so after processing `p_j`, `t=S_j`.

If `t > mx`, the loop stops. All primes are positive, so every later prefix sum would be even larger and also outside every legal query.

When `t <= mx`, the sieve lookup `is_prime[t]` determines whether this allowed sum is itself prime. Only prime totals are appended to `s`.

For the first few prefixes:

- $2=2$ is prime and is stored;
- $2+3=5$ is prime and is stored;
- $2+3+5=10$ is composite and is skipped;
- $2+3+5+7=17$ is prime and is stored.

Skipping a composite prefix sum does not reset `t`. The next candidate must still include every consecutive prime from 2, so accumulation continues from the same running total.

**Use zero as a safe no-answer sentinel**

Zero is deliberately placed at the front of `s` even though it is not prime. It represents the required return value when no prime prefix sum is at most `n`.

Every real appended candidate is positive, and cumulative sums strictly increase. Therefore `s` is sorted as

`[0, valid_candidate_1, valid_candidate_2, ...]`.

This sentinel avoids a separate branch for `n=1`. Since legal `n` is at least one, zero is always a valid fallback position in the list.

**Answer by finding the rightmost candidate within the bound**

`bisect_right(s, n)` returns the insertion position after every value less than or equal to `n`. Subtracting one produces the index of the rightmost existing value satisfying the bound.

For `n=20`, the relevant candidate prefix is `[0,2,5,17]`. The insertion point lies after 17, so the method returns 17.

For `n=2`, `bisect_right` moves past the stored 2, and the result is 2. For `n=1`, it moves past only the zero sentinel, so index zero is returned and the answer is 0.

**Why preprocessing and binary search cover the exact answer**

The sieve labels every integer through 500,000 correctly. The cumulative loop visits every consecutive-prime prefix sum in increasing length until the first one above that same limit. Because subsequent sums can only grow, no candidate relevant to a legal query is omitted.

The list `s` contains a value exactly when it is either the sentinel or a prefix sum that the sieve certifies prime. Binary search returns its greatest member at most `n`. Thus the returned positive values satisfy all three requirements—prime, consecutive-prime sum starting from 2, and at most `n`—and no larger qualifying value can have been skipped.

**Distinguish fixed global preprocessing from per-query work**

The sieve and candidate construction live at module scope, outside the method. They run once when the solution module is loaded, regardless of the particular `n` later supplied. The method itself performs only one binary search.

The manifest describes sieving “through `n`.” Conceptually that leads to the same answer, but the exact source always precomputes through the fixed maximum 500,000. This should be visible in both the algorithm narrative and its detailed resource accounting.

## Complexity detail

Let $M=500000$ be the fixed preprocessing limit and let $C$ be the number of stored prime prefix-sum candidates, including the sentinel.

The sieve takes $O(M\log\log M)$ time and $O(M)$ Boolean storage. Scanning the primes and building prefix sums is at most $O(M)$ iterations in a loose bound and is dominated by the sieve. The `primes` and `s` lists together also use $O(M)$ worst-case storage.

One call to `largestPrime` takes $O(\log C)$ time for `bisect_right` and $O(1)$ additional space.

Including module initialization, the exact source costs $O(M\log\log M)$ time and $O(M)$ space, followed by $O(\log C)$ per query. If an implementation instead sized the sieve to the input $N$, this would be written as $O(N\log\log N)$ time and $O(N)$ space, matching the manifest. Here the source chooses the fixed legal ceiling so the precomputed tables can be reused.

## Alternatives and edge cases

- **Trial-divide every potential value:** Repeated primality checks are simpler for tiny bounds but much slower than one shared sieve across the full domain.
- **Sieve only through the current `n`:** This saves work for a single small query and matches the manifest wording, but does not reuse a fixed global table.
- **Sum an arbitrary consecutive prime interval:** That solves a different problem; the required sequence always starts from 2.
- **Reset after a composite prefix sum:** Composite status of one total does not end the sequence. Later, longer prefix sums may be prime, as 10 is followed by 17.
- **Return the largest prime at most `n`:** A prime is eligible only if it is also one of the cumulative sums from 2.
- **`n=1`:** No positive candidate fits, so the zero sentinel is returned.
- **`n=2`:** The one-term sum 2 qualifies.
- **Bound between candidates:** Binary search returns the previous stored candidate, not the insertion position itself.
- **Bound exactly equal to a candidate:** `bisect_right` places the insertion point after equal values, so that candidate is included.
- **Prefix sum above 500,000:** The construction stops permanently because all later sums are larger.
- **Zero in `s`:** It is a fallback marker, not a claim that zero is prime.
- **Repeated method calls:** They share the already-built read-only sieve and candidate list.
- **Inputs above the documented ceiling:** The fixed table is not designed to establish correctness beyond 500,000.
- **Module initialization cost:** It is paid before the method call and must not be mistaken for an $O(\log C)$ complete-program cost.
