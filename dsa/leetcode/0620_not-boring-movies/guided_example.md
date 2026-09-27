# Guided Example: Not Boring Movies

This lesson filters a small cinema catalogue and orders what survives. A row
qualifies only when its ticket identifier is odd *and* its description differs
from the literal quality label `boring`; the survivors are then presented with
the highest rating first. The instance is chosen because each of the five rows
fails the test for a different reason — or for no reason at all — so every branch
of the conjunction is visible in one pass.

The catalogue is a single relation whose identifier is unique and whose rating is
a two-decimal value in the range $[0, 10]$.

| `id` | `movie` | `description` | `rating` |
|:---:|:---:|:---:|:---:|
| $1$ | `War` | `great 3D` | $8.9$ |
| $2$ | `Science` | `fiction` | $8.5$ |
| $3$ | `irish` | `boring` | $6.2$ |
| $4$ | `Ice song` | `Fantacy` | $8.6$ |
| $5$ | `House card` | `Interesting` | $9.1$ |

| `id` | `movie` | `description` | `rating` |
|:---:|:---:|:---:|:---:|
| $5$ | `House card` | `Interesting` | $9.1$ |
| $1$ | `War` | `great 3D` | $8.9$ |

The answer keeps all four attributes unchanged. It is a filtered and reordered
subset of the catalogue, not a projection onto fewer columns and not an
aggregation, so nothing about a qualified row's contents may be altered.

---

## 1. The Qualification Predicate and Its Two Independent Tests

The qualifying condition is the conjunction of two predicates over disjoint
attributes. Let $A(r)$ be the parity test and $B(r)$ the quality test:

$$
A(r) \equiv \bigl(r.\text{id} \bmod 2 = 1\bigr),
\qquad
B(r) \equiv \bigl(r.\text{description} \neq \text{'boring'}\bigr),
$$

$$
Q(r) \equiv A(r) \wedge B(r).
$$

Parity is arithmetic and reads only the identifier; the quality test is a string
comparison and reads only the description. No attribute appears in both tests, so
the two predicates are logically independent: knowing whether a row is odd tells
you nothing about whether its description is the excluded label, and vice versa.

Independence has an operational consequence that the contract quietly relies on.
Because the predicates commute and associate, the surviving set is the same
whether the parity test is applied first, the quality test is applied first, or
both are evaluated together. The intersection of the two restricted sets is the
restriction of the intersection:

$$
\sigma_{A \wedge B}(\text{Cinema})
= \sigma_{A}\bigl(\sigma_{B}(\text{Cinema})\bigr)
= \sigma_{B}\bigl(\sigma_{A}(\text{Cinema})\bigr).
$$

The tidy way to remember this is that selection restricts a relation; composing
two selections over disjoint attributes restricts it twice, and the order in which
the restrictions are imposed cannot change which tuples remain. This is *not* true
of arbitrary pairs of operations — an order-sensitive operation such as trimming a
relation to a fixed number of rows does not commute with a filter — so the
commutation here is a property of the predicates, not a general license.

Parity can be tested in several equivalent ways on non-negative integers: a
modular remainder test, an explicit modulus function, or a test on the lowest bit
of the binary representation. All three agree on the identifier domain here, and
the choice among them is a style decision with no semantic content.

## 2. Per-Row Evaluation of the Conjunction

Evaluating both predicates row by row separates the catalogue into qualifiers and
rejects, and it also shows how many *distinct* reasons for rejection exist:
even identifier, or excluded description.

| `id` | `movie` | Odd identifier $A$? | Description differs from `boring`, $B$? | $A \wedge B$ | Verdict | `rating` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `War` | yes | yes | true | qualified | $8.9$ |
| $2$ | `Science` | no | yes | false | rejected on parity | $8.5$ |
| $3$ | `irish` | yes | no | false | rejected on description | $6.2$ |
| $4$ | `Ice song` | no | yes | false | rejected on parity | $8.6$ |
| $5$ | `House card` | yes | yes | true | qualified | $9.1$ |

Three rows are rejected, and they are not rejected for a single shared reason.
Row $2$ and row $4$ have acceptable descriptions but even identifiers; row $3$
has an odd identifier but the excluded description. Row $3$ is the informative
one: it would pass a filter that tested either condition alone on the odd
identifiers, because it is odd, and it would pass the quality test's complement if
the exclusion were not stated. Only the conjunction removes it.

Only rows $1$ and $5$ clear both tests, so the candidate set before ordering is
$\{(\text{id } 1, 8.9), (\text{id } 5, 9.1)\}$.

## 3. Ordering the Survivors by Descending Rating

The required presentation order is by `rating` descending, and the comparison
here is a numerical one on a fixed-precision decimal, not a lexicographic one on a
string. With two survivors the ordering step is immediate: $9.1 > 8.9$, so row $5$
takes the first position and row $1$ the second.

| Position | `id` | `movie` | `rating` | Reason for the position |
|:---:|:---:|:---:|:---:|:---|
| $1$ | $5$ | `House card` | $9.1$ | largest rating among the survivors |
| $2$ | $1$ | `War` | $8.9$ | second largest rating among the survivors |

Two properties of this step are worth isolating. First, the order is applied to
the survivors only, never to the full catalogue, so the relative positions of
rejected rows are irrelevant to the answer. Second, the sort key is the rating and
not the identifier; sorting by the identifier would place `War` first and produce
a relation that is correctly filtered but incorrectly ordered.

The final relation is the two surviving tuples in the order above. Every surviving
attribute is carried through untouched: the `movie` and `description` values of
rows $1$ and $5$ are exactly what the catalogue stored, and only their position
changed.

## 4. The Conjunction Invariant and Why the Order Preserves It

The reasoning has three parts, and the invariant that ties them together is
membership itself: a row belongs to the result exactly when both predicates hold
of it, and no later operation is allowed to add to or remove from that set.

*Filters are pure selections.* Each predicate keeps or drops a tuple without
altering it, so every tuple in the result is a tuple of the input. Since the
contract asks for rows of the catalogue rather than for derived values, this is
the correct class of operation, and no projection, join, or aggregation belongs
anywhere in the plan.

*The conjunction is exact.* A row appears in the result if and only if both
predicates hold. Row $3$ confirms the "only if" direction, since it satisfies
one predicate and is still excluded; rows $1$ and $5$ confirm the "if" direction,
and rows $2$ and $4$ confirm that parity alone can reject a row whose description
is acceptable. Enumerating the four combinations of the two boolean outcomes
shows that exactly one combination is admitted:

| $A(r)$ | $B(r)$ | $Q(r)$ | Behaviour |
|:---:|:---:|:---:|:---|
| true | true | true | admitted — this is the only accepting combination |
| true | false | false | rejected, as row $3$ shows |
| false | true | false | rejected, as rows $2$ and $4$ show |
| false | false | false | rejected by both predicates |

*Ordering does not change membership.* Sorting permutes the surviving tuples and
adds no tuple and removes none, so composing the selection with the ordering
cannot corrupt the filter. The only requirement the ordering must meet is
comparison on the rating attribute in decreasing order, and the total order on
ratings makes that well defined for any number of survivors.

Together these give the guarantee the contract needs: the result contains exactly
those catalogue rows satisfying both tests, each appearing once, presented in
non-increasing rating order.

One subtlety about equality of ratings is worth recording even though this
instance has no tie. Two rows with the same rating both survive the filter, and
because their rating values are equal the sort key does not distinguish them;
either relative order between them satisfies "ordered by rating descending". The
instance deliberately avoids a tie, but a correct plan must not *drop* one of the
tied rows.

## 5. Traps This Instance Exposes

| Trap | Effect on this instance |
|:---|:---|
| Combining the predicates with disjunction instead of conjunction | Rows $2$ and $4$ have acceptable descriptions, so they enter the result on the strength of passing one predicate. The output gains two rows that the contract excludes. |
| Applying the parity test to the rating or the quality test to the movie title | The tests read the wrong attributes. A row whose title happens to be `boring` must still qualify if its description differs from the label, because only the description column carries the exclusion. |
| Sorting ascending instead of descending | The two survivors are emitted in the reverse order, placing the $8.9$ rating above the $9.1$ rating. |
| Sorting on the identifier rather than the rating | The rows are correctly chosen but wrongly arranged. |
| Projecting a subset of the columns | The answer's schema is all four attributes; emitting only `movie` and `rating` does not match the required relation. |
| Treating the parity test as a bit test on a signed value without care | For the non-negative identifiers in the contract the test is unambiguous, but the reasoning depends on the identifier domain rather than on the operator spelling. |

Two boundary conditions behave as the definition requires rather than as special
cases. An identifier of $0$ is even and therefore rejected, so a catalogue that
begins at $0$ still loses that row. A `null` description is not equal to the
label `boring`, so the quality predicate `description ≠ 'boring'` evaluates to
unknown rather than to true, and the row is not admitted by the conjunction; the
exclusion is a comparison against a specific string, not a general "has content"
requirement.

## 6. Complexity Derivation

Let $N$ be the number of catalogue rows and $K$ the number that clear both
predicates, so $K \le N$. In this instance $N = 5$ and $K = 2$.

Filtering is one sequential pass over the relation. Each row requires one parity
test on an integer and one string comparison against a fixed literal; both are
constant work, so the filtering stage costs $O(N)$ time and needs only constant
working state per scanned row.

Ordering operates on the survivors, so it costs $O(K \log K)$ for a general
comparison sort. That is at most $O(N \log N)$ and is the stage that dominates.
If a declared ordering index on the rating attribute can supply the rows in
descending rating order while the predicates are applied, an engine may avoid the
explicit sort and approach $O(N)$, but the table contract does not promise such an
index, so a bound independent of physical design must assume the sort.

| Stage | Cost | Notes |
|:---|:---:|:---|
| Scan the $N$ rows and test both predicates | $O(N)$ | constant work per row; $K$ rows survive |
| Order the $K$ survivors by descending rating | $O(K \log K)$ | at most $O(N \log N)$ |
| Emit the ordered survivors | $O(K)$ | output size depends on the filters, not on $N$ |

The engine-independent time bound is therefore $O(N \log N)$.

Auxiliary space is $O(K)$ and hence $O(N)$ in the worst case. The sort
materializes row references or row copies for the survivors, and external sorting
may move that workspace to disk without changing how much of it exists. The
filter itself adds only $O(1)$ state through two predicate evaluations, and the
output relation holds exactly $K$ rows. When the filters are very selective — as
they are here, where $K = 2$ out of $N = 5$ — the auxiliary workspace shrinks with
$K$ rather than with $N$.
