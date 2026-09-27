# Guided Example: Triangle Judgement

The `Triangle` table stores one row per triple of segment lengths $(x, y, z)$, and
$(x, y, z)$ is the primary key, so no two rows repeat. For every stored triple we must
decide whether those three segments can close into a non-degenerate triangle, and report
the original lengths alongside a fourth attribute `triangle` holding exactly `'Yes'` or
`'No'`.

The interesting content of this problem is geometric, not relational: the entire decision
is a conjunction of three strict inequalities, and the lesson explains why that
conjunction is both necessary and sufficient, why the strictness cannot be relaxed, and
why evaluating all three comparisons is safer than pre-selecting the longest side.

## 1. The Instance and the Predicate Contract

Input relation `Triangle`:

| `x` | `y` | `z` |
|---|---|---|
| 13 | 15 | 30 |
| 10 | 20 | 15 |

Required output relation, in any row order:

| `x` | `y` | `z` | `triangle` |
|---|---|---|---|
| 13 | 15 | 30 | `No` |
| 10 | 20 | 15 | `Yes` |

Note what the contract does and does not ask for. The three original attributes are
projected through unchanged — the predicates are never allowed to rewrite the stored
lengths — and exactly one attribute is appended. The appended literal is a string with
fixed casing, so `'YES'`, `'yes'`, and `'true'` are all incorrect answers even though
they carry the same meaning to a human reader.

## 2. The Triangle Inequality as a Closure Condition

Given three positive lengths, the geometric question is whether the two endpoints of the
longest segment can be joined by the other two segments. That happens exactly when the
three inequalities below all hold:

$$
x + y > z, \qquad x + z > y, \qquad y + z > x .
$$

Each inequality says "the path that detours through the third side can outrun the direct
side". The conjunction is usually summarized as

$$
\max(x, y, z) < x + y + z - \max(x, y, z),
$$

that is, the longest side is shorter than the sum of the other two.

| Situation | Numeric witness | What the geometry does | Verdict |
|---|---|---|---|
| Every inequality holds with slack | $(3, 4, 5)$ | The two shorter sides meet above the longest one and enclose positive area | `Yes` |
| One inequality holds with equality | $(2, 3, 5)$ | The two shorter sides lie flat along the longest one; the "triangle" has zero area and collapses to a segment | `No` |
| One inequality fails outright | $(13, 15, 30)$ | The two shorter sides stop short of bridging the gap; the endpoints never meet | `No` |
| All three sides equal | $(7, 7, 7)$ | The strongest possible slack, $14 > 7$ in each direction | `Yes` |

The equality row is the whole reason the comparison must be strict. Allowing
$\ge$ would classify every collinear triple as a triangle, and a degenerate triple has no
enclosed region, no interior angle, and no valid area.

## 3. Why the Three Comparisons Are Kept Even Though One Decides

Suppose the lengths of a row are positive and let $z$ be the largest of the three. Two of
the three inequalities then hold automatically:

$$
y + z > z \ge x \quad\text{and}\quad x + z > z \ge y,
$$

where both steps are strict because the added term is positive. Only the inequality whose
right-hand side is the largest entry, namely $x + y > z$, can fail. So the conjunction is
logically equivalent to a single test on the maximum.

The conjunction is nevertheless the better relational formulation, because the maximum is
not a stored attribute. Selecting it costs either a row-wise three-way comparison or a
sort, whereas the three pairwise tests read the three stored values directly and add no
state at all.

| Formulation | What it needs from the row | Behaviour on this instance | Trade-off |
|---|---|---|---|
| All three pairwise sums | Nothing beyond $x, y, z$ | Row 1 fails at the first comparison | No pre-processing; three additions and three comparisons per row |
| Compare each side with the sum of the others | Nothing beyond $x, y, z$ | Identical verdict | Same cost, phrased asymmetrically |
| Longest side against the sum of the rest | The maximum of the triple | Identical verdict | Needs an extra selection step per row |
| Sort the triple, then test the largest | An ordered triple | Identical verdict | Sorting is wasted work for three elements |

All four agree on the verdict; they differ only in the work that precedes it. The pairwise
conjunction keeps the whole computation inside a single streaming pass.

## 4. Row-by-Row Evaluation

**Row 1 — the triple $(13, 15, 30)$.** The first comparison already decides the row:

$$
13 + 15 = 28 \quad\text{and}\quad 28 > 30 \ \text{is false}.
$$

A detour of length $28$ cannot span a direct segment of length $30$, so the endpoints of
the long segment never meet. The remaining comparisons are irrelevant — a conjunction
fails as soon as one conjunct fails — and the row is answered `No`.

**Row 2 — the triple $(10, 20, 15)$.** Here no comparison is decisive on its own, so all
three are evaluated:

$$
10 + 20 = 30 > 15, \qquad 10 + 15 = 25 > 20, \qquad 20 + 15 = 35 > 10 .
$$

Every conjunct holds, so the conjunction holds and the row is answered `Yes`.

The complete evaluation, with the computed sum recorded for each comparison:

| `x` | `y` | `z` | $x + y$ vs $z$ | $x + z$ vs $y$ | $y + z$ vs $x$ | Conjunction | `triangle` |
|---|---|---|---|---|---|---|---|
| 13 | 15 | 30 | $28 > 30$ false | $43 > 15$ true | $45 > 13$ true | false | `No` |
| 10 | 20 | 15 | $30 > 15$ true | $25 > 20$ true | $35 > 10$ true | true | `Yes` |

The two rows also show why a "check only the largest against the sum of the others"
shortcut must first *identify* the largest. In row 2 the largest entry is $y = 20$, in row
1 it is $z = 30$; a fixed positional test would be wrong for one of them.

## 5. Correctness: Necessity and Sufficiency

> **Theorem.** For positive lengths $x, y, z$, the three pairwise strict inequalities hold
> if and only if the segments bound a non-degenerate triangle.

*Necessity.* Suppose one inequality fails, say $x + y \le z$. Any broken line made of the
segments of length $x$ and $y$ has total length at most $z$, so its endpoints cannot be
farther apart than $z$. Placing those two segments between the endpoints of the segment of
length $z$ either leaves a gap (when $x + y < z$) or forces the whole broken line to lie
flat inside the long segment (when $x + y = z$). Neither case bounds a region, so a valid
triangle requires the strict inequality. The same argument applies to each of the three
pairs by symmetry.

*Sufficiency.* Assume all three inequalities hold and let $z$ be the longest side. Place
the segment of length $z$ with endpoints $A$ and $B$, and draw the circle of radius $x$
centred at $A$ and the circle of radius $y$ centred at $B$. Two circles intersect in two
distinct points exactly when the distance between their centres lies strictly between the
difference and the sum of their radii, that is when
$\lvert x - y \rvert < z < x + y$. The upper bound is precisely the inequality
$x + y > z$. The lower bound also comes from our hypotheses: if $x \ge y$ then
$z > x - y = \lvert x - y \rvert$ is exactly the inequality $y + z > x$, and if $y \ge x$
the same role is played by $x + z > y$; when $x = y$ the difference is $0 < z$ because
lengths are positive. An intersection point $C$ therefore exists off the line $AB$, and
$ABC$ is a triangle of positive area.

*Why the relational formulation preserves the theorem.* The conditional projection is a
pure function of the row: it evaluates a fixed boolean expression on $(x, y, z)$ and emits
a literal. It cannot alter the lengths, cannot reorder the pairs, and cannot depend on any
other row, so rows are decided independently and duplicate triples are decided
consistently.

> **Invariant.** During the sweep, the appended attribute of each emitted row equals
> `'Yes'` precisely when the three stored lengths satisfy the strict triangle inequality;
> the first three attributes of every emitted row are byte-identical to the stored row.

## 6. Boundary Conditions and Grading Traps

| Scenario | Input row | Expected `triangle` | Reason |
|---|---|---|---|
| Degenerate collinear triple | $(1, 2, 3)$ | `No` | $1 + 2 = 3$: equality is not strict |
| Isosceles just inside the boundary | $(5, 5, 9)$ | `Yes` | $10 > 9$, a single unit of slack |
| Isosceles exactly at the boundary | $(5, 5, 10)$ | `No` | $10 > 10$ is false |
| Equilateral | $(7, 7, 7)$ | `Yes` | Maximum symmetry, maximum slack |
| Narrow but valid | $(1, 1000, 1000)$ | `Yes` | $1000 < 1000 + 1$ |
| Largest side in the middle column | $(2, 9, 3)$ | `No` | A positional test must not assume the last column is longest |
| Repeated input rows | two identical $(3, 4, 5)$ rows | two identical `Yes` rows | $x, y, z$ is the primary key in principle, but the projection is row-wise and idempotent |
| Empty relation | no rows | empty relation with the same four attributes | A projection over no rows produces no rows |

Three traps recur in submitted solutions:

- **Relaxing the comparison to $\ge$.** This admits the $(1, 2, 3)$ family and turns a
  zero-area collinear triple into a false `Yes`. The strictness is a semantic
  requirement, not a stylistic preference.
- **Testing one fixed pair.** Checking only $x + y > z$ is correct only once $z$ is known to
  be the largest entry, which a stored row does not promise. All three pairs must be tested,
  or the maximum genuinely identified.
- **Emitting the wrong literal or dropping attributes.** The appended value must be exactly
  `'Yes'` or `'No'`, and the output must still carry the three original lengths; replacing
  them with the decision loses required information.

## 7. Complexity Derivation

Let $N$ be the number of rows in `Triangle`. Every row is processed independently and its
cost does not grow with the relation:

- three integer additions produce the three sums;
- three integer comparisons produce the three conjuncts;
- one logical conjunction, one null-free conditional selection, and one projection of four
  attributes complete the row.

Because each row performs a constant number $c$ of fixed-size operations, the total work
is $cN = \Theta(N)$. The relation is consumed exactly once and no intermediate relation is
materialized, so the sweep streams. Even the worst case of evaluating all three
comparisons costs a constant factor, not an asymptotic factor, more than the single
decisive comparison would.

Auxiliary space is $\Theta(1)$: the decision needs three stored lengths, three sums, and
one boolean, all bounded by a constant. Only the emitted rows accumulate, and those rows
are the output of the query rather than working memory. If the input were ordered and a
sort were introduced to find the maximum, the bound would rise to $\Theta(N \log N)$ time
and $O(N)$ space — another reason to prefer the direct pairwise conjunction.

One numeric remark: the sums reach $2 \times 10^9$ when both operands are near $10^9$, so
the arithmetic needs a width that cannot wrap; 64-bit integer evaluation satisfies this
without special handling, and no sum can be negative because lengths are positive.