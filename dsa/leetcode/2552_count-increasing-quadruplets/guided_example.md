# Guided Example: Count Increasing Quadruplets

## 1. The instance, and the crossed pattern it asks for

Take the first official sample: `nums = [1,3,2,4,5]`, whose required output is `2`. The array is a permutation of $1$ to $n$, and a quadruplet is a choice of four indices $i < j < k < l$ whose values satisfy

$$
\text{nums}[i] < \text{nums}[k] < \text{nums}[j] < \text{nums}[l],
$$

so the two middle positions are *crossed*: the value at $j$ is larger than the value at $k$, while the outer pair straddles them. Ranking the four values from smallest to largest, the positions $i, j, k, l$ receive ranks $1, 3, 2, 4$. This is the classical $1324$ pattern in a permutation, and it is the reason the problem is hard: the condition is not "four increasing values", and it is not an inversion either. It is a mixed pattern whose two inner positions must be a descent while both outer positions must sit outside that descent's value range.

The reading "four increasing values" is the first trap. For `nums = [1,2,3,4]`, the only available index tuple is $(0,1,2,3)$, and $\text{nums}[j] = 2 < \text{nums}[k] = 3$ fails, so the required output is `0` rather than `1`. Every candidate must be tested against the crossed order.

## 2. Anchoring on the middle pair

The four inequalities become manageable once the *middle pair* $(j,k)$ is treated as the anchor. Fixing indices $j$ and $k$ with $j < k$ splits the requirement into three independent parts:

- the pair itself must be a descent, $\text{nums}[j] > \text{nums}[k]$;
- the first index $i$ must lie strictly left of $j$ and carry a value strictly below $\text{nums}[k]$;
- the last index $l$ must lie strictly right of $k$ and carry a value strictly above $\text{nums}[j]$.

Nothing couples $i$ to $l$: once $(j,k)$ is fixed, every admissible $i$ can be combined with every admissible $l$, because the index order $i < j < k < l$ is automatic from the two ranges and the value chain $\text{nums}[i] < \text{nums}[k] < \text{nums}[j] < \text{nums}[l]$ follows from the two separate comparisons. The count therefore factors into a product. Writing

$$
L(j,k) = \#\{\, i : i < j \text{ and } \text{nums}[i] < \text{nums}[k] \,\},
\qquad
R(j,k) = \#\{\, l : l > k \text{ and } \text{nums}[l] > \text{nums}[j] \,\},
$$

the answer is the sum of $L(j,k) \cdot R(j,k)$ over all descents $(j,k)$ with $1 \le j$ and $k \le n-2$. The index bounds matter: $j$ needs at least one position to its left and $k$ needs at least one to its right, so the pairs live in a strict interior band and there are $\binom{n-2}{2}$ of them, about $8.0 \times 10^6$ at the maximum $n = 4000$.

Note carefully which value each count compares against. $L$ is filtered by $\text{nums}[k]$, not by $\text{nums}[j]$, and $R$ is filtered by $\text{nums}[j]$, not by $\text{nums}[k]$. Using the wrong reference silently over-counts, and Section 7 shows the instance where the two filters disagree.

## 3. The traced instance `[1,3,2,4,5]`

Scan the possible middle pairs and test the descent condition first, since a pair that is not a descent contributes nothing.

| $(j,k)$ | $\text{nums}[j], \text{nums}[k]$ | Descent? | $L(j,k)$: indices $i < j$ with $\text{nums}[i] < \text{nums}[k]$ | $R(j,k)$: indices $l > k$ with $\text{nums}[l] > \text{nums}[j]$ | Product |
|---|---|---|---|---|---|
| (1,2) | 3, 2 | yes, $3 > 2$ | $i = 0$ works since $1 < 2$: count 1 | $l = 3$ ($4 > 3$) and $l = 4$ ($5 > 3$): count 2 | 2 |
| (1,3) | 3, 4 | no | not a middle pair | not a middle pair | 0 |
| (1,4) | 3, 5 | no | not a middle pair | not a middle pair | 0 |
| (2,3) | 2, 4 | no | not a middle pair | not a middle pair | 0 |
| (2,4) | 2, 5 | no | not a middle pair | not a middle pair | 0 |
| (3,4) | 4, 5 | no | not a middle pair | not a middle pair | 0 |

Only $(j,k) = (1,2)$ survives, and its product is $1 \times 2 = 2$, matching the required output. The two quadruplets it generates are $(0,1,2,3)$ and $(0,1,2,4)$: both use $i = 0$, because only the value $1$ is below $\text{nums}[k] = 2$, and they differ in the fourth index, exactly as the official explanation reports. Notice that the pair $(2,3)$ with values $2, 4$ is *increasing*, so even though the prefix contains a smaller value and the suffix contains larger ones, no quadruplet can use it as its middle.

## 4. A richer instance: `[1,4,2,5,3,6]`

The traced sample exercises only one middle pair, so it cannot show how several pairs add up. Take the recorded trial `nums = [1,4,2,5,3,6]`, whose expected output is `5`, and enumerate every descent in the interior band.

| $(j,k)$ | Values | $L(j,k)$ | Which $i$ | $R(j,k)$ | Which $l$ | Contribution |
|---|---|---|---|---|---|---|
| (1,2) | 4, 2 | 1 | $i = 0$, since $1 < 2$ | 2 | $l = 3$ ($5 > 4$), $l = 5$ ($6 > 4$) | 2 |
| (1,3) | 4, 5 | — | not a descent | — | — | 0 |
| (1,4) | 4, 3 | 1 | $i = 0$, since $1 < 3$ | 1 | $l = 5$ ($6 > 4$) | 1 |
| (2,3) | 2, 5 | — | not a descent | — | — | 0 |
| (2,4) | 2, 3 | — | not a descent | — | — | 0 |
| (3,4) | 5, 3 | 2 | $i = 0$ ($1 < 3$), $i = 2$ ($2 < 3$) | 1 | $l = 5$ ($6 > 5$) | 2 |

The contributions are $2 + 1 + 2 = 5$, matching the expected output. Spelling out the five quadruplets makes the product structure visible, since each row of the table expands into exactly $L \times R$ index tuples.

| $(j,k)$ | Quadruplets $(i,j,k,l)$ | Value chain |
|---|---|---|
| (1,2) | $(0,1,2,3)$, $(0,1,2,5)$ | $1 < 2 < 4 < 5$ and $1 < 2 < 4 < 6$ |
| (1,4) | $(0,1,4,5)$ | $1 < 3 < 4 < 6$ |
| (3,4) | $(0,3,4,5)$, $(2,3,4,5)$ | $1 < 3 < 5 < 6$ and $2 < 3 < 5 < 6$ |

Two things to notice. First, the index $l = 4$ is unusable for the pair $(1,2)$ even though it lies to the right of $k = 2$, because $\text{nums}[4] = 3$ is not above $\text{nums}[j] = 4$; the fourth value is filtered by the *larger* member of the middle pair. Second, the index $i$ must also be compared against the *smaller* member: for the pair $(3,4)$, the prefix indices $0$ and $2$ qualify because both values sit below $\text{nums}[k] = 3$, while $i = 1$ with value $4$ does not. Both filters are one-sided and both are easy to invert by accident.

## 5. How the two counts are maintained without rescanning

Computing $L$ and $R$ from scratch for every pair would cost $\Theta(n^3)$ time, but each count changes by at most one when a pair coordinate moves, so a single sweep per coordinate suffices.

- **Maintaining $R$ for a fixed $j$.** Let $k$ run upward from $j+1$. Start with the count of all $l > j$ whose value exceeds $\text{nums}[j]$. That pool contains the positions greater than $k$, plus position $k$ itself when it is large. As $k$ advances, position $k$ leaves the range $l > k$, so if $\text{nums}[k] > \text{nums}[j]$ the pool must shrink by one; otherwise $k$ was never in the pool and the count is unchanged. Reading the pool at each descent gives $R(j,k)$ exactly.
- **Maintaining $L$ for a fixed $k$.** Let $j$ run downward from $k-1$. Start with the count of all $i < k$ whose value is below $\text{nums}[k]$, which contains the positions below $j$ plus position $j$ itself when it is small. As $j$ decreases, position $j$ leaves the range $i < j$, so if $\text{nums}[j] < \text{nums}[k]$ the count shrinks by one; otherwise it is unchanged. Reading it at each descent gives $L(j,k)$ exactly.

The sweep for $j = 1$ on the richer instance shows the bookkeeping. The pool starts as $\{3, 5\}$, the positions right of $j = 1$ with values above $\text{nums}[1] = 4$.

| $k$ | $\text{nums}[k]$ | Pool of usable $l$ before the test | $R(1,k)$ | Pool after moving past $k$ |
|---|---|---|---|---|
| 2 | 2 | $\{3,5\}$ | 2, and $(1,2)$ is a descent | unchanged, since $2 < 4$ was never in the pool |
| 3 | 5 | $\{3,5\}$ | not a descent, no pair | drop 3, since $5 > 4$ |
| 4 | 3 | $\{5\}$ | 1, and $(1,4)$ is a descent | unchanged, since $3 < 4$ was never in the pool |

Reading the non-empty entries gives $R(1,2) = 2$ and $R(1,4) = 1$, matching Section 4. The mirrored sweep for $k = 4$ produces the $L$ values in the same way: the pool of usable $i$ starts as $\{0, 2\}$, the positions left of $k = 4$ with values below $\text{nums}[4] = 3$; at $j = 3$ the pool is intact and $L(3,4) = 2$; moving past $j = 3$ drops nothing because $\text{nums}[3] = 5$ was never in the pool; at $j = 1$ the pool has already lost position $2$ when $j$ passed it, leaving $L(1,4) = 1$. Every descent therefore reads its own count in constant amortized time, and the whole table of pairs is filled in $\Theta(n^2)$ work.

## 6. Why every quadruplet is counted exactly once

The decomposition is a bijection, which is the correctness argument in full.

- **Every quadruplet has a unique anchor.** Given $i < j < k < l$ satisfying the value chain, the middle pair $(j,k)$ is determined, and it is a descent because $\text{nums}[k] < \text{nums}[j]$ is part of the chain. The index $i$ is counted by $L(j,k)$ since $i < j$ and $\text{nums}[i] < \text{nums}[k]$, and $l$ is counted by $R(j,k)$ since $l > k$ and $\text{nums}[l] > \text{nums}[j]$. So the quadruplet appears in exactly one product term.
- **Every product term describes real quadruplets.** Conversely, if $i < j$ with $\text{nums}[i] < \text{nums}[k]$, and $l > k$ with $\text{nums}[l] > \text{nums}[j]$, and $(j,k)$ is a descent, then $i < j < k < l$ and the four values chain as $\text{nums}[i] < \text{nums}[k] < \text{nums}[j] < \text{nums}[l]$. Chaining the two independent comparisons through the descent is exactly the required order.

Because the map from quadruplets to (anchor, $i$, $l$) triples is a bijection, summing the products neither misses nor double-counts anything. The only structural requirement is the boundary band on $j$ and $k$: pairs outside it cannot have both a left and a right partner, and including them would add zero terms anyway since one of the two counts would be empty.

## 7. Traps this instance exposes

| Situation | Naive expectation | Actual behaviour | Where it bites |
|---|---|---|---|
| The pattern | four increasing values | ranks $1, 3, 2, 4$: the middle pair must be a descent | `[1,2,3,4]` returns `0`, not `1` |
| Which value filters $i$ | compare $\text{nums}[i]$ with $\text{nums}[j]$ | compare with $\text{nums}[k]$, the smaller middle value | $i = 1$ with value $4$ must be excluded for $(j,k) = (3,4)$ |
| Which value filters $l$ | compare $\text{nums}[l]$ with $\text{nums}[k]$ | compare with $\text{nums}[j]$, the larger middle value | $l = 4$ with value $3$ is unusable for $(j,k) = (1,2)$ |
| Anchor bounds | every pair $j < k$ | $j \ge 1$ and $k \le n-2$ are required | pairs at the edges always contribute zero |
| Pairing the counts | $i$ and $l$ interact | the choices are independent, so the counts multiply | adding instead of multiplying is a different problem |
| A descent alone | a descent guarantees a quadruplet | it needs a lower value to its left and a higher one to its right | `[5,4,3,2,1]` has many descents and returns `0` |
| Position versus value | small values can be first indices whenever they appear | $i$ must also be positioned left of $j$ | `[4,1,6,2,5,3,7]` needs position-sensitive counting |
| Rescanning | each pair can be counted on demand | a naive rescan is $\Theta(n^3)$ | at $n = 4000$ that is far beyond any time limit |

The second and third rows are the same mistake in mirror image, and they are the dominant source of wrong answers: the quadruplet's value chain crosses in the middle, so each outer index is compared against the *opposite* member of the middle pair from the one intuition suggests.

## 8. Time and auxiliary space

With $m = n - 2$ usable middle positions, the number of anchor pairs is

$$
\binom{m}{2} = \frac{(n-2)(n-3)}{2} = \Theta(n^2),
$$

about $8.0 \times 10^6$ at $n = 4000$. Each pair is visited once and reads two counters that are updated in constant amortized time, so the running time is $\Theta(n^2)$ with a small constant: one sweep per starting row for the right-hand counts and one sweep per starting column for the left-hand counts, each of length at most $n$. Nothing in the algorithm depends on the values themselves, only on comparisons, so a permutation with heavy structure is no easier or harder than a random one.

The straightforward tabulation stores one count per anchor pair in each of the two sweeps, which is $\Theta(n^2)$ auxiliary space — two triangular tables of about eight million entries at the maximum input. That is the honest cost of joining the left-hand count $L$ and the right-hand count $R$ at the same anchor pair. When memory is the binding constraint, both counts can instead be obtained from a Fenwick tree over value ranks, giving $\Theta(n^2 \log n)$ time with only $O(n)$ auxiliary space; the extra logarithmic factor buys back the quadratic table. Either way, the product structure of Section 2 is what keeps the algorithm quadratic rather than cubic, and no dynamic program over four indices is needed.