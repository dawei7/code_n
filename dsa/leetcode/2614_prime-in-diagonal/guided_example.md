# Guided Example: Prime In Diagonal

## 1. The instance, and the two conditions it separates

Take the square matrix

| row `i` | `nums[i][0]` | `nums[i][1]` | `nums[i][2]` |
|---|---|---|---|
| 0 | 4 | 97 | 8 |
| 1 | 89 | 9 | 83 |
| 2 | 6 | 79 | 13 |

Nine entries are stored, and the largest prime written anywhere in this matrix is $97$. The required answer is nevertheless $13$. The four large primes $97$, $89$, $83$ and $79$ sit off both diagonals, so they are invisible to the question, while $13$ sits on a diagonal and is prime. This instance therefore pulls apart two conditions that are easy to conflate: *being prime* and *lying on a diagonal*. A value can enter the answer only when both hold at once, and the answer is the largest such value, or $0$ if no diagonal entry is prime.

The matrix is square, $n = 3$, and every entry satisfies $1 \le \text{nums}[i][j] \le 4 \times 10^{6}$ with $1 \le n \le 300$. The $1$ lower bound matters later: no legal entry is $0$, so $0$ is available as an unambiguous "nothing found" marker.

## 2. Which cells count as diagonal cells

The statement defines a value as diagonal when it appears at `nums[i][i]` for some `i`, or at `nums[i][n - 1 - i]` for some `i`. Those two index rules are exactly the primary diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left), so the eligible set is the *union* of two families of $n$ coordinates each:

$$
\mathcal{D} = \{\, (i,\, i) : 0 \le i < n \,\} \;\cup\; \{\, (i,\, n - 1 - i) : 0 \le i < n \,\}.
$$

For $n = 3$ the two families contain one shared coordinate, $(1, 1)$, because the matrix size is odd:

| `i` | primary coordinate `(i, i)` | its value | anti-diagonal coordinate `(i, n-1-i)` | its value |
|---|---|---|---|---|
| 0 | `(0, 0)` | 4 | `(0, 2)` | 8 |
| 1 | `(1, 1)` | 9 | `(1, 1)` | 9 |
| 2 | `(2, 2)` | 13 | `(2, 0)` | 6 |

The union therefore holds only five distinct cells even though the two families together list six coordinates. Odd $n$ always yields the shared centre; even $n$ gives two disjoint diagonals. The deduplication is automatic once the running maximum is used, because $\max(a, a) = a$: encountering the centre twice cannot inflate or corrupt the result. Off-diagonal entries such as $97$ at `(0, 1)` are never enumerated at all, which is precisely why the answer is smaller than the largest prime in the matrix.

## 3. Deciding primality by trial division

An integer is prime when it exceeds $1$ and has no positive divisors other than $1$ and itself. To test a candidate $x$ it is enough to look for a divisor $d$ with $2 \le d \le \lfloor \sqrt{x} \rfloor$: if $x = a \cdot b$ with $a \le b$, then $a \le \sqrt{x}$, so every composite number has a factor inside that range. Because entries are capped at $4 \times 10^{6}$, no candidate needs more than $1999$ divisor probes.

| value | $\lfloor \sqrt{x} \rfloor$ | divisors probed | witness or conclusion | prime? |
|---|---|---|---|---|
| 4 | 2 | 2 | $4 = 2 \times 2$ | no |
| 8 | 2 | 2 | $8 = 2 \times 4$ | no |
| 6 | 2 | 2 | $6 = 2 \times 3$ | no |
| 9 | 3 | 2, 3 | $9 = 3 \times 3$ | no |
| 13 | 3 | 2, 3 | no divisor found | yes |
| 1 | — | none | $1$ is not greater than $1$ | no |

Two rows carry the load. The value $1$ must be rejected before any division, since it has no divisor strictly between $1$ and itself yet is still not prime. The value $9$ shows why the probe range must be *inclusive* of $\lfloor \sqrt{x} \rfloor$: stopping at $2$ would find no divisor and wrongly accept $9$.

## 4. The sweep, step by step

Walk $i$ from $0$ to $n - 1$. At each $i$, examine the primary coordinate `(i, i)` and then the anti-diagonal coordinate `(i, n-1-i)`, testing each value for primality and folding the primes into one accumulator that starts at $0$.

| step | coordinate | value | prime? | accumulator after the step |
|---|---|---|---|---|
| 1 | `(0, 0)` | 4 | no | 0 |
| 2 | `(0, 2)` | 8 | no | 0 |
| 3 | `(1, 1)` | 9 | no | 0 |
| 4 | `(1, 1)` | 9 (revisited centre) | no | 0 |
| 5 | `(2, 2)` | 13 | yes | 13 |
| 6 | `(2, 0)` | 6 | no | 13 |

Every probe before step 5 returns "not prime", so the accumulator stays at the sentinel $0$ for the first four steps; the centre is visited twice and both visits agree, which costs one redundant primality test but changes nothing. Step 5 supplies the only prime and lifts the accumulator to $13$; step 6 adds no prime and leaves it alone. The six steps have exhausted $\mathcal{D}$, so the accumulator is the answer: $13$.

## 5. Invariant: why the running maximum is exact

Let $\mathcal{D}_k$ be the first $k$ coordinates examined by the sweep, in the order shown above, and let $P_k$ be the set of values in $\mathcal{D}_k$ that are prime.

**Invariant.** After step $k$, the accumulator equals $\max P_k$ when $P_k \neq \emptyset$, and equals $0$ when $P_k = \emptyset$.

*Base.* At $k = 0$ no coordinate has been examined, $P_0 = \emptyset$, and the accumulator holds $0$ — the invariant holds by initialization.

*Step.* Suppose the invariant holds after step $k$, and step $k+1$ examines a coordinate whose value is $v$. If $v$ is composite or equals $1$, then $P_{k+1} = P_k$; the accumulator is left unchanged and still equals $\max P_{k+1}$ (or $0$ when that set is empty). If $v$ is prime, then $P_{k+1} = P_k \cup \{v\}$, and replacing the accumulator with $\max(\text{accumulator}, v)$ yields exactly $\max P_{k+1}$: the new value either dominates the whole previous set or is dominated by it.

Two consequences make this a genuine correctness argument rather than bookkeeping.

- **Soundness.** A value is written into the accumulator only after a divisor search has proved it prime, and only while visiting a coordinate of $\mathcal{D}$. So the final accumulator is either $0$ (no prime exists in $\mathcal{D}$) or a prime that really lies on a diagonal; it is never an off-diagonal value such as $97$ and never a composite such as $9$.
- **Completeness.** The two index rules generate all of $\mathcal{D}$, and the sweep runs over every $i$ in $[0, n)$. Hence no diagonal coordinate is skipped, and no prime on a diagonal can be missed.

Combining both directions, the final accumulator is exactly the largest prime on at least one diagonal, and it is $0$ precisely when no such prime exists — the two behaviours the statement requires.

## 6. Traps this instance exposes

| trap | what it looks like here | correct handling |
|---|---|---|
| Confusing "largest prime in the matrix" with "largest prime on a diagonal" | $97$ is prime and is the biggest entry, but it is off both diagonals; the answer is $13$ | Restrict candidates to $\mathcal{D}$ *before* comparing magnitudes |
| Treating $1$ as prime | A diagonal of all $1$s must yield $0$, and entries of $1$ appear in the official samples | Reject any value $\le 1$ before probing divisors |
| Stopping the divisor search below $\lfloor \sqrt{x} \rfloor$ | $9$ is composite with its smallest factor equal to $\lfloor \sqrt{9} \rfloor = 3$ | Probe divisors up to and including $\lfloor \sqrt{x} \rfloor$ |
| Assuming the centre is only tested once | With odd $n$ the same cell arrives from both index rules; skipping the second visit by symmetry would need extra branching | Let the running maximum absorb the duplicate |
| Using a "not found" marker that is a legal entry | A sentinel of $1$ or $2$ would collide with real diagonal values | Use $0$, which the constraint $1 \le \text{nums}[i][j]$ excludes from the input |
| Degenerate $n = 1$ | A single cell is both diagonals simultaneously, so it is examined twice | The same duplicate-absorption applies; a lone prime returns itself |
| Even $n$ | The diagonals share no coordinate, so exactly $2n$ cells are examined | The sweep is unchanged; only the duplicate disappears |

## 7. Complexity

**Time.** The sweep visits $2n$ coordinates, and each visited value costs one trial-division test whose probe count is at most $\lfloor \sqrt{V} \rfloor - 1$, where $V$ is the largest permitted entry. With $V = 4 \times 10^{6}$ that is at most $1999$ probes. The total is therefore

$$
O\!\left(n \sqrt{V}\right) \;=\; O\!\left(2n \cdot \lfloor \sqrt{V} \rfloor\right),
$$

which for the stated limits is at most $600 \times 1999 \approx 1.2 \times 10^{6}$ integer remainder operations. The duplicate centre in odd matrices only doubles one already-counted term, so it does not change the bound.

**Auxiliary space.** The method stores one accumulator and two loop counters, independent of $n$ and of the entry magnitudes: $O(1)$ extra space. The matrix itself is read in place and never copied. A sieve of Eratosthenes over the whole value range would trade this for $O(V)$ memory and precomputation that is wasted whenever the sweep only touches $2n$ values, which is why per-value trial division is the better fit for these limits.
