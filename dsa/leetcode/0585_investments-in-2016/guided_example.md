# Guided Example: Investments in 2016

We trace one aggregation whose input set is decided by two independent counting
queries over the same relation. The instance is chosen so that the two criteria
pull in opposite directions: three policyholders share a 2015 value, and two of
them sit at the same coordinate, so the qualifying set cannot be obtained by
filtering on a single attribute frequency.

- **Input relation** `Insurance`, keyed by `pid`:

    | `pid` | `tiv_2015` | `tiv_2016` | `lat` | `lon` |
    |:---:|:---:|:---:|:---:|:---:|
    | $1$ | $10$ | $5$ | $10$ | $10$ |
    | $2$ | $20$ | $20$ | $20$ | $20$ |
    | $3$ | $10$ | $30$ | $20$ | $20$ |
    | $4$ | $10$ | $40$ | $40$ | $40$ |

- **Required output** — the summed 2016 investment, to two decimal places:

    | `tiv_2016` |
    |:---:|
    | $45.00$ |

Every required behaviour appears in these four rows: a shared 2015 value
(policies $1$, $3$, $4$), a lone 2015 value (policy $2$), a coordinate collision
(policies $2$ and $3$), and a policy that satisfies both criteria (policies $1$
and $4$).

---

## 1. Instance & Teaching Goal

Report the sum of `tiv_2016` over all policyholders who satisfy **both** of the
following, and round the result to two decimal places:

1. the policyholder's `tiv_2015` value is shared with one or more other
   policyholders; and
2. the policyholder's `(lat, lon)` pair occurs nowhere else in the relation.

The two conditions are of different kinds, and that difference is the lesson.
Condition 1 is a statement about *how many rows carry a value*; condition 2 is a
statement about *how many rows carry a pair of values*. Neither is a comparison
against a constant, so neither can be evaluated by inspecting a single row in
isolation. Each row must first be told how its group is populated.

### Two frequency signals, never one

It is tempting to treat "same `tiv_2015` as someone else" and "unique location"
as two filters over one shared notion of frequency. They are not. They partition
the same relation along different keys:

| Partition key | Number of groups | Group sizes on this instance | Signal it supplies |
|:---|:---:|:---|:---|
| `tiv_2015` | $2$ | $10 \mapsto 3$, $20 \mapsto 1$ | whether a 2015 value is shared |
| `(lat, lon)` | $3$ | $(10,10) \mapsto 1$, $(20,20) \mapsto 2$, $(40,40) \mapsto 1$ | whether a location is unique |

A group of size $1$ under the first key is a *disqualification*, while a group of
size $1$ under the second key is a *qualification*. The same numeric group size
means opposite things depending on which partition produced it, so the two
signals must be computed separately and combined per row. Collapsing them into a
single grouping is the central error this instance is built to catch.

---

## 2. The Two Predicates and Their Invariant

Write the group-size signals attached to a row $r$ as

$$
c_1(r) = \bigl\lvert\{\, s \in \texttt{Insurance} : s.\texttt{tiv\_2015} =
r.\texttt{tiv\_2015} \,\}\bigr\rvert, \qquad
c_2(r) = \bigl\lvert\{\, s \in \texttt{Insurance} : s.\texttt{lat} = r.\texttt{lat}
\;\wedge\; s.\texttt{lon} = r.\texttt{lon} \,\}\bigr\rvert .
$$

A row qualifies exactly when

$$
Q(r) \;=\; \bigl(c_1(r) > 1\bigr) \;\wedge\; \bigl(c_2(r) = 1\bigr).
$$

> **Per-row partition invariant.** After the two group sizes are attached to each
> row, $c_1(r)$ and $c_2(r)$ depend only on $r$'s own attribute values and on the
> multiset of values in the relation. Attaching them therefore preserves the row
> multiplicity of the relation: every policy keeps exactly one tuple, and the
> predicate $Q$ can be evaluated on each row independently.

This invariant is what makes the aggregation safe. Because the grouping is a
*windowing* operation — it computes a value per row rather than collapsing rows
into one row per group — the relation is not reduced, and the subsequent sum sees
each qualifying policy once. If instead the analysis had used an ordinary
grouping, the four policies would collapse into two rows and the identity of the
coordinate collision would be lost.

Why must the location test use the **pair**? Uniqueness of a coordinate is a
property of the two-dimensional point, not of either ordinate. Two policyholders
may share a latitude and still be in different cities. A predicate that tests
`lat` alone, or that tests the two ordinates disjunctively, measures the wrong
relation:

| Candidate location test | Policies $1$ and $4$ | Policies $2$ and $3$ | Correct criterion? |
|:---|:---:|:---:|:---|
| Pair equality on `(lat, lon)` | distinct, both unique | equal, both colliding | Yes |
| Equality on `lat` alone | distinct | equal | Coincidence only — a shared latitude is not a shared city |
| Equality on `lon` alone | distinct | equal | Same defect |
| "either ordinate differs" | distinct | considered distinct, so the collision is missed | No — the collision would go undetected |

### Relational formulation

The pipeline for this instance has three stages. First, for every row of
`Insurance`, compute two independent partition counters: one over the partition
keyed by the 2015 investment value, and one over the partition keyed by the
coordinate pair. Both are window-style aggregates that annotate rows in place
rather than reducing the relation. Second, retain the rows whose first counter
exceeds one while their second counter equals one. Third, sum the 2016
investment of the retained rows and round the total to two decimal places. Which
window framing and which rounding call express these stages belongs to the
Reference workflow; the three stages themselves are the lesson.

A useful hybrid view of the first stage is a frequency table: build a map from
each key to its multiplicity, then read each row's two multiplicities out of the
maps. That is the same computation stated with auxiliary maps instead of window
annotations.

---

## 3. Step-by-Step Worked Execution

### Step 1 — Build the two frequency tables

| Key | Multiplicity | Policies carrying it |
|:---:|:---:|:---|
| `tiv_2015 = 10` | $3$ | $1, 3, 4$ |
| `tiv_2015 = 20` | $1$ | $2$ |
| `(lat, lon) = (10, 10)` | $1$ | $1$ |
| `(lat, lon) = (20, 20)` | $2$ | $2, 3$ |
| `(lat, lon) = (40, 40)` | $1$ | $4$ |

### Step 2 — Attach both signals to every policy

| `pid` | `tiv_2015` | `(lat, lon)` | $c_1$ | $c_2$ | $c_1 > 1$ | $c_2 = 1$ | $Q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $10$ | $(10, 10)$ | $3$ | $1$ | $\mathit{True}$ | $\mathit{True}$ | Qualifies |
| $2$ | $20$ | $(20, 20)$ | $1$ | $2$ | $\mathit{False}$ | $\mathit{False}$ | Fails both |
| $3$ | $10$ | $(20, 20)$ | $3$ | $2$ | $\mathit{True}$ | $\mathit{False}$ | Fails the location test |
| $4$ | $10$ | $(40, 40)$ | $3$ | $1$ | $\mathit{True}$ | $\mathit{True}$ | Qualifies |

Two of the four policies qualify. The table shows why neither criterion can be
dropped: policy $2$ is killed by the value test, policy $3$ by the location test.

### Step 3 — Accumulate the qualifying 2016 investment

| `pid` | Qualifies? | Contribution to the sum |
|:---:|:---:|:---:|
| $1$ | Yes | $5$ |
| $2$ | No | — |
| $3$ | No | — |
| $4$ | Yes | $40$ |

$$
\sum_{r \,:\, Q(r)} r.\texttt{tiv\_2016} \;=\; 5 + 40 \;=\; 45.
$$

### Step 4 — Round to two decimal places

The required presentation carries exactly two fractional digits, so the exact
integer total is rendered with a zero-padded fractional part:

$$
\text{round}(45, 2) \;=\; 45.00 .
$$

---

## 4. Why the Reasoning Is Correct

**The two counters are exact.** The partition keyed by the 2015 value places two
rows in the same group precisely when their `tiv_2015` values are equal, because
grouping compares the attribute by equality. Hence the group size seen by a row
is exactly the number of rows whose 2015 value equals that row's, which is
$c_1(r)$ by definition. The same argument with the coordinate pair as the key
establishes $c_2(r)$. Neither counter depends on scan order, and neither is
affected by how many other attributes the rows carry.

**The predicate selects exactly the required rows.** By the per-row partition
invariant, $Q$ is a function of the counters alone, and the counters encode
exactly the two conditions in the contract. The contract requires both
conditions, so the conjunction is the correct combination; a disjunction would
admit policy $2$ or policy $3$, both of which the contract rejects.

**The complement is correctly excluded.** Policy $3$ shares its coordinate with
policy $2$. The location criterion is a property of the coordinate, not of the
policy, so it disqualifies *every* policy at that coordinate at once. No rule
privileges the first arrival at a location, and the answer must not depend on
scan order. This is why the criterion is $c_2(r) = 1$ rather than "the first row
seen at this coordinate".

**The sum is over the qualifying set alone, and each row contributes once.**
Because the windowed counters do not collapse rows, the surviving relation has
one tuple per qualifying policy. Summing its 2016 column therefore adds each
qualifying policy's investment exactly once. Note also that the input relation
carries no constraint that distinct policies have distinct 2016 values, so two
qualifying policies may contribute equal amounts; both must still be added. That
is a direct consequence of membership being decided per policy, not per value.

**The projection and rounding are faithful.** The output is a single aggregate
column, so the sum must be computed before the two-decimal presentation is
applied; rounding the individual contributions first would change the total in
general.

| Aggregation mistake | Effect on this instance | Why it is wrong |
|:---|:---|:---|
| Sum evaluated before filtering | $5 + 20 + 30 + 40 = 95$ | The contract sums only the qualifying policies |
| Grouping by `tiv_2016` before filtering | Policies with equal 2016 values merge, destroying per-policy membership | Membership is a property of the policy, not of its investment amount |
| Rounding each contribution separately | Identical here because the contributions are integers | In general it accumulates error, so the rounding must follow the summation |
| Summing the raw rows with duplicates introduced by either count | Depends on the join multiplicity | A frequency-join formulation can multiply rows and inflate the total |

---

## 5. Boundary and Degenerate Cases

| Instance | Qualifying policies | Reported value | Teaching point |
|:---|:---|:---|:---|
| No policy shares its 2015 value | none | the empty sum, which is null rather than $0.00$ | An aggregate over no rows has no value; a null result is a distinct outcome from a zero total |
| Every policy shares a 2015 value, all coordinates distinct | all | the full 2016 sum | The value criterion can be satisfiable by the whole relation |
| Two policies collide at one coordinate and share a 2015 value | neither | their contributions are both excluded | A collision removes *both* members, not just the later one |
| A qualifying policy has `tiv_2016 = 0` | it still qualifies | contributes $0$ but does not change the total | Qualification and contribution are separate questions |
| All policies collide pairwise on coordinates | none | the empty sum | Cliques of size two exclude everyone |
| Two policies share a latitude but not a longitude | both may qualify | both contributions count | The coordinate pair, not either ordinate, defines the collision |
| The total has more than two fractional digits | unchanged membership | rounded to exactly two digits | Rounding is a presentation step applied once, to the total |

The first row is worth dwelling on. A common reflex is to report $0.00$ when
nothing qualifies, but a sum over an empty collection is undefined, so the
correct presentation is a null value rather than a zero. The two answers are not
interchangeable, and a report that cannot distinguish "summed to zero" from
"nothing to sum" has lost information.

---

## 6. Traps This Instance Exposes

- **Filtering on one criterion only:** Keeping just the shared-2015 policies
  admits policy $3$ and returns $75.00$; keeping just the unique-location
  policies admits policy $2$ and returns either $20$ or a differently wrong total
  depending on the combination. Both failures are visible immediately on this
  instance.
- **Testing `lat` or `lon` alone:** The coordinate collision between policies $2$
  and $3$ would be missed, and policy $3$ would be counted.
- **Ordinary grouping instead of windowed counting:** Grouping by `tiv_2015`
  collapses three policies into one row, so the location criterion has nothing
  left to test and the per-policy distinction is destroyed.
- **Using `NOT IN` or a negated subquery for the location test over a nullable
  column:** `lat` and `lon` are declared non-null here, but a negated membership
  test against any set containing a null is unsound in general; a count-based
  test has no such failure mode.
- **Assuming the largest 2015 group is the answer:** Group size is a filter
  threshold, not a ranking. A relation may contain several shared 2015 values,
  and every qualifying policy from every such group contributes.
- **Damaging duplicates with joins:** A self-join on equal 2015 values emits
  cross-products rather than group members, so a naive formulation counts some
  policies several times. Counting is the safer primitive.
- **Rounding too early:** Applying the two-decimal rounding to intermediate
  values rather than to the final total changes the answer on inputs with longer
  fractional parts.
- **Projecting the intermediate counters:** The response schema is one numeric
  column; the two counters are working state, not output.

---

## 7. Complexity Derivation

Let $N = \lvert \texttt{Insurance} \rvert$.

**Group-size computation.** Each partition counter groups the relation on a key
and then reads a group size back onto every row. With hashing, building the
frequency structures costs expected $\Theta(N)$ for each key, so the two signals
together cost expected $\Theta(N)$:

$$
T_{\text{counts}}(N) = \Theta(N) \quad \text{(expected, hash-based)} .
$$

If the engine chooses a sorting plan instead of hashing, each grouping requires
an ordering of its key and the cost becomes $\Theta(N \log N)$. Sorting is the
standard route for window partitioning, so the conservative bound often quoted
for this problem is the sorting one; the hash plan above is what a map-based
implementation actually achieves.

**Filtering and summing.** One pass over the annotated rows evaluates $Q$ and
adds the qualifying contributions, so the aggregation is

$$
T_{\text{sum}}(N) = \Theta(N).
$$

**Total.** The pipeline is a constant number of linear-time passes, so

$$
T(N) \;=\; \Theta(N) \quad \text{(expected, hash-based)}, \qquad
T(N) \;=\; \Theta(N \log N) \quad \text{(sort-based)} .
$$

Neither pass nests inside the other, so there is no quadratic blow-up: a
formulation that joins the relation to itself on equal 2015 values would instead
inspect cross-products and reach $\Theta(N^2)$ on relations with large shared
groups.

**Auxiliary space.** The two frequency structures hold one entry per distinct
2015 value and one entry per distinct coordinate, which is at most $N$ entries
each, and the annotated relation holds one counter pair per row. Caching both
counters is what turns the two criteria into two independent linear passes, at
the price of linear working memory:

$$
M(N) = \Theta(N) .
$$

A streaming variant that recomputes one counter by rescanning would reduce the
working set to the size of a single frequency structure, still $\Theta(N)$ in the
worst case, while multiplying the time by a constant number of passes.
