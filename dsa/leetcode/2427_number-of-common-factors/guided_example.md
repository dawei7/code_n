# Guided Example: Number of Common Factors

## 1. The instance and what must be counted

Take $a = 12$ and $b = 6$. The required answer is `4`, because exactly four
positive integers divide both inputs. The whole lesson is about counting that set
without ever testing the two inputs separately for each candidate.

Two definitions must be kept apart:

- a **divisor** of $a$ is a positive integer $x$ with $a \bmod x = 0$;
- a **common factor** of $a$ and $b$ is a positive integer $x$ with
  $a \bmod x = 0$ **and** $b \bmod x = 0$.

The second condition is a conjunction, so the answer is the size of an
intersection, not the size of either factor set.

| $x$ | Divides 12? | Divides 6? | Common factor? |
|---|---|---|---|
| 1 | yes | yes | yes |
| 2 | yes | yes | yes |
| 3 | yes | yes | yes |
| 4 | yes | no | no |
| 6 | yes | yes | yes |
| 12 | yes | no | no |

There are $1, 2, 3, 6$, so the count is four. Notice how two of the six divisors of
12 fall away, and none of the divisors of 6 is outside the divisor set of 12,
because $6$ divides $12$.

## 2. Two divisibility conditions collapse into one

Let $\gcd(a, b)$ be the greatest common divisor. The key structural fact is

$$
x \mid a \ \text{ and } \ x \mid b
\quad\Longleftrightarrow\quad
x \mid \gcd(a, b).
$$

*Forward direction.* Any common divisor $x$ divides every integer combination
$ua + vb$ with integers $u, v$. Euclid's algorithm produces $\gcd(a,b)$ as exactly
such a combination, so $x$ divides it.

*Reverse direction.* The gcd divides $a$ and divides $b$ by definition, so any
divisor of the gcd is a divisor of both inputs.

The two directions are precisely `soundness` and `completeness` for this
reduction: nothing is included that is not common, and nothing common is left
out. The counting problem therefore becomes "how many positive divisors does
$g = \gcd(a,b)$ have", and the only candidate values that must be examined are
$1, 2, \dots, g$. No candidate above $g$ can be common, because the largest
possible common factor is the gcd itself.

## 3. Obtaining the gcd with Euclid's algorithm

Euclid's identity

$$
\gcd(a, b) = \gcd(b,\ a \bmod b)
$$

preserves the common divisor set while shrinking the numbers: $a \bmod b$ is a
divisor-preserving combination of $a$ and $b$, and the pair strictly decreases
whenever the remainder is nonzero. Repeating until the remainder is zero leaves
the answer as the last nonzero value.

| Step | Pair | Division with remainder | New pair |
|---|---|---|---|
| 1 | $(180, 48)$ | $180 = 3 \cdot 48 + 36$ | $(48, 36)$ |
| 2 | $(48, 36)$ | $48 = 1 \cdot 36 + 12$ | $(36, 12)$ |
| 3 | $(36, 12)$ | $36 = 3 \cdot 12 + 0$ | remainder zero, stop |
| 4 | — | $\gcd(180, 48) = 12$ | — |

Both inputs are positive and at least 1, so the gcd is at least 1 and the
candidate range $1 \dots g$ is never empty. There is no zero case to special-case.

## 4. Worked trace of the instance

For $a = 12$ and $b = 6$, the first division already terminates:
$12 = 2 \cdot 6 + 0$, so $g = 6$. Every candidate from 1 through $g$ is then tested
once for divisibility of $g$.

| $x$ | $g \bmod x$ for $g = 6$ | Counts as a factor? | Running count |
|---|---|---|---|
| 1 | 0 | yes | 1 |
| 2 | 0 | yes | 2 |
| 3 | 0 | yes | 3 |
| 4 | 2 | no | 3 |
| 5 | 1 | no | 3 |
| 6 | 0 | yes | 4 |

The scan includes both endpoints, and both are essential. The value 1 divides
every positive integer, and $g$ always divides itself, so a scan that stopped
before $g$ would undercount by one.

The same scan applied to the gcd $12$ of the pair $(48, 180)$ produces six
factors: $1, 2, 3, 4, 6, 12$. Whether the gcd is large or small, the procedure is
identical; only the number of candidates changes.

## 5. Cross-checking against several instances

| $a$ | $b$ | $g = \gcd(a,b)$ | Prime factorisation of $g$ | Divisors of $g$ | Answer |
|---|---|---|---|---|---|
| 12 | 6 | 6 | $2 \cdot 3$ | $1, 2, 3, 6$ | 4 |
| 25 | 30 | 5 | $5$ | $1, 5$ | 2 |
| 48 | 180 | 12 | $2^2 \cdot 3$ | $1, 2, 3, 4, 6, 12$ | 6 |
| 8 | 32 | 8 | $2^3$ | $1, 2, 4, 8$ | 4 |
| 17 | 19 | 1 | — | $1$ | 1 |
| 36 | 36 | 36 | $2^2 \cdot 3^2$ | nine values | 9 |
| 1000 | 1000 | 1000 | $2^3 \cdot 5^3$ | sixteen values | 16 |

The last two rows show why the answer is not simply "the number of factors of the
smaller input": when the inputs are equal, every factor of that value is shared,
and when they are coprime, only 1 is shared. The row $(8, 32)$ shows the case where
one input divides the other, so the gcd is the smaller input.

The $(36, 36)$ row also demonstrates that a divisor count can be odd. Divisors
usually come in pairs $x$ and $g/x$, and the pair collapses to a single value
exactly when $x = \sqrt{g}$. Since $36 = 6^2$, the value 6 is counted once, which
is why 36 has nine divisors rather than ten.

## 6. Why the reasoning is correct

**Invariant of the enumeration.** Let $D$ be the set of candidates that have been
accepted so far. After every tested candidate, $D$ is exactly the set of divisors
of $g$ among the values tested so far. This holds vacuously before the scan, and
the acceptance rule $g \bmod x = 0$ adds $x$ precisely when $x$ divides $g$. When
the scan finishes, $D$ is the complete divisor set of $g$.

**Exhaustiveness.** Every common factor is at most $g$, since the gcd is the
largest common factor. The scan enumerates every integer in $[1, g]$, so no
possible common factor is skipped. No candidate outside that range could ever
have been accepted, so the range is not merely convenient, it is exactly the
search space.

**Soundness.** Every accepted candidate divides $g$, and $g$ divides both $a$ and
$b$; divisibility is transitive, so every accepted candidate divides both inputs.
The count therefore never includes a value that fails the definition.

**Equality of the two counts.** By the reduction of section 2, the common factor
set of $(a,b)$ equals the divisor set of $g$. The scan returns the cardinality of
the latter, which is therefore the cardinality of the former — the required
answer. The correctness does not depend on the sign of anything, because the
constraints guarantee $a, b \ge 1$.

## 7. Boundary conditions this instance family exposes

| Situation | Instance | Answer | Reason |
|---|---|---|---|
| Minimum inputs | $(1, 1)$ | 1 | $\gcd = 1$, and 1 divides itself. |
| Coprime inputs | $(17, 19)$ | 1 | The only shared factor of distinct primes is 1. |
| One input divides the other | $(8, 32)$ | 4 | The gcd is 8, so the answer is the divisor count of 8. |
| Equal inputs | $(1000, 1000)$ | 16 | The gcd is 1000 and every factor is shared. |
| Perfect-square gcd | $(36, 36)$ | 9 | The square-root divisor pairs with itself and is counted once by a plain scan. |
| Prime gcd | $(25, 30)$ | 2 | $\gcd = 5$, so only 1 and 5 qualify. |
| Maximum inputs | $(1000, 1000)$ | 16 | The largest possible gcd, and therefore the longest scan, is 1000 candidates. |
| Endpoint inclusion | any instance | — | Both 1 and $g$ are divisors; a scan that omits either endpoint undercounts. |

## 8. Alternative methods and their trade-offs

| Method | Time | Auxiliary space | Why it is not used here |
|---|---|---|---|
| Test both inputs directly for every $x$ up to $\min(a,b)$ | $O(\min(a,b))$ | $O(1)$ | Correct but repeats two modulo tests per candidate and may scan past the gcd, whose divisors are the only ones that can qualify. |
| Enumerate divisor pairs up to $\sqrt{g}$ | $O(\sqrt{g})$ | $O(1)$ | Asymptotically the better scan: whenever $x$ divides $g$, both $x$ and $g/x$ are divisors, except when $x^2 = g$ and the two coincide. It needs an explicit square case, which the linear scan avoids. |
| Prime factorisation with the divisor-count product | $O(\sqrt{g})$ | $O(1)$ | If $g = p_1^{e_1} \cdots p_t^{e_t}$, the count is $\prod_r (e_r + 1)$. Elegant and general, but it needs trial division and exponent bookkeeping for a bound of only $g \le 1000$. |
| Reduce to the gcd, then scan $1 \dots g$ | $O(\log \min(a,b) + g)$ | $O(1)$ | Chosen. It removes the redundant second divisibility test, bounds the search space by the gcd, and needs no special case for square roots. |

## 9. Cost of the method: complexity derivation

Let $g = \gcd(a, b)$.

*Time.* Euclid's algorithm runs in $O(\log \min(a,b))$ divisions: the remainder
sequence decreases at least geometrically, so the number of steps is logarithmic
in the smaller input. The enumeration then performs one modulo operation for each
integer from 1 through $g$, which is $g$ constant-cost tests. Adding the two
phases,

$$
T(a, b) = O\bigl(\log \min(a,b)\bigr) + O(g) = O(g),
$$

because $g$ dominates the logarithm for every input in range. Under the stated
constraint $a, b \le 1000$ we have $g \le 1000$, so the scan performs at most a
thousand modulo operations — far below any practical limit. The bound is linear in
the gcd rather than in the inputs, which is exactly the improvement the reduction
buys: the pair $(8, 32)$ scans eight candidates instead of thirty-two.

*Auxiliary space.* The computation keeps the current candidate, the accumulated
count, and the pair of values that Euclid's algorithm is reducing — a constant
number of integers. No table indexed by $g$ or by a divisor is built, and the
input pair is never copied. Auxiliary memory is therefore

$$
S(a, b) = O(1).
$$

If the same gcd were needed for many queries, caching it would trade space for
time, but a single query needs no storage at all.