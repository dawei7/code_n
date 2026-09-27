# Guided Example: Shortest Distance in a Line

The `Point` table stores one integer position per row on the x-axis, and `x` is the
primary key, so positions are unique. Every row is a point on the real line; the task is
to report a single attribute named `shortest` holding the smallest absolute difference
between two distinct stored positions. The relation is guaranteed to contain at least two
rows, so an answer always exists.

Working on a line rather than in the plane removes an entire dimension of difficulty but
introduces one sharp trap: once the points are comparable, the difference between two
positions is *signed*, and aggregating a signed difference with a minimum produces the most
negative value instead of the smallest distance. The lesson develops the orientation
discipline that removes the sign, proves that one orientation still covers every unordered
pair, and then sharpens the same reasoning into the adjacency invariant that answers the
statement's follow-up question.

## 1. The Instance and the Contract

Schema of `Point`:

| Column name | Type | Role |
|---|---|---|
| `x` | int | the position on the x-axis; the primary key, hence unique |

Input relation:

| `x` |
|---|
| -1 |
| 0 |
| 2 |

Required output relation:

| `shortest` |
|---|
| 1 |

The distance between two positions is the absolute difference

$$
d(x_i, x_j) = \lvert x_i - x_j \rvert,
$$

and the returned value is $\min_{i \ne j} d(x_i, x_j)$. Row order in the input is
irrelevant; the positions are a set, not a sequence.

## 2. Removing the Sign with an Orientation

The absolute value is exactly what a minimum aggregate handles badly, but it can be
eliminated algebraically. For any two positions,

$$
\lvert x_i - x_j \rvert = \max(x_i, x_j) - \min(x_i, x_j).
$$

So if a pairing rule guarantees that one side of the subtraction always holds the larger
position, the computed difference is already non-negative and no absolute value is needed.

| Pairing rule | Self-pairs admitted | Sign of the computed difference | Pairs examined per unordered pair |
|---|---|---|---|
| No rule (full Cartesian product) | yes, all $N$ of them | can be negative | 2 |
| Positions merely unequal | no | can be negative | 2 |
| One side not larger than the other | yes, difference is $0$ | never negative | 1 plus $N$ self-pairs |
| Strictly smaller on the left | no | always strictly positive | 1 |

The first row is the empty-filter failure: the minimum over all pairs including the $N$
self-pairs is $0$ for every input. The second row removes the self-pairs but keeps both
orientations of every remaining pair, and both orientations are signed, so the aggregate
sees the value $-|x_i - x_j|$ for whichever orientation subtracts the larger position
first. The minimum of a symmetric set of signed differences is the *most negative* value,
not the smallest distance — on this instance the candidates would be
$\{1, -1, 2, -2, 3, -3\}$ and the aggregate would return $-3$ instead of $1$. The fourth
row is the disciplined choice: strict inequality on one side simultaneously excludes
self-pairs, forces positivity, and picks one orientation per pair.

## 3. Why One Orientation Still Covers Every Pair

The real numbers are totally ordered, so for any two distinct positions exactly one of
$x_i < x_j$ and $x_j < x_i$ holds. That trichotomy is what makes the strict orientation
complete rather than merely convenient:

* it cannot both keep and drop a pair, because the two orientations are mutually
  exclusive;
* it cannot drop a pair entirely, because every unequal pair has exactly one orientation
  satisfying the strict comparison;
* it cannot double-count a pair, because only one orientation satisfies it.

Enumerating the six ordered pairs of the instance makes the reduction visible:

| Ordered pair $(p_1, p_2)$ | Strictly smaller on the left? | Difference computed | Kept as an unordered pair |
|---|---|---|---|
| $(-1, 0)$ | yes | $0 - (-1) = 1$ | yes |
| $(0, -1)$ | no | $-1 - 0 = -1$ | no, mirror image |
| $(-1, 2)$ | yes | $2 - (-1) = 3$ | yes |
| $(2, -1)$ | no | $-1 - 2 = -3$ | no, mirror image |
| $(0, 2)$ | yes | $2 - 0 = 2$ | yes |
| $(2, 0)$ | no | $0 - 2 = -2$ | no, mirror image |

Three ordered pairs survive, and they are exactly the three unordered pairs. Notice what
the discarded rows would have contributed: $-1$, $-3$, and $-2$. An aggregate over all six
rows would therefore report $-3$, which is neither a distance nor even a non-negative
number.

## 4. Working the Instance to the Answer

The three surviving candidates, evaluated in the order produced by the input:

| Step | Kept pair | Difference | Running minimum | Comment |
|---|---|---|---|---|
| 1 | $-1$ and $0$ | $0 - (-1) = 1$ | $1$ | The running minimum initializes here |
| 2 | $-1$ and $2$ | $2 - (-1) = 3$ | $1$ | Larger than the running minimum, ignored |
| 3 | $0$ and $2$ | $2 - 0 = 2$ | $1$ | Larger again; the aggregate is final |

$$
\min\{1, 3, 2\} = 1 .
$$

The distances written out in full are

$$
d(-1, 0) = 1, \qquad d(-1, 2) = 3, \qquad d(0, 2) = 2,
$$

which agrees with the positional picture: on the line the points are ordered
$-1 < 0 < 2$, and the closest two are the ones with nothing between them. The reported
attribute `shortest` therefore holds $1$.

## 5. Correctness and the Adjacency Invariant

> **Invariant of the oriented scan.** During the sweep, every unordered pair of distinct
> positions has had its difference evaluated exactly once, and the running minimum equals
> the smallest difference among the pairs evaluated so far.

Combining the invariant with trichotomy gives the correctness of the aggregate. Every
candidate value is the absolute difference of two distinct stored positions because the
strict orientation makes it positive and equal to the true distance; every unordered pair
appears exactly once, so no distance is missed; and the streaming minimum always ends
holding the smallest examined value. Hence the aggregate is
$\min_{i \ne j} d(x_i, x_j)$.

There is a stronger structural statement hiding here, and it is what the follow-up question
is asking for. Sort the positions into

$$
x_{(1)} < x_{(2)} < \dots < x_{(N)},
$$

let $g_k = x_{(k+1)} - x_{(k)}$ be the gap between consecutive sorted positions, and let
$G = \min_k g_k$ be the smallest gap.

> **Adjacency invariant.** For a finite set of distinct positions,
> $\min_{i \ne j} \lvert x_i - x_j \rvert = \min_k (x_{(k+1)} - x_{(k)})$.

*Proof.* Let $x_{(i)} < x_{(j)}$ attain the minimum, with $i < j$. Their difference is the
sum of the consecutive gaps between them,
$x_{(j)} - x_{(i)} = g_i + g_{i+1} + \dots + g_{j-1}$, and every term of that sum is
positive, so it is at least each individual gap and in particular at least $G$. Hence the
minimum over all pairs is at least $G$. Conversely $G$ is itself the difference of two
distinct positions, so the minimum over all pairs is at most $G$. The two bounds meet, so
the two minima are equal. $\square$

For the instance the sorted order is $-1, 0, 2$ and the gaps are $g_1 = 1$ and $g_2 = 2$,
whose minimum is $1$ — the same answer the pairwise scan produced, obtained from two
comparisons instead of three.

| Sorted rank $k$ | Position $x_{(k)}$ | Next position | Gap $g_k$ | Running smallest gap |
|---|---|---|---|---|
| 1 | $-1$ | $0$ | $1$ | $1$ |
| 2 | $0$ | $2$ | $2$ | $1$ |
| 3 | $2$ | none | — | $1$ |

## 6. Boundary Conditions and Traps

| Scenario | Input positions | Expected `shortest` | Observation |
|---|---|---|---|
| Exactly two rows | $0$, $1000$ | `1000` | The smallest legal input; the single pair is the answer |
| Both positions negative | $-10$, $-8$, $-5$ | `2` | Differences are computed on the positions, never on their magnitudes |
| Positions straddling zero | $-3$, $0$, $4$ | `3` | Sign of the coordinates is irrelevant once orientation is fixed |
| Adjacent integers | $7$, $8$ | `1` | A difference of $1$ is the smallest possible value for distinct integers |
| Very large separation | positions more than $2^{31}$ apart | their exact difference | A width hazard rather than a stated bound: a wrapped 32-bit difference can masquerade as the smallest distance |
| Two rows, descending input order | $5$, $1$ | `4` | Input order does not affect the result; only the comparison does |

Traps that this instance exposes:

- **Aggregating a signed difference.** Removing the self-pairs only with "positions are
  unequal" leaves both orientations in the candidate set, and the minimum then returns the
  most negative value rather than the smallest distance. The strict orientation is what
  makes the subtraction safe.
- **Admitting equality in the comparison.** Relaxing the strict comparison to "not
  greater" readmits a self-pair whose difference is $0$ and collapses the answer to zero.
  Here the uniqueness of `x` guarantees that two rows never share a position, so a
  non-strict comparison has no compensating benefit.
- **Ignoring the guaranteed minimum size.** The problem promises at least two rows, so the
  aggregate over candidates is never empty. If that guarantee were absent, the minimum of
  an empty candidate set would be the null value and the contract would have to admit it.
- **Aliasing the output attribute.** The single returned column must be named `shortest`;
  a default computed-column name fails the result-shape check even when the value is right.

## 7. Complexity Derivation

Let $N$ be the number of stored positions. The input guarantee gives $N \ge 2$.

**Oriented pairwise scan.** The Cartesian product contributes $N^2$ ordered pairs; the
strict orientation keeps exactly $\binom{N}{2} = \frac{N(N-1)}{2}$ of them. Each kept pair
costs one comparison to test orientation plus one subtraction, both $\Theta(1)$, so the
scan is

$$
\Theta(N^2) \ \text{time with } \Theta(1) \text{ auxiliary space},
$$

because a streaming minimum needs only the current best value and no intermediate
relation.

**Sorted adjacency scan.** Ordering the positions costs $\Theta(N \log N)$ time and
$\Theta(N)$ space for the sorted copy, after which a single pass compares each position with
its successor, taking $\Theta(N)$ further time. The total is

$$
\Theta(N \log N) \ \text{time and } \Theta(N) \text{ auxiliary space},
$$

which dominates the quadratic scan for all but the smallest inputs. This is precisely the
improvement the statement's follow-up points at: when the positions arrive already in
ascending order, no sort is needed at all and the pairwise scan collapses to a single
$\Theta(N)$ pass over adjacent rows, still with $\Theta(1)$ working memory.

**Numeric range.** Positions may be far enough apart that their difference exceeds the
range of a signed 32-bit integer — two positions separated by $2 \times 10^9$ already do —
so the subtraction should be carried out in 64-bit integer arithmetic. This is a real
hazard because an overflowing difference can wrap to a large negative number and be
selected by the minimum aggregate as if it were the smallest distance.