# Guided Example: Shortest Distance in a Plane

The `Point2D` table stores distinct integer coordinate pairs $(x, y)$. The task is to
report, as a single attribute named `shortest`, the smallest Euclidean distance between
any two distinct stored points, rounded to two digits after the decimal point.

Two decisions dominate this problem. The first is which pairs of rows are legitimate
candidates at all: a point has distance zero from itself, so careless pairing makes the
minimum trivially zero. The second is that the reported number must be the *distance*, not
its square, and rounding happens only at the end. The worked instance below is the
official one, and its answer is produced by a vertical pair whose $x$-coordinates are
equal — exactly the case that a plausible-looking but wrong distinctness predicate would
discard.

## 1. The Instance and the Distance Contract

`Point2D` holds two `int` columns, `x` and `y`, which together form the primary key.

Input relation:

| `x` | `y` |
|---|---|
| -1 | -1 |
| 0 | 0 |
| -1 | -2 |

Required output relation:

| `shortest` |
|---|
| 1.00 |

For points $p_1 = (x_1, y_1)$ and $p_2 = (x_2, y_2)$ the Euclidean distance is

$$
d(p_1, p_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.
$$

The contract asks for the minimum of $d$ over unordered pairs of *distinct* rows, rounded
to two decimal places. Row order in the result is irrelevant because the result is a
single scalar row.

## 2. Candidate Pairs and the Self-Pair Trap

Let $N$ be the number of stored points. A naive pairing of every row with every row
produces $N^2$ ordered pairs, and among them $N$ are self-pairs whose distance is exactly
$0$. If a self-pair survives the filter, the minimum is $0$ for every input, and the
problem becomes vacuous — so the filter is the only thing standing between the query and a
constant wrong answer.

Two rows are distinct exactly when they differ in at least one coordinate:

$$
p_1 \ne p_2 \iff x_1 \ne x_2 \ \lor \ y_1 \ne y_2 .
$$

The alternatives to this predicate have different consequences, and the differences are
the heart of the lesson.

| Distinctness predicate | Self-pairs admitted | Kept pairs for $N = 3$ | Effect on this instance |
|---|---|---|---|
| No filter at all | all $N$ self-pairs | $9$ ordered | Minimum becomes $0$; wrong |
| Both coordinates must differ | none | $2$ ordered | Drops $(-1,-1)$ vs $(-1,-2)$; returns $1.41$ instead of $1.00$; wrong |
| At least one coordinate differs | none | $6$ ordered | Correct, but every unordered pair is evaluated twice |
| Coordinate-lexicographic order | none | $3$ unordered | Correct and each unordered pair is evaluated once |

The third row of the table is the decisive one. Points $(-1, -1)$ and $(-1, -2)$ share their
$x$-coordinate and differ only in $y$. Requiring *both* coordinates to differ therefore
discards them, and with them the true minimum of the instance. Coordinates are read
pairwise, so distinctness must be a disjunction, never a conjunction.

The fourth row is an optimization rather than a correctness requirement. A strict
lexicographic comparison keeps exactly one representative of each unordered pair:

$$
(x_1 < x_2) \ \lor \ (x_1 = x_2 \ \land \ y_1 < y_2).
$$

Because this predicate is antisymmetric, it selects exactly one of $p_1 \to p_2$ and
$p_2 \to p_1$ for every unequal pair. The tie-break on $y$ matters precisely when
$x_1 = x_2$, which is the configuration that decides this instance.

## 3. Worked Pair Enumeration

Name the points $A = (-1, -1)$, $B = (0, 0)$, and $C = (-1, -2)$. There are
$\binom{3}{2} = 3$ unordered pairs, and the lexicographic predicate keeps one ordered
representative of each:

| Unordered pair | Lower by lexicographic order | Kept orientation | $\Delta x$ | $\Delta y$ |
|---|---|---|---|---|
| $A, B$ | $A$ | $A \to B$ | $0 - (-1) = 1$ | $0 - (-1) = 1$ |
| $A, C$ | $C$ | $C \to A$ | $-1 - (-1) = 0$ | $-1 - (-2) = 1$ |
| $B, C$ | $C$ | $C \to B$ | $0 - (-1) = 1$ | $0 - (-2) = 2$ |

Squaring removes the sign of each difference, so the orientation chosen for a pair cannot
change its distance:

$$
d(p_1, p_2)^2 = (\Delta x)^2 + (\Delta y)^2 .
$$

Evaluating all three pairs:

$$
d(A,B)^2 = 1^2 + 1^2 = 2, \qquad
d(A,C)^2 = 0^2 + 1^2 = 1, \qquad
d(B,C)^2 = 1^2 + 2^2 = 5 .
$$

Taking square roots and ranking gives the full trace:

| Pair | $(\Delta x)^2$ | $(\Delta y)^2$ | Sum | Exact distance | Rounded | Rank |
|---|---|---|---|---|---|---|
| $A, C$ | $0$ | $1$ | $1$ | $1$ | `1.00` | 1 |
| $A, B$ | $1$ | $1$ | $2$ | $\sqrt{2} \approx 1.41421356$ | `1.41` | 2 |
| $B, C$ | $1$ | $4$ | $5$ | $\sqrt{5} \approx 2.23606798$ | `2.24` | 3 |

The minimum over the candidate set is $1$, attained by the vertical pair $A$ and $C$, and
rounding two digits past the decimal point leaves it as `1.00`.

## 4. Why the Squared Distance Cannot Be Reported

The square root is strictly increasing on the non-negative reals:

$$
0 \le u < v \implies \sqrt{u} < \sqrt{v}.
$$

Consequently the pair that minimizes the squared distance is the same pair that minimizes
the distance, and if an implementation only needs the *argmin* it may compare squared
values and never take a root. The reported value, however, is a distance, so the root must
be taken for the winning pair, and the rounding applies to the root rather than to the
square.

| Pair | Squared distance | If reported as-is | Actual distance | Contract value |
|---|---|---|---|---|
| $A, C$ | $1$ | `1.00` (coincidence) | $1$ | `1.00` |
| $A, B$ | $2$ | `2.00` (wrong) | $1.41421356$ | `1.41` |
| $B, C$ | $5$ | `5.00` (wrong) | $2.23606798$ | `2.24` |

The coincidence in the first row is instructive: squared and actual distances agree only
when the squared value is a perfect square, which happens for integer-coordinate points
exactly on a Pythagorean relation. For all other pairs the substitution silently inflates
the answer.

## 5. Correctness of the Minimum Selection

> **Invariant.** After each row of the candidate set has been examined, the running
> minimum equals the smallest distance among the pairs examined so far.

The invariant is established on the first candidate and preserved by a streaming minimum: a
newly examined distance either exceeds the running minimum, leaving it unchanged, or is
smaller, becoming the new minimum. The comparison is total on non-negative reals, and ties
may keep either value because tied values are equal, so the aggregate always ends holding
the true minimum of the examined set.

Completeness is the second half of the argument, and it is where the distinctness filter
does its work. Every unordered pair of distinct rows appears in the candidate set, because
the disjunctive predicate admits a pair whenever at least one coordinate differs and two
distinct rows always differ in at least one coordinate; every candidate value is a genuine
distance, because it is computed from the stored coordinates of two rows; and self-pairs,
whose value would be $0$, are excluded, so the minimum is attained by distinct points.

Soundness follows: the final aggregate is the distance of some pair of distinct stored
points, and no pair of distinct stored points was skipped. On this instance the aggregate
ends at $1$, which is exactly $d(A, C)$, and the required answer is `1.00`.

## 6. Boundary Conditions and Rounding Traps

| Scenario | Input points | Expected `shortest` | Observation |
|---|---|---|---|
| Exactly two points | $(0,0)$, $(3,4)$ | `5` | The single pair is returned; the value is a whole number |
| Closest pair shares $x$ | $(2,-3)$, $(2,5)$, $(2,6)$ | `1` | A vertical pair decides; a conjunctive filter would fail here |
| Closest pair shares $y$ | $(-10,7)$, $(-4,7)$, $(8,7)$ | `6` | Negative coordinates behave like any others |
| Several pairs tie for the minimum | $(0,0)$, $(0,2)$, $(2,0)$, $(2,2)$ | `2` | Ties need no special handling because only the value is reported |
| Nearest pair is far apart in input order | $(50,50)$, $(-100,-100)$, $(4,5)$, $(3,4)$ | `1.41` | The minimum is order-independent |
| Large coordinate magnitudes | $(-10000,-10000)$, $(10000,10000)$, $(9997,9996)$ | `5` | Squared coordinates reach $10^8$; 64-bit integer arithmetic is exact |
| Distance rounds upward | $(0,0)$, $(2,2)$ | `2.83` | $\sqrt{8} \approx 2.82842712$ rounds up to two digits |
| Distance rounds downward | $(0,0)$, $(-1,-1)$ | `1.41` | $\sqrt{2} \approx 1.41421356$ rounds down |

Traps worth naming explicitly:

- **Conjunction instead of disjunction.** Requiring both coordinates to differ removes
  every pair that shares a column. On the official instance this loses the unique minimum,
  so the error is not subtle — it changes the answer.
- **Letting self-pairs through.** Any filter that admits $p$ paired with $p$ makes the
  answer $0$ for all inputs. The failure is invisible on inputs whose true answer happens
  to be $0$ and total elsewhere.
- **Reporting before rounding, or rounding before minimizing.** Rounding is a non-injective
  map, so minimizing over rounded values can pick a pair that is not the true nearest one.
  The correct order is: compute exact distances, select the minimum, then round.
- **Rounding the wrong numeric type.** In engines where the rounding routine is defined only
  for exact decimal types, a floating-point distance must be converted before it is rounded.
  Square roots of integers are essentially never exactly halfway between two two-decimal
  values, so the rounding mode itself does not change the verdict here, but the conversion
  can make the call fail.
- **Emitting more than one row.** The contract is a single scalar row; returning every
  distance, or the minimum once per candidate, violates the result format.

## 7. Complexity Derivation

Let $N$ be the number of rows in `Point2D`.

**Candidate generation.** Pairing every row with every row is a Cartesian product of size
$N^2$. Under the disjunctive predicate each unordered pair survives twice, giving
$N(N-1)$ candidates; under the lexicographic predicate exactly $\frac{N(N-1)}{2}$ survive.
Both counts are $\Theta(N^2)$; the factor of two is a constant-factor saving.

**Per-candidate work.** Two subtractions, two multiplications, one addition, and one
square root, each on bounded-width numbers, so every candidate costs $\Theta(1)$.

**Aggregation.** A running minimum consumes the candidate stream in one pass with
$\Theta(1)$ state, giving total time

$$
\Theta(N^2) \quad\text{with}\quad \Theta(1) \text{ auxiliary space}.
$$

A sort-based alternative — materialize all candidates, order them by distance, keep the
first — costs $\Theta(N^2 \log N)$ time and $\Theta(N^2)$ space, because the whole
candidate relation must be stored before it can be ordered. The streaming minimum is
strictly better and is the reason the naive quadratic scan is acceptable here.

**Numeric range.** For coordinate magnitudes of order $10^4$, as in the large-coordinate
trial above, each squared difference is at most $10^8$ and their sum is at most
$2 \times 10^8$, which a 64-bit integer holds exactly; no overflow check is needed, and
converting that integer sum to floating point for the square root introduces no error at
this scale. Only much larger coordinates, where a single squared difference approaches
$2^{53}$, would make the exact-integer reasoning fail.
