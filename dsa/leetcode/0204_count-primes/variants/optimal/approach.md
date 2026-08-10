## General

**Treat every index as a candidate number**

The solution allocates `primes = [True] * n`. Index `x` represents integer
`x`, and a true value means no smaller processed prime has yet proved `x`
composite.

Indices 0 and 1 also begin true, even though neither is prime. This causes no
incorrect count because the outer loop starts at 2 and never examines those
indices. A more explicit sieve might initialize them false, but the exact code
does not need to.

**Scan candidates in increasing order**

For every `i` from 2 through `n - 1`, the algorithm checks `primes[i]`. If the
entry is false, some earlier prime marked `i` as a multiple, so it is composite
and is skipped.

If the entry is still true, `i` is prime. The proof comes from the smallest
prime factor: if `i` were composite, it would have a factor smaller than `i`,
and that factor's marking pass would already have set this entry false. The
algorithm therefore increments `ans` exactly at prime indices.

Scanning only through `n - 1` enforces the exclusive upper bound. Even if `n`
itself is prime, it has no array index in this length-$n$ list and is not
counted.

**Mark all later multiples of a discovered prime**

For a prime `i`, the inner range begins at `i + i`, advances by `i`, and stops
before `n`. These values are `2i, 3i, 4i, ...`, each divisible by `i` with a
second factor at least two, so every marked value is composite.

The prime `i` itself is not marked because marking begins at twice its value.
Some composite entries are written false many times; for example, 30 is a
multiple of 2, 3, and 5. Repeatedly assigning false does not change correctness,
though it adds work.

**Trace `n = 10`**

Index 2 is true, so the answer becomes one and indices 4, 6, and 8 are marked.
Index 3 is true, so the answer becomes two and indices 6 and 9 are marked.
Index 4 is false and skipped.

Index 5 remains true, increasing the answer to three; its first multiple 10 is
outside the half-open interval. Index 6 is false, index 7 is true and raises the
answer to four, and indices 8 and 9 are false. The returned count is 4 for
primes 2, 3, 5, and 7.

**Why every counted value is prime**

Suppose the scan counts some composite `i`. Let $p$ be its smallest prime
factor. Then $p < i$, so the outer loop processed $p$ earlier. Since
`i = kp` for integer $k \ge 2$, the inner range for $p$ includes `i` and would
have marked it false. This contradicts the fact that it was counted.

Therefore no composite can contribute to `ans`.

**Why every prime below `n` is counted**

A prime has no representation `kp` with both $k \ge 2$ and earlier prime
$p$. None of the marking loops can include it. Its entry remains true until its
own outer iteration, where the solution increments `ans`. Since every integer
from 2 through `n - 1` is visited, no eligible prime is missed.

**Exact source differs from the manifest summary**

The manifest says the method uses a `bytearray` and starts each prime's marking
at its square. The exact file uses a Python list of booleans and starts at
`2*i`. It also lets the outer loop run to `n - 1` rather than stopping near
$\sqrt n$.

Starting at `i*i` is a valid optimization because smaller multiples already
have a smaller factor and were marked earlier. The stored code instead repeats
some safe markings. Its explanation must reflect that actual choice rather than
attribute an optimization it does not contain.

**Count during discovery instead of summing afterward**

Many sieves mark all composites first and then count true entries in a final
pass. This method increments `ans` immediately whenever it discovers a prime.
That avoids a separate summation pass, although the outer scan already visits
all relevant indices.

**Small bounds work without special cases**

For `n` equal to 0, 1, or 2, the outer range is empty and `ans` remains zero.
The list allocation is valid for each nonnegative constraint value. No access
to indices 0 or 1 occurs.

## Complexity detail

The outer scan is $O(n)$. For each prime $p<n$, the inner loop performs roughly
$n/p$ markings. Summed over primes, this is $O(n\log\log n)$ by the standard
prime harmonic bound. Starting at `2p` repeats more previously known markings
than starting at $p^2$, but it remains within the same asymptotic sieve class.

The boolean list contains $n$ Python references/values, so auxiliary space is
$O(n)$. It is not the compact bytearray described in the manifest, though both
have linear asymptotic size.

## Alternatives and edge cases

- **Square-start sieve:** Begin marking at `p*p` and stop outer candidate processing near $\sqrt n$; avoids redundant writes.
- **Bytearray slicing:** Compact storage and C-level bulk marking can be substantially faster in Python.
- **Odd-only sieve:** Store only odd candidates and treat 2 separately, as the competitive variant effectively does.
- **Linear sieve:** Record smallest prime factors so each composite is generated once; $O(n)$ time but more bookkeeping.
- **Trial division per number:** Uses less sieve storage but is too slow near five million.
- **`n <= 2`:** No primes are strictly below the bound.
- **Prime `n`:** Excluded because the range is `[0,n)`.
- **Repeated marking:** Safe because false assignment is idempotent.
- **Indices 0 and 1:** Remain true internally but are never scanned or counted.
- **Manifest mismatch:** Exact source is a boolean-list, `2p`-start sieve, not a bytearray square-start implementation.
