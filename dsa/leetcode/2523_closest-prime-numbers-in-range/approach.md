## General

**Generate every prime through the right endpoint**

To find the closest primes in `[left,right]`, the method first identifies all primes up to `right`. It uses a linear sieve, sometimes called Euler's sieve, even though the manifest summary calls it the Sieve of Eratosthenes.

`st[x]` records whether `x` is known composite. `prime` is a preallocated array that stores discovered primes in increasing order, and `cnt` is the number currently stored.

The outer loop visits integers `i=2` through `right` in ascending order.

**Recognize a new prime**

If `st[i]` is false when `i` is reached, no smaller prime generated `i` as a composite product. Therefore, `i` is prime.

The code writes it to `prime[cnt]` and increments `cnt`. Ascending outer-loop order makes the stored prime list sorted.

**Mark composites with their smallest prime factor**

For each `i`, the inner loop multiplies it by stored primes `prime[j]` while the product remains at most `right`. The condition

`prime[j] <= right//i`

avoids overflow-prone direct boundary multiplication.

It marks `prime[j]*i` composite.

If `prime[j]` divides `i`, the loop breaks. This is the central linear-sieve rule. Continuing to larger primes would mark products whose smallest prime factor was already represented elsewhere. Stopping ensures every composite is generated once by the quotient paired with its smallest prime factor.

For example, 12 is marked as $2\cdot6$. When processing `i=6`, prime 2 divides it and the loop stops, so 12 is not redundantly approached through a larger prime.

**Why the sieve is complete**

Every composite `x` has a smallest prime factor `p` and can be written `x=pq`. When outer loop reaches `q`, `p` is already in the prime list, the product is within range, and no earlier prime dividing `q` causes a break before `p` because `p` is the smallest factor of `x`. Thus `x` is marked.

Every marked value is explicitly a product of integers at least two, so no prime is marked by mistake.

The unmarked values discovered by the outer loop are therefore exactly the primes.

**Filter to the requested interval**

Only `prime[:cnt]` is initialized with real prime values. The list comprehension retains values satisfying `left<=v<=right`, producing sorted list `p`.

Values below `left` were useful for sieving but cannot appear in the answer.

**Only consecutive primes can form the closest pair**

Suppose two interval primes `p_i<p_j` have another prime between them. Then

$$
p_j-p_i
=
(p_{i+1}-p_i)+\cdots+(p_j-p_{j-1}),
$$

so at least one adjacent gap is strictly smaller than the full nonadjacent gap. A minimum-gap pair must therefore be consecutive in sorted prime order.

`pairwise(p)` yields exactly these neighboring pairs.

**Preserve the smallest first prime on ties**

`mi` starts at infinity. A pair replaces `ans` only when `d=b-a` is strictly smaller than `mi`.

Pairs are scanned in ascending `a` order. If a later pair ties the minimum gap, strict `<` does not replace the earlier answer. The retained pair automatically has the smallest `num1`, satisfying the tie rule.

**Handle fewer than two primes**

`ans` begins as `[-1,-1]`. If `p` has zero or one element, `pairwise` yields no pairs and the sentinel is returned unchanged.

**Trace `[10,19]`**

Filtering yields `[11,13,17,19]`. Consecutive gaps are 2, 4, and 2. The first gap sets `ans=[11,13]`. The final gap ties rather than improves, so the earlier pair remains.

**How the break prevents duplicate marking**

If `i` is divisible by current prime `p`, then `p` is the smallest prime factor used for `p*i`. Multiplying `i` by a later prime `q` would create `q*i` whose smallest prime factor is still at most `p`; that composite will be generated from another quotient in its canonical turn. Breaking keeps the inner work linear while leaving every composite covered.

## Complexity detail

Let $R=\texttt{right}$. The Euler sieve marks every composite in its canonical smallest-prime-factor way and runs in $O(R)$ time. Filtering and scanning primes add $O(R)$ worst-case work.

Arrays `st` and `prime` each have length $R+1$, and filtered list `p` contains at most $O(R)$ values. Total auxiliary space is $O(R)$.

The manifest's $O(R\log\log R)$ time describes a classic Eratosthenes sieve, while the exact implementation is linear-sieve $O(R)$.

## Alternatives and edge cases

- **Sieve of Eratosthenes:** Mark multiples from each prime's square in $O(R\log\log R)$ time; simpler but not the exact source.
- **Test each interval number independently:** Trial division can be much slower across a wide range.
- **Fewer than two primes:** Return `[-1,-1]`.
- **Prime 2:** It is handled normally as the first discovered prime.
- **`left=1`:** One is marked neither composite nor returned because the sieve begins at two.
- **Tie gaps:** Strict improvement preserves the smaller first prime.
- **Consecutive-pair scan:** Nonadjacent primes cannot be closest.
- **Overflow-safe product bound:** `prime[j]<=right//i` guards multiplication.
- **Preallocated prime array:** Only its prefix through `cnt` contains valid primes.
- **Manifest mismatch:** The break-on-divisor rule identifies Euler's linear sieve.
