# Guided Example: Closest Prime Numbers in Range

## 1. The Instance and the Two Decisions It Exposes

We are given two positive integers $left \le right$ and must return the pair of primes $num_1 < num_2$ inside that interval whose difference is minimal, breaking ties by the smaller $num_1$, or `[-1, -1]` when the interval does not contain two primes.

We work the first official instance:

- `left` = `10`
- `right` = `19`

The required output is `[11, 13]`. This instance is ideal because it forces both decisions at once:

- **the tie-break**, since the interval contains the primes $11, 13, 17, 19$ and the minimum gap $2$ is achieved **twice** — by $(11, 13)$ and by $(17, 19)$ — so the rule "smallest `num1` among minimal gaps" decides the answer, and a scan that overwrote the incumbent on an equal gap would return `[17, 19]`;
- **the adjacency fact**, since the pair $(13, 17)$ has gap $4$ and is never competitive, while $(11, 19)$ has gap $8$; the winning pair is adjacent in the sorted prime list, and section 7 proves that this must always be the case.

The instance also sits just above the small-prime edge cases ($2$ and $3$ are outside the interval) and well below the numeric ceiling, so it isolates the algorithmic ideas without arithmetic noise.

## 2. Why the Interval Is Sieved from the Bottom

A single interval can be tested for primality number by number, but the whole range must be examined anyway: the minimum gap is a global property of the prime list inside $[left, right]$, so every candidate number in the interval participates in the decision. The practical strategy is therefore to build the primality table **once for the entire prefix** $[2, right]$ and then read the interval out of it.

The bound is what makes this affordable. With $right \le 10^{6}$, a boolean table of size $right + 1$ is small, and the sieve needs to mark composites only using primes up to $\sqrt{right} \le 1000$, because every composite $x \le right$ has a prime factor not exceeding $\sqrt{x} \le \sqrt{right}$. Formally, if $x = a \cdot b$ with $1 < a \le b < x$ then $a \le \sqrt{x}$; so a composite is always reached by a marking pass launched from one of its prime factors at most $\sqrt{right}$.

Two conventions matter before any marking begins. The numbers $0$ and $1$ are not prime, so the sieve iterates from $2$. And the table must cover $right$ itself, not $right - 1$, because the endpoint is inclusive: for the maximum input $10^{6}$ the final slot is part of the answer space.

## 3. Marking Composites: The Sieve of Eratosthenes

The classical sieve walks the candidates in increasing order; when a candidate has not been marked by any earlier pass, it is prime, and all of its multiples are marked composite. For $right = 19$ the marking primes are those with $p^2 \le 19$, namely $2$ and $3$:

| Marking prime $p$ | Multiples $2p, 3p, \dots$ inside $[2, 19]$ | Values marked composite | Already marked earlier? |
|:---:|:---|:---|:---|
| 2 | 4, 6, 8, 10, 12, 14, 16, 18 | 4, 6, 8, 10, 12, 14, 16, 18 | no, this is the first pass |
| 3 | 9, 15 (starting at $3^2 = 9$) | 9, 15 | no |

Starting each pass at $p^2$ is safe because every smaller multiple $k p$ with $k < p$ has a prime factor $k$'s own prime divisor below $p$ and was therefore marked by an earlier pass. After both passes the unmarked values in $[2, 19]$ are

$$2, 3, 5, 7, 11, 13, 17, 19,$$

which are exactly the primes up to $19$. The composites $4, 6, 8, 9, 10, 12, 14, 15, 16, 18$ are all accounted for, and every mark is justified by an explicit factorization: $9 = 3^2$, $15 = 3 \cdot 5$, $16 = 2^4$, and so on.

## 4. The Linear Sieve: Each Composite Marked Exactly Once

A tighter variant, and the one this package's reference follows, marks every composite exactly once, by its **smallest** prime factor. It walks $i$ from $2$ upward, records $i$ as prime when the table still says composite-free, and then marks $i \cdot p$ for the discovered primes $p$ in increasing order — stopping as soon as $p$ divides $i$. The stopping rule is what prevents duplicate marks: once $i \bmod p = 0$, every larger prime $q$ would mark a value whose smallest prime factor is $p$, not $q$, and that value will be marked again later from the index $i \cdot q / p$.

Tracing the sieve for $right = 19$, where the marking condition is $i \cdot p \le 19$:

| $i$ | Table says composite already? | New prime recorded | Products $i \cdot p$ marked ($p$ increasing) | Why the inner loop stopped |
|:---:|:---:|:---:|:---|:---|
| 2 | no | 2 | `4` (from $p = 2$) | $i \bmod 2 = 0$ |
| 3 | no | 3 | `6` ($p = 2$), `9` ($p = 3$) | $i \bmod 3 = 0$ |
| 4 | yes | — | `8` ($p = 2$) | $i \bmod 2 = 0$ |
| 5 | no | 5 | `10` ($p = 2$), `15` ($p = 3$) | next prime would exceed $19 / i$, so no further product fits |
| 6 | yes | — | `12` ($p = 2$) | $i \bmod 2 = 0$ |
| 7 | no | 7 | `14` ($p = 2$) | next prime would exceed $19 / i$ |
| 8 | yes | — | `16` ($p = 2$) | $i \bmod 2 = 0$ |
| 9 | yes | — | `18` ($p = 2$) | next prime would exceed $19 / i$ |
| 10 to 19 | mixed | 11, 13, 17, 19 | none | $2i > 19$ for every $i \ge 10$, so no product fits |

The primes recorded are $2, 3, 5, 7, 11, 13, 17, 19$ — the same eight values the classical sieve produced — and the marked composites are again exactly $4, 6, 8, 9, 10, 12, 14, 15, 16, 18$, this time each one marked once. Notice how the two stopping reasons differ in kind: a divisibility stop ($i \bmod p = 0$) is a correctness rule about smallest prime factors, while an out-of-range stop ($i \cdot p > right$) is a boundary rule about the table. Confusing the two is a common source of either duplicate work or an out-of-bounds write.

Rows $10$ through $19$ are grouped because the whole inner loop is skipped there: $2 \cdot 10 = 20 > 19$. The sieve's work is concentrated at small $i$, which is why its total cost is nearly linear.

## 5. Reading the Interval Out of the Table

With the full prime list in hand, the interval filter keeps only the primes inside $[left, right]$ — endpoints inclusive, which matters for the case $left = right = 17$:

| Prime $p$ | $p < 10$? | $10 \le p \le 19$? | Kept for the gap scan? |
|:---:|:---:|:---:|:---|
| 2 | yes | no | no |
| 3 | yes | no | no |
| 5 | yes | no | no |
| 7 | yes | no | no |
| 11 | no | yes | yes |
| 13 | no | yes | yes |
| 17 | no | yes | yes |
| 19 | no | yes | yes |

The kept list is $(11, 13, 17, 19)$ in increasing order, which is exactly the order in which the sieve discovered them. That ordering is not incidental: the primality table produces the primes in ascending order for free, so no sort is ever required, and the scan that follows can rely on the list being sorted.

## 6. The Consecutive-Gap Scan and the Tie-Break

The scan walks the kept list once and compares each prime only with its immediate successor, maintaining the best gap and the corresponding pair. The update is strict, which is what implements the "smallest `num1`" tie-break: an equal gap never replaces the incumbent, and because the list is scanned left to right, the first pair achieving the minimum is the one with the smallest $num_1$.

| Step | Current prime | Next prime | Gap $num_2 - num_1$ | Gap beats incumbent? | Best gap | Best pair |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| start | — | — | — | — | $\infty$ | $[-1, -1]$ |
| 1 | 11 | 13 | 2 | yes, $2 < \infty$ | 2 | $[11, 13]$ |
| 2 | 13 | 17 | 4 | no, $4 \ge 2$ | 2 | $[11, 13]$ |
| 3 | 17 | 19 | 2 | no, $2 \ge 2$ (strict comparison keeps the earlier pair) | 2 | $[11, 13]$ |

The final answer is $[11, 13]$, matching the required output. Step 3 is the decisive one: a relaxed comparison `gap <= best` would replace the pair with $[17, 19]$ and return the wrong tie winner. The pair $(13, 17)$ at step 2 is never a candidate despite gap $4$, and the non-adjacent pair $(11, 19)$ with gap $8$ is never even examined — the next section explains why that omission is not a loss.

## 7. Correctness: The Adjacent-Pair Invariant

**Claim.** If two primes $a < b$ in the interval minimize the difference, then $a$ and $b$ are adjacent in the sorted list of interval primes.

*Proof.* Suppose some prime $c$ of the interval satisfies $a < c < b$. Then $c - a > 0$ and $b - c > 0$, and their sum is $b - a$, so each is strictly smaller than $b - a$. Either of the pairs $(a, c)$ or $(c, b)$ is therefore a pair of interval primes with a strictly smaller gap, contradicting the minimality of $b - a$. Hence no such $c$ exists and $a, b$ are adjacent in the sorted list. $\square$

**Invariant of the scan.** After processing the first $k$ adjacent pairs of the kept list, the stored best gap equals the minimum gap over those pairs, and the stored pair is the lexicographically smallest pair achieving it.

*Initialization.* Before any pair is examined the best gap is $\infty$ and the pair is the `[-1, -1]` sentinel, which no finite gap can beat. The sentinel also covers the case of an interval with fewer than two primes, because then the scan body never runs and the untouched sentinel is returned.

*Preservation.* The scan visits adjacent pairs in increasing order of $num_1$. If the new gap is strictly smaller than the stored one, the new pair is the unique best so far; if it is equal or larger, the stored pair was already optimal and has a smaller $num_1$, so keeping it is exactly the tie-break rule. Either way the invariant holds after the update.

*Completeness.* After the last pair the invariant covers every adjacent pair. By the adjacency claim, the minimum over adjacent pairs equals the minimum over **all** pairs of distinct interval primes, so the stored gap is globally minimal and the stored pair satisfies both tie-break requirements. When fewer than two primes lie in the interval, no pair exists and the sentinel `[-1, -1]` is returned, which is the required output.

The sieve's own correctness completes the argument: a value is marked composite exactly when some prime $p \le \sqrt{right}$ (classical variant) or some recorded prime $p$ with $i \bmod p = 0$ handled it (linear variant) divides it, and an unmarked value greater than $1$ has no divisor other than $1$ and itself, hence is prime.

## 8. Traps and Boundary Behaviour

| Scenario | Instance | What happens | Result | Why the rule still holds |
|:---|:---|:---|:---|:---|
| interval contains `1` | `left = 1, right = 3` | $1$ is never prime; the primes are $2, 3$ | `[2, 3]` | The sieve starts at $2$, so the non-prime unit is excluded structurally rather than by a special case. |
| only one prime | `left = 4, right = 6` | primes in range: $5$ only | `[-1, -1]` | Fewer than two primes means no adjacent pair, and the sentinel survives the scan. |
| no primes at all | `left = 14, right = 16` | $14, 15, 16$ are all composite | `[-1, -1]` | The kept list is empty, which is a special case of "fewer than two". |
| a singleton interval | `left = right = 17` | the endpoint is inclusive, so $17$ is kept | `[-1, -1]` | One prime cannot form a pair; inclusivity is what puts $17$ in the list rather than nothing. |
| several tied gaps | `left = 5, right = 19` | gaps $2, 4, 2, 4, 2$ | `[5, 7]` | Strict comparison keeps the earliest pair, so the smallest $num_1$ wins all three ties. |
| the only gap of size one | `left = 1, right = 3` | $(2, 3)$ has gap $1$ | `[2, 3]` | For primes above $2$ all values are odd, so every other gap is even and $1$ is unattainable; the pair $(2,3)$ is the unique exception. |
| larger interval, same rule | `left = 100, right = 140` | primes $101, 103, \dots, 139$; gaps $2, 4, 2, 4, 14, 4, 6, 2$ | `[101, 103]` | The minimum gap $2$ occurs first at $101$; later tied pairs do not displace the incumbent. |
| the extreme upper end | `left = 999900, right = 1000000` | the sieve must cover $10^{6}$ inclusive | `[999959, 999961]` | Allocating a table of size $right + 1$ keeps the endpoint in the valid index range. |
| non-adjacent pairs | `left = 10, right = 19` | $(11, 19)$ has gap $8$ and is skipped | — | By the adjacency claim a non-adjacent pair can never be strictly better than some adjacent pair inside it. |

Two traps deserve to be named. First, **the tie-break direction**: the problem asks for the smallest $num_1$, so replacing the incumbent on equal gaps is wrong — the instance above flips from `[11, 13]` to `[17, 19]`. Second, **the meaning of "range"**: the endpoints are inclusive, and the sieve for the classical variant only needs to mark with primes up to $\sqrt{right}$, so a loop that marks all the way to $right$ wastes a large factor of work without changing a single verdict.

## 9. Complexity: Time and Auxiliary Space

**Sieve time.** The classical sieve marks the multiples of each prime $p \le \sqrt{right}$, costing about $right/p$ operations for that prime, so the total is the familiar

$$\sum_{p \le \sqrt{right}} \frac{right}{p} = \mathrm{O}(right \cdot \log \log right).$$

The linear variant used by this package's reference marks each composite exactly once, because every composite $m = i \cdot p$ with $p$ its smallest prime factor is generated by exactly one pair $(i, p)$ — the pairs cut off by the divisibility stop are precisely the duplicates. Its cost is therefore

$$T_{\text{sieve}}(right) = \mathrm{O}(right),$$

which is optimal up to a constant: the table has $right + 1$ slots and each composite must be handled at least once.

**Scan time.** Collecting the in-range primes costs one pass over the recorded prime list, and the gap scan visits at most $\pi(right) - 1$ adjacent pairs, where $\pi$ counts primes. Since $\pi(right) \le right$, both are dominated by the sieve, and the total is

$$T(left, right) = \mathrm{O}(right).$$

No sorting is performed — the sieve emits primes in increasing order — so the $\mathrm{O}(\pi \log \pi)$ cost of sorting never appears. When the interval is short but sits near the ceiling, the sieve still pays $\mathrm{O}(right)$, which is the correct trade: it is the price of the single-pass table that answers every primality question in the range at once.

**Auxiliary space.** The primality table has $right + 1$ entries, the recorded prime list holds at most $\pi(right)$ values, and the kept in-range list holds at most as many, so

$$S_{\text{aux}}(left, right) = \mathrm{O}(right).$$

The dominant term is the table. The scan itself is $\mathrm{O}(1)$ beyond the lists, needing only the incumbent gap, the incumbent pair, and a cursor. A segmented sieve restricted to $[left, right]$ would cut the memory to $\mathrm{O}(right - left)$ while keeping roughly the same marking work, at the price of a more intricate index mapping — a reasonable trade only when the interval is much narrower than the ceiling, which the constraints do not guarantee.

## 10. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Sieve the prefix, then scan adjacent pairs | Build a primality table for $[2, right]$, filter the interval, compare consecutive primes. | $\mathrm{O}(right)$ time and space | The preferred method: one table, one filter, one linear scan, and no sorting. |
| Trial-divide every value in the interval | Test each $x \in [left, right]$ for divisors up to $\sqrt{x}$. | $\mathrm{O}\big((right - left)\sqrt{right}\big)$ time, $\mathrm{O}(1)$ space | Competitive only for very short intervals; it re-derives information the sieve shares across the range, and at $10^{6}$ values it does roughly $10^{9}$ operations. |
| Segmented sieve over the interval | Mark composites in $[left, right]$ using primes up to $\sqrt{right}$ only. | $\mathrm{O}\big((right - left)\log\log right\big)$ time, $\mathrm{O}(right - left)$ space | Uses less memory when the interval is narrow, but needs careful offset arithmetic so that marks land on multiples of each prime relative to the window start. |
| Compare all pairs of in-range primes | Take the minimum gap over every pair, not just neighbours. | $\mathrm{O}(\pi^2)$ time | Unnecessary: the adjacency claim shows the closest pair is always adjacent, so the extra comparisons can never find a smaller gap. |
| Test the fixed candidates 2 and 3 first as a shortcut | Assume the answer is a twin pair when one exists. | — | True only when a gap of $2$ occurs in the interval; intervals such as $[4, 6]$ or $[23, 29]$ have no twin pair, and the general scan handles every case uniformly. |
| Replace the incumbent on equal gaps | Use a non-strict comparison when a smaller gap is found. | $\mathrm{O}(right)$ time | Returns the *largest* tied $num_1$, contradicting the tie-break rule; the sample would become `[17, 19]`. |

The transferable ideas are two: a numeric range question is usually cheapest to answer by sieving a single shared prefix table, and a minimum-gap question over a sorted set needs only adjacent comparisons, because any wider pair strictly contains a narrower one.
