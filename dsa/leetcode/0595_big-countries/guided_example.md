# Guided Example: Big Countries

We trace one horizontal selection over a fixed pair of inclusive thresholds. The
instance is chosen because its five countries cover the whole decision surface:
two countries qualify through the population test alone, two fail both tests with
one of them failing by a wide margin, and none qualifies through the area test —
yet the area test still has to be evaluated on every row.

- **Input relation** `World`, keyed by `name`:

    | `name` | `continent` | `area` | `population` | `gdp` |
    |:---|:---:|:---:|:---:|:---:|
    | `Afghanistan` | `Asia` | $652230$ | $25500100$ | $20343000000$ |
    | `Albania` | `Europe` | $28748$ | $2831741$ | $12960000000$ |
    | `Algeria` | `Africa` | $2381741$ | $37100000$ | $188681000000$ |
    | `Andorra` | `Europe` | $468$ | $78115$ | $3712000000$ |
    | `Angola` | `Africa` | $1246700$ | $20609294$ | $100990000000$ |

- **Required output** — `name`, `population`, and `area` of each big country:

    | `name` | `population` | `area` |
    |:---:|:---:|:---:|
    | `Afghanistan` | $25500100$ | $652230$ |
    | `Algeria` | $37100000$ | $2381741$ |

---

## 1. Instance & Teaching Goal

A country is **big** when it has an area of at least three million square
kilometres, **or** a population of at least twenty-five million. Report the
`name`, `population`, and `area` of every big country, in any order.

Write the two threshold predicates for a row $r$ as

$$
A(r) = \bigl(r.\texttt{area} \ge 3{,}000{,}000\bigr), \qquad
P(r) = \bigl(r.\texttt{population} \ge 25{,}000{,}000\bigr).
$$

The required membership test is their disjunction:

$$
B(r) \;=\; A(r) \;\lor\; P(r).
$$

The instance illustrates why the connective matters more than the thresholds. If
the contract had required both thresholds, the answer would be empty; with the
disjunction it contains two countries. On these five rows the two connectives
disagree completely:

| Connective | Logic | Countries satisfying it here | Result cardinality |
|:---|:---|:---|:---:|
| Conjunction | $A(r) \land P(r)$ | none | $0$ |
| Disjunction | $A(r) \lor P(r)$ | `Afghanistan`, `Algeria` | $2$ |
| Area disjunct alone | $A(r)$ | none | $0$ |
| Population disjunct alone | $P(r)$ | `Afghanistan`, `Algeria` | $2$ |

### Why every row still needs both tests

No country in the instance reaches the area threshold, which can create the
illusion that the area test is unnecessary. It is not. The area predicate is a
disjunct, so it can rescue a row whose population is small, and it also
determines which of the two reasons a country qualifies for. A selection is
defined by its predicate, not by whether this particular relation happens to
exercise every branch of it, and the instance's job is to make the
qualification *reasons* visible rather than to exercise every threshold.

---

## 2. The Selection Invariant

Membership is a per-row property, and this yields the invariant that governs the
whole computation.

> **Independent-rows invariant.** The predicate $B$ reads only attributes of its
> own row and compares them against constants. Nothing in $B$ refers to another
> row, so the selection is a pure horizontal restriction: it never adds a row,
> never removes two rows because of one row's fate, and never depends on the
> order in which rows are visited.

The invariant has three consequences that are easy to state and easy to get
wrong.

1. **Cardinality.** The output has exactly as many rows as the relation contains
   rows satisfying $B$; no row is duplicated. A disjunction is not a union of two
   selections unless duplicates are removed, because a row satisfying both
   disjuncts would be produced twice by a naive union of the two branches.
2. **Order independence.** Because no comparison spans rows, the surviving set is
   invariant under any permutation of the input. The contract's "any order"
   clause is therefore satisfiable trivially.
3. **Idempotence.** Applying the selection twice changes nothing, since a
   surviving row still satisfies $B$. A filter that is not idempotent is a sign
   that it is not a pure row-wise selection.

### The two predicates are partial indicators

Each predicate is a Boolean indicator over the relation. Their values on the five
rows are worth tabulating separately, because the qualifying rows are exactly
those whose indicator pair contains at least one true value:

| Row | $A(r)$: area $\ge 3{,}000{,}000$ | $P(r)$: population $\ge 25{,}000{,}000$ | $B(r) = A \lor P$ |
|:---|:---:|:---:|:---:|
| `Afghanistan` | $\mathit{False}$ | $\mathit{True}$ | $\mathit{True}$ |
| `Albania` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ |
| `Algeria` | $\mathit{False}$ | $\mathit{True}$ | $\mathit{True}$ |
| `Andorra` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ |
| `Angola` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ |

Both qualifying rows qualify through the population disjunct. Neither has a
true area indicator, which is why the area column of the output is entirely
sub-threshold — and precisely why the area values still belong in the projection:
they are required output attributes, not qualifying attributes.

### Inclusive thresholds and their null cases

Both thresholds are inclusive, so a value exactly equal to the constant qualifies
while a value one unit below does not. The predicates are simple at the
boundary because `area` and `population` are declared non-null integers:

| Value compared | `area >= 3000000` | `population >= 25000000` |
|:---|:---:|:---:|
| threshold $+1$ | $\mathit{True}$ | $\mathit{True}$ |
| threshold exactly | $\mathit{True}$ | $\mathit{True}$ |
| threshold $-1$ | $\mathit{False}$ | $\mathit{False}$ |
| absent value | not possible — the attribute is declared non-null | not possible — the attribute is declared non-null |

### Relational formulation

The pipeline is a horizontal selection followed by a vertical projection. The
selection restricts `World` to the rows satisfying
$A(r) \lor P(r)$; the projection keeps the three required attributes `name`,
`population`, and `area` and discards the two it does not need. The area and
population attributes appear in *both* stages, which is the source of a common
confusion: they are read as predicates and emitted as values, and a correct
method must not mistake one role for the other. The concrete spelling of the
selection and projection belongs to the Reference workflow.

For large relations an index-friendly alternative exists: splitting the
disjunction into two separate selections, one per threshold, taking the union of
their outputs. In engines holding separate sorted indexes on `area` and on
`population`, each branch becomes a range scan against its own index and the
union performs the set semantics that the disjunction requires. The two forms are
extensionally equal — they return the same rows — but they differ in physical
cost, and the union only preserves cardinality because union removes the rows
satisfying both branches.

---

## 3. Step-by-Step Worked Execution

### Step 1 — Scan the relation in key order

The relation is keyed by `name`, so a scan in key order visits the rows
alphabetically:

| Scan order | `name` | `continent` | `area` | `population` |
|:---:|:---|:---|:---:|:---:|
| $1$ | `Afghanistan` | `Asia` | $652230$ | $25500100$ |
| $2$ | `Albania` | `Europe` | $28748$ | $2831741$ |
| $3$ | `Algeria` | `Africa` | $2381741$ | $37100000$ |
| $4$ | `Andorra` | `Europe` | $468$ | $78115$ |
| $5$ | `Angola` | `Africa` | $1246700$ | $20609294$ |

### Step 2 — Evaluate the area predicate on every row

`Afghanistan` holds the largest area in the relation at $652230$ square
kilometres, and it is still more than four times smaller than the threshold. So
the area predicate is $\mathit{False}$ everywhere:

| `name` | `area` | $3{,}000{,}000 - \text{area}$ | $A(r)$ |
|:---|:---:|:---:|:---:|
| `Afghanistan` | $652230$ | $2347770$ | $\mathit{False}$ |
| `Albania` | $28748$ | $2971252$ | $\mathit{False}$ |
| `Algeria` | $2381741$ | $618259$ | $\mathit{False}$ |
| `Andorra` | $468$ | $2999532$ | $\mathit{False}$ |
| `Angola` | $1246700$ | $1753300$ | $\mathit{False}$ |

### Step 3 — Evaluate the population predicate on every row

Here the rows split. The shortfall column shows how far each failing row is from
the threshold:

| `name` | `population` | `population` vs $25{,}000{,}000$ | Shortfall or surplus | $P(r)$ |
|:---|:---:|:---:|:---:|:---:|
| `Afghanistan` | $25500100$ | exceeds | $+500100$ | $\mathit{True}$ |
| `Albania` | $2831741$ | below | $-22168259$ | $\mathit{False}$ |
| `Algeria` | $37100000$ | exceeds | $+12100000$ | $\mathit{True}$ |
| `Andorra` | $78115$ | below | $-24921885$ | $\mathit{False}$ |
| `Angola` | $20609294$ | below | $-4390706$ | $\mathit{False}$ |

### Step 4 — Combine the two indicators

Because $A$ is false on every row, the disjunction reduces to $P$ on this
instance. The combination is still evaluated as a disjunction:

| `name` | $A(r)$ | $P(r)$ | $B(r) = A \lor P$ | Decision |
|:---|:---:|:---:|:---:|:---|
| `Afghanistan` | $\mathit{False}$ | $\mathit{True}$ | $\mathit{True}$ | Keep |
| `Albania` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ | Drop |
| `Algeria` | $\mathit{False}$ | $\mathit{True}$ | $\mathit{True}$ | Keep |
| `Andorra` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ | Drop |
| `Angola` | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ | Drop |

### Step 5 — Project the required attributes

| `name` | `population` | `area` |
|:---:|:---:|:---:|
| `Afghanistan` | $25500100$ | $652230$ |
| `Algeria` | $37100000$ | $2381741$ |

Two of the five rows survive. `continent` and `gdp` are dropped by the
projection; `gdp` in particular was never consulted by the predicate and is
therefore irrelevant to the answer, however large it is.

---

## 4. Why the Reasoning Is Correct

**Soundness.** Suppose $B(r) = \mathit{True}$ for a surviving row $r$. Then at
least one disjunct holds. If $A(r)$ holds, the row's area is at least the
threshold, so the row is big. If $P(r)$ holds, its population is at least the
threshold, so the row is big. In either case the emitted row satisfies the
definition, and the projection copies its attributes unchanged, so no value in the
output has been altered.

**Completeness.** Suppose a row $r$ is big. By definition it satisfies $A(r)$ or
$P(r)$, so the disjunction is true and the selection retains it, and the
projection emits the three required attributes. Hence every big country in the
relation appears in the answer.

**Cardinality is preserved exactly.** The selection is a row-wise restriction, so
each input row contributes either zero or one output row; the projection is a
mapping applied independently to each surviving row and cannot merge two rows
into one, because it retains `name`, which is the primary key and therefore
distinct across rows. The answer's cardinality is thus exactly the number of rows
satisfying $B$, and no row can appear twice.

**The order clause is satisfiable trivially.** Because the predicate never
compares two rows, permuting the input permutes the answer without changing its
row set. Whichever order the engine emits is therefore acceptable, and the
implementation must not add an ordering step it does not need.

**The projection is exact, not convenient.** It is tempting to reason that since
the area predicate never fires here, the area column is decoration. The contract
requests `name`, `population`, and `area`, and `Afghanistan` is proof that a
qualifying row can carry a sub-threshold area that a reader needs to see. The
projection is dictated by the requested schema, not by which attribute caused
qualification.

---

## 5. Boundary and Degenerate Cases

| Instance | Rows satisfying the disjunction | Output | Teaching point |
|:---|:---|:---|:---|
| Area exactly $3{,}000{,}000$, small population | that row | that row | The threshold is inclusive: equality qualifies |
| Population exactly $25{,}000{,}000$, small area | that row | that row | Same inclusivity on the other predicate |
| Both attributes one unit below the thresholds | none | empty relation with the three requested columns | Below-threshold on both disjuncts is a rejection |
| Both predicates true at once | that row | that row exactly once | A row satisfying both disjuncts must not be duplicated |
| Every row satisfies both predicates | all rows | the whole relation | The selection degenerates to the identity |
| No row satisfies either predicate | none | empty relation with headers | A filter may legitimately return nothing |
| A row with enormous `gdp` and tiny area and population | none | absent | `gdp` is not part of the definition of big |
| Negative or zero area and population | none | absent | Both thresholds are positive, so such rows can never qualify |

The fourth row is where implementations break most often. A disjunction is
naturally implemented as the union of two branch selections, and if that union is
a multiset union rather than a set union, every row satisfying both disjuncts is
emitted twice. Set semantics are part of the answer, not an optimisation.

---

## 6. Traps This Instance Exposes

- **Conjunction instead of disjunction:** Requiring both thresholds returns an
  empty relation on this instance, because no country is both large and populous.
- **Strict inequality instead of inclusive:** Replacing "at least" with "greater
  than" discards rows sitting exactly on a threshold. The difference is invisible
  on this instance, where no row is near the area threshold, which is exactly why
  the boundary deserves its own case.
- **Projecting every column:** The response schema is three columns. Emitting
  `continent` or `gdp` as well violates it, and emitting only the two columns
  used as predicates omits a required attribute.
- **Testing the wrong attribute for a threshold:** Applying the area threshold to
  `population` or vice versa inverts the semantics; the two constants differ by
  an order of magnitude, and the confusion is silent on rows that fail both.
- **Believing the area test can be skipped:** The area indicator is false on
  every row of this instance, tempting an implementation to drop the branch. The
  predicate is part of the contract and must hold for all relations.
- **Duplicating rows that satisfy both disjuncts:** Implementing the disjunction
  as a multiset union of two branch selections inflates the answer.
- **Treating `gdp` as a tie-breaker or a criterion:** `gdp` is not mentioned in
  the definition of a big country; ranking or filtering by it changes the answer.
- **Sorting the output:** The contract permits any order, so an ordering stage
  adds cost without adding correctness.

---

## 7. Complexity Derivation

Let $N = \lvert \texttt{World} \rvert$ be the number of rows and let $K$ be the
number of rows satisfying $B$, so $0 \le K \le N$.

**Selection.** The predicate evaluates two comparisons and one disjunction per
row, each in constant time. Each row is visited exactly once, so the scan is
linear:

$$
T_{\text{select}}(N) = \Theta(N).
$$

The predicate is not a range search on a single attribute, so the plan cannot
prune the relation by an index on `area` alone or on `population` alone: a
disjunction over two independently indexed attributes is not answerable by one
range scan. Hence $\Theta(N)$ is the realised cost, not merely an upper bound. An
index union plan changes the shape of the cost without changing its growth in the
worst case:

$$
T_{\text{select}}^{\text{union}}(N) = \Theta\bigl(\log N + K_A\bigr) +
\Theta\bigl(\log N + K_P\bigr) + \Theta(K),
$$

where $K_A$ and $K_P$ are the per-branch candidate counts. That is attractive only
when both indexes exist and the branches are genuinely selective.

**Projection.** Each surviving row is mapped to three attributes, so the
projection costs

$$
T_{\text{project}}(K) = \Theta(K) \;\subseteq\; \Theta(N).
$$

**Total.**

$$
T(N) \;=\; \Theta(N) + \Theta(K) \;=\; \Theta(N).
$$

On the worked instance $N = 5$ and $K = 2$: five predicate evaluations, two
projected rows. There is no grouping, no join, and no sort on the critical path,
so the method never exceeds linear time.

**Auxiliary space.** The predicate is a function of one row at a time and nothing
is carried between rows: there is no accumulator, no map of seen values, and no
sort buffer. The filter is therefore a streaming pipeline with constant working
state, and the output buffer of $K$ rows is produced space rather than auxiliary
state:

$$
M(N) = \Theta(1).
$$
