# Guided Example: Form a Chemical Bond

## 1. What the bond condition actually tests

The `Elements` relation describes one chemical element per row: `symbol` (the
primary key, hence unique), `type`, and `electrons`. The `type` column is an enum
over `('Metal', 'Nonmetal', 'Noble')`, and the `electrons` column is documented
per type: `0` for a noble element, the number of electrons one atom can *give*
for a metal, and the number of electrons one atom *needs* for a nonmetal.

The rule that defines a bond in this problem is purely categorical:

> Two elements can form a bond if one of them is a `'Metal'` and the other is a
> `'Nonmetal'`.

There is no arithmetic in that sentence. The `electrons` column is descriptive
metadata about the elements, not a matching key, and no comparison between a
metal's supply and a nonmetal's demand is part of the contract. That distinction
is the whole lesson: the answer is the complete pairing of the two role lists,
and the tempting "balanced electrons" rule is eliminated by the specification
itself.

Because the output schema is the ordered pair of columns `(metal, nonmetal)`, the
answer is the full product of the metal list $M$ and the nonmetal list $N$:

$$
\text{answer} = M \times N = \{\, (a, b) : a \in M,\ b \in N \,\},
\qquad
\lvert \text{answer} \rvert = \lvert M \rvert \cdot \lvert N \rvert .
$$

## 2. The official instance, sorted by role

The official example contains seven elements. Reading them in storage order hides
the structure, so the first step is to classify every row by its `type` and note
whether it can play a role at all.

| `symbol` | `type` | `electrons` | role in a bond |
|:---:|:---|:---:|:---|
| `He` | Noble | 0 | none — excluded by both sides of the rule |
| `Na` | Metal | 1 | metal (electron donor) |
| `Ca` | Metal | 2 | metal (electron donor) |
| `La` | Metal | 3 | metal (electron donor) |
| `Cl` | Nonmetal | 1 | nonmetal (electron acceptor) |
| `O` | Nonmetal | 2 | nonmetal (electron acceptor) |
| `N` | Nonmetal | 3 | nonmetal (electron acceptor) |

So $M = \{\texttt{Na}, \texttt{Ca}, \texttt{La}\}$ with $\lvert M \rvert = 3$ and
$N = \{\texttt{Cl}, \texttt{O}, \texttt{N}\}$ with $\lvert N \rvert = 3$. The
predicted number of result rows is $\lvert M \rvert \cdot \lvert N \rvert = 9$,
while `He` contributes nothing: `Noble` is neither of the two required types, so
no filter can ever admit it.

## 3. The pairing as a complete grid

Writing the pairing as a grid makes it obvious that every metal is joined with
every nonmetal and that nothing else is emitted.

| metal $\backslash$ nonmetal | `Cl` | `O` | `N` |
|:---:|:---:|:---:|:---:|
| `Na` | `Na` with `Cl` | `Na` with `O` | `Na` with `N` |
| `Ca` | `Ca` with `Cl` | `Ca` with `O` | `Ca` with `N` |
| `La` | `La` with `Cl` | `La` with `O` | `La` with `N` |

All nine cells are valid bonds, which matches the official expected output of nine
rows. Two structural facts are visible in the grid:

- The diagonal notion of "an element bonding with itself" cannot arise. A row has
  exactly one `type`, so no row is simultaneously a metal and a nonmetal, and
  every emitted pair therefore consists of two different symbols.
- The grid is a *directed by role* product, not the set of unordered pairs. The
  pair containing `Na` and `Cl` appears once, in the cell whose row is `Na` and
  whose column is `Cl`. The mirror cell would name `Cl` as the metal column and
  `Na` as the nonmetal column, which the `type` values forbid. Emitting each
  physical pair exactly once is therefore automatic, not a de-duplication step.

## 4. Why the electron counts must not enter the test

The `electrons` column is the trap of this problem. Since a metal supplies
electrons and a nonmetal needs them, a chemically motivated solver may want to
keep only pairs where the supply equals the demand. On the official instance that
alternative rule produces only the three diagonal matches `Na`–`Cl`, `Ca`–`O`,
and `La`–`N`, and it silently discards six rows that the specification requires.

| Rule applied | What it compares | Rows on the official instance | Consistent with the expected output |
|:---|:---|:---:|:---|
| Categorical rule (`Metal` with `Nonmetal`) | the `type` values only | 9 | yes |
| Electron-balance rule (supply equals demand) | `electrons` of the two sides | 3 | no — drops `Na`–`O`, `Na`–`N`, and six more |
| Either side may be `Noble` | `type` contains the substring `Noble` | extra rows | no — `Noble` is neither Metal nor Nonmetal |

The authored `trial-electrons-do-not-filter` instance settles the question
independently: it pairs metal `Al` with `electrons = 3` against
`Cl` (`electrons = 1`) and `S` (`electrons = 2`), and the expected output contains
*both* `Al`–`Cl` and `Al`–`S`. A supply of three matching neither demand of one
nor demand of two is still required to bond, so the counts demonstrably play no
role in deciding membership.

## 5. What the output shape guarantees

| Property of the result | Holds? | Reason |
|:---|:---|:---|
| one row per `(metal, nonmetal)` choice | yes | the product $M \times N$ has exactly $\lvert M \rvert \lvert N \rvert$ cells |
| roles are fixed by column, not by pair order | yes | the schema names the first column `metal` and the second `nonmetal` |
| a physical pair is emitted twice | no | the reversed naming would require the nonmetal row to be typed `Metal` |
| an element can bond with itself | no | `type` is single-valued, so no row belongs to both lists |
| duplicate rows | no | `symbol` is the primary key, so each role list has distinct symbols |
| `Noble` rows appear | no | both filters require `Metal` and `Nonmetal` respectively |
| a stable row order is required | no | the result is accepted in any order, so no ordering work is warranted |

The last row is worth acting on. Because ordering is free, the method needs no
sorting, no grouping, and no ranking; it only has to enumerate the product and
filter it.

## 6. Why matching every metal with every nonmetal is correct

The invariant is a set identity. Let $R$ be the emitted relation. The claim is

$$
R = \{\, (a, b) \;:\; a, b \in \texttt{Elements},\
a.\texttt{type} = \texttt{'Metal'},\ b.\texttt{type} = \texttt{'Nonmetal'} \,\}.
$$

*Soundness.* Every emitted row is built from one row of the relation placed in the
metal role and another placed in the nonmetal role, and the admission test requires
`a.type = 'Metal'` and `b.type = 'Nonmetal'`. So every emitted row satisfies the
defining condition of a bond.

*Completeness.* Conversely, take any ordered pair $(a, b)$ satisfying the
condition. A systematic scan that walks every row of `Elements` against every row
of `Elements` — the full cross product of the relation with itself — considers
$(a, b)$ at least once, because `a` and `b` are both rows of the relation. Since
both of their type tests hold, the pair passes the filter and is emitted. Hence no
qualifying pair is missed.

The two directions together give the set identity, and the cardinality follows
immediately: the filter admits exactly the cells of the role grid of section 3,
so the result has $\lvert M \rvert \cdot \lvert N \rvert$ rows. This argument also
shows why the `electrons` requirement cannot be inserted: doing so would make the
emitted relation a strict subset of the right-hand side and break completeness,
exactly as the three-row alternative of section 4 does.

## 7. Boundary conditions the authored instances expose

| Instance | Situation | $\lvert M \rvert \cdot \lvert N \rvert$ | Rows returned |
|:---|:---|:---:|:---:|
| `Li` (Metal), `F` (Nonmetal) | smallest non-empty case | $1 \cdot 1$ | 1 |
| `Ar`, `Ne` (Noble), `K` (Metal), `Br` (Nonmetal) | noble rows present around a valid pair | $1 \cdot 1$ | 1 |
| `O` (Nonmetal), `Ne` (Noble) | no metal at all | $0 \cdot 1$ | 0 |
| `Fe` (Metal), `He` (Noble) | no nonmetal at all | $1 \cdot 0$ | 0 |
| `Al` (Metal, 3), `Cl` (Nonmetal, 1), `S` (Nonmetal, 2) | electron counts deliberately mismatched | $1 \cdot 2$ | 2 |
| `M1`, `M2` (Metal), `X1`, `X2`, `X3` (Nonmetal) | larger product | $2 \cdot 3$ | 6 |

The two empty instances are the interesting ones, because a product with an empty
factor is empty: when either role list is missing, no pair can satisfy both
filters, and the method returns zero rows without any special branch. The noble
instance shows the same mechanism from the other direction — a row that is
excluded is not "skipped late"; it simply never lands in either role list.

## 8. Alternative formulations

| Formulation | How it pairs | Cost | Where it breaks down |
|:---|:---|:---|:---|
| Cross product of the relation with itself, filtered by the two type tests (used here) | enumerate every ordered pair of rows, keep the metal-first, nonmetal-second ones | $\Theta(n^2)$ candidate pairs | none for the stated output; the only cost is the redundant mirrored candidates |
| Collect the two role lists, then form their product | two scans to build $M$ and $N$, then $\lvert M \rvert \lvert N \rvert$ pairs | $\Theta(n + \lvert M \rvert \lvert N \rvert)$ | needs temporary lists for the two roles |
| Inner join on a role predicate | join rows whose types differ, then order the columns by role | comparable to the product | expressing "differ and one is Metal" is more clauses for the same result, and a plain inequality alone would also admit two rows of the same type |
| Emit both orderings and union them | produce each physical pair twice and de-duplicate | about twice the work plus a de-duplication pass | the schema forbids the reversed naming, so the second half of the union can never be valid |
| Concatenate the two symbols into one column | one string per pair | same product, different shape | the required output has two separate columns, so the shape is wrong even though the pairs are right |

The product formulation is the cleanest statement of the specification: it says
"every metal with every nonmetal" literally. A pairwise join on types is
equivalent but expresses the same set through an extra predicate, and the
de-duplication variant is wasted work because the role columns already make each
valid pair unique.

## 9. Complexity of the method

Let $n$ be the number of rows of `Elements`, $m = \lvert M \rvert$ the number of
metals, and $x = \lvert N \rvert$ the number of nonmetals, with $m + x \le n$ and
$\text{answer size} = m x$.

- **Time:** scanning the relation to identify the two role lists costs
  $\Theta(n)$. Enumerating the product of the two lists performs $m x$ admission
  tests, each a constant-cost type comparison, so the total is
  $\Theta(n + m x)$. A literal double scan of the relation without first
  projecting the roles inspects $n^2$ ordered candidate pairs and discards the
  $n^2 - m x$ pairs that fail a type test, so materializing the role lists first
  is the cheaper organization.
- **Auxiliary space:** the role lists occupy $O(m + x)$ cells, i.e. $O(n)$ in the
  worst case, and each emitted pair consumes constant extra state. Counting the
  output separately, the auxiliary space is $O(m + x)$, which is $O(1)$ beyond
  the result when the roles can be streamed.

The one non-obvious reading is that the output itself is quadratic in the worst
case: if the relation splits evenly into metals and nonmetals, the answer has
about $n^2 / 4$ rows, while the input has $n$. Producing that many rows is
unavoidable because each of them is required, so the bound $\Theta(n + m x)$ is
output-sensitive rather than a sign of wasted computation.
