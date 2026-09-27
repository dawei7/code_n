# Guided Example: Find Customer Referee

We trace one selection predicate through SQL's three-valued logic. The instance
is built so that both ways of lying are present at once: a customer whose
`referee_id` is exactly $2$ must be rejected, and a customer whose `referee_id`
is `NULL` must be accepted even though no comparison against `NULL` is ever true.

- **Input relation** `Customer`, keyed by `id`:

    | `id` | `name` | `referee_id` |
    |:---:|:---:|:---:|
    | $1$ | `Will` | `null` |
    | $2$ | `Jane` | `null` |
    | $3$ | `Alex` | $2$ |
    | $4$ | `Bill` | `null` |
    | $5$ | `Zack` | $1$ |
    | $6$ | `Mark` | $2$ |

- **Required output** — the names of customers not referred by customer $2$:

    | `name` |
    |:---:|
    | `Will` |
    | `Jane` |
    | `Bill` |
    | `Zack` |

The relation is deliberately chosen over a smaller two-row instance because it
separates three distinct populations: three customers with no referee at all,
two customers referred by the forbidden identifier $2$, and one customer referred
by a different identifier $1$. A predicate that handles only the first two
populations cannot pass this instance.

---

## 1. Instance & Teaching Goal

Report the `name` of every customer who was **not** referred by the customer
whose `id` is $2$. "Not referred by $2$" covers two disjoint situations:

1. the customer has a referee, and that referee's `id` differs from $2$; or
2. the customer has no referee at all, so `referee_id` is `NULL`.

Return the result in any order, and project only the `name` attribute.

The contract is a *disjunction*, and this is exactly where the difficulty lives.
The second branch is not a comparison at all — it is an absence. A predicate
written as a single inequality covers branch 1 only and silently drops branch 2,
which is the trap this instance is designed to expose.

### The nullable column is the whole problem

`referee_id` is a foreign key into the very relation being filtered, and it is
nullable: the description of the relation records that a row indicates the `id`
of the customer who referred them, and referral is optional. Every customer with
`referee_id IS NULL` is a legitimate member of branch 2, so any filter that
cannot express "no value" fails the contract by construction.

---

## 2. Three-Valued Predicate Semantics

SQL evaluates a comparison over a nullable attribute in a logic with three
outcomes rather than two. Write $\mathit{True}$, $\mathit{False}$, and
$\mathit{Unknown}$ for them. A selection keeps a tuple if and only if the
predicate evaluates to $\mathit{True}$; both $\mathit{False}$ and
$\mathit{Unknown}$ discard it.

For any comparison operator $\theta$ and any value $v$, if either operand is
`NULL` then $v \;\theta\; \texttt{NULL}$ evaluates to $\mathit{Unknown}$. The
rule is not an accident of one engine; it is what the standard prescribes, and
it is the reason the naive inequality loses rows.

| Row | `referee_id` | $\texttt{referee\_id} \ne 2$ | Keeps the row? | $\texttt{referee\_id} \text{ IS NULL}$ | Keeps the row? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `Will` | `NULL` | $\mathit{Unknown}$ | No | $\mathit{True}$ | Yes |
| `Jane` | `NULL` | $\mathit{Unknown}$ | No | $\mathit{True}$ | Yes |
| `Alex` | $2$ | $\mathit{False}$ | No | $\mathit{False}$ | No |
| `Bill` | `NULL` | $\mathit{Unknown}$ | No | $\mathit{True}$ | Yes |
| `Zack` | $1$ | $\mathit{True}$ | Yes | $\mathit{False}$ | No |
| `Mark` | $2$ | $\mathit{False}$ | No | $\mathit{False}$ | No |

Neither column of that table is correct alone: the inequality column keeps only
`Zack`, and the nullity column keeps only the three unreferred customers. The
correct predicate is their disjunction, which is $\mathit{True}$ for `Will`,
`Jane`, `Bill`, and `Zack`.

> **Null-guard invariant.** A filter over a nullable attribute is only correct
> if, for every value actually present in the column, the predicate evaluates to
> $\mathit{True}$ exactly when the row belongs to the required set — including
> the `NULL` value, which must be admitted by an explicit null test or by
> substituting an in-domain sentinel before comparing.

### Two admissible ways to guard the null

**Substitute before comparing.** Replace `NULL` with a sentinel drawn from
outside the legitimate domain of the column and then compare. Because `id` is a
primary key of positive integers, $0$ cannot be the identifier of any real
customer, so coalescing `referee_id` to $0$ before the comparison maps the
unknown case to a definite $\mathit{True}$ without ever colliding with a genuine
rejection. The precondition is real: if the sentinel were a value that could
occur, a customer referred by that value would be misclassified.

**Test for null explicitly.** Keep the inequality and add a disjunct that is
true precisely when the attribute is absent. The disjunction
$(x \ne 2) \lor (x \text{ IS NULL})$ evaluates as follows: on a concrete $x$ the
second disjunct is $\mathit{False}$ and the first decides; on `NULL` the first is
$\mathit{Unknown}$ and the second is $\mathit{True}$, and $\mathit{Unknown} \lor
\mathit{True} = \mathit{True}$. This form needs no sentinel and no domain
assumption, which makes it the safer habit.

| Guard strategy | Predicate outcome on `referee_id = 1` | On `referee_id = 2` | On `referee_id = NULL` | Domain assumption required |
|:---|:---:|:---:|:---:|:---|
| Bare inequality | $\mathit{True}$ | $\mathit{False}$ | $\mathit{Unknown}$ — row lost | none, but answer is wrong |
| Sentinel substitution | $\mathit{True}$ | $\mathit{False}$ | $\mathit{True}$ | a sentinel outside the value domain must exist |
| Inequality disjoined with an explicit null test | $\mathit{True}$ | $\mathit{False}$ | $\mathit{True}$ | none |

### Relational formulation

Reaching the answer requires exactly two operations: a horizontal selection on
`Customer` whose predicate is the disjunction described above, followed by a
vertical projection onto the single attribute `name`. The decisive design
choice is how the selection treats the absent-referee case; the concrete spelling
belongs to the Reference workflow.

---

## 3. Step-by-Step Worked Execution

### Step 1 — Scan the relation

| Scan order | Tuple | `id` | `name` | `referee_id` |
|:---:|:---|:---:|:---:|:---:|
| $1$ | $t_1$ | $1$ | `Will` | `NULL` |
| $2$ | $t_2$ | $2$ | `Jane` | `NULL` |
| $3$ | $t_3$ | $3$ | `Alex` | $2$ |
| $4$ | $t_4$ | $4$ | `Bill` | `NULL` |
| $5$ | $t_5$ | $5$ | `Zack` | $1$ |
| $6$ | $t_6$ | $6$ | `Mark` | $2$ |

### Step 2 — Evaluate the guarded predicate tuple by tuple

Using the sentinel-substitution guard with $0$ as the sentinel:

| Tuple | `referee_id` | Substituted value | Comparison against $2$ | Decision |
|:---:|:---:|:---:|:---:|:---|
| $t_1$ | `NULL` | $0$ | $0 \ne 2 \implies \mathit{True}$ | Keep |
| $t_2$ | `NULL` | $0$ | $0 \ne 2 \implies \mathit{True}$ | Keep |
| $t_3$ | $2$ | $2$ | $2 \ne 2 \implies \mathit{False}$ | Drop |
| $t_4$ | `NULL` | $0$ | $0 \ne 2 \implies \mathit{True}$ | Keep |
| $t_5$ | $1$ | $1$ | $1 \ne 2 \implies \mathit{True}$ | Keep |
| $t_6$ | $2$ | $2$ | $2 \ne 2 \implies \mathit{False}$ | Drop |

The same decisions arise from the explicit-null disjunction, which never forms an
`Unknown` at all:

| Tuple | First disjunct $x \ne 2$ | Second disjunct $x$ `IS NULL` | Disjunction | Decision |
|:---:|:---:|:---:|:---:|:---|
| $t_1$ | $\mathit{Unknown}$ | $\mathit{True}$ | $\mathit{True}$ | Keep |
| $t_2$ | $\mathit{Unknown}$ | $\mathit{True}$ | $\mathit{True}$ | Keep |
| $t_3$ | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ | Drop |
| $t_4$ | $\mathit{Unknown}$ | $\mathit{True}$ | $\mathit{True}$ | Keep |
| $t_5$ | $\mathit{True}$ | $\mathit{False}$ | $\mathit{True}$ | Keep |
| $t_6$ | $\mathit{False}$ | $\mathit{False}$ | $\mathit{False}$ | Drop |

### Step 3 — Project the surviving tuples

| Surviving tuple | `id` | Projected `name` |
|:---:|:---:|:---:|
| $t_1$ | $1$ | `Will` |
| $t_2$ | $2$ | `Jane` |
| $t_4$ | $4$ | `Bill` |
| $t_5$ | $5$ | `Zack` |

Four of the six tuples survive. The order of these four rows is unspecified by
the contract, since the projection retains no ordering attribute.

---

## 4. Why the Reasoning Is Correct

**Soundness.** Suppose the predicate is $\mathit{True}$ for a tuple $t$. If
$t$'s `referee_id` is a concrete value, the sentinel is not substituted, so
$\mathit{True}$ means that value differs from $2$ and $t$ belongs to branch 1.
If `referee_id` is `NULL`, the sentinel $0$ is substituted and the comparison
$0 \ne 2$ is $\mathit{True}$ by the choice of $0$; then $t$ has no referee and
belongs to branch 2. In both cases the emitted tuple satisfies the contract, so
nothing spurious is reported.

**Completeness.** Suppose $t$ satisfies the contract. If $t$ has a referee
$r \ne 2$, the predicate reduces to $r \ne 2$, which is $\mathit{True}$. If $t$
has no referee, `referee_id` is `NULL`, a value is substituted, and the result is
$0 \ne 2 = \mathit{True}$. So every qualifying tuple passes, and no qualifying
customer is omitted.

**The projection is faithful.** `name` is copied unchanged from the surviving
tuple, and no other attribute is emitted, so the output schema is exactly the
single required column. Duplicate names are preserved rather than collapsed:
two distinct rows may carry the same `name`, and the selection is row-wise, so
both survive and both appear. This matches the contract, which is stated over
customers and not over distinct names.

---

## 5. Boundary and Degenerate Cases

| Instance | Qualifying tuples | Output | Teaching point |
|:---|:---|:---|:---|
| Every `referee_id` equals $2$ | none | empty relation with header `name` | The filter may legitimately return zero rows; the column header still exists |
| Every `referee_id` is `NULL` | all | every name | The null branch alone can carry the whole answer |
| No `referee_id` equals $2$, all concrete | all | every name | The inequality branch alone can carry the whole answer |
| `Customer` is empty | none | empty relation with header `name` | No row ever reaches the predicate |
| Two customers share a `name` | depending on referees | two identical `name` entries | Selection preserves duplicates; it is not a distinct operation |
| A customer's own `id` equals $2$ | decided only by their `referee_id` | may qualify | The filtered attribute is the referee, never the customer's own key |

The last row is the subtler semantic trap. The label "$2$" in the contract
identifies a *referrer*, so the value $2$ appearing in the `id` column is
irrelevant to a row's own eligibility. A customer who happens to hold `id = 2`
is judged solely by whom they were referred by.

---

## 6. Traps This Instance Exposes

- **The bare inequality:** A predicate that only asserts "differs from $2$"
  discards `Will`, `Jane`, and `Bill`, returning just `Zack` — one row instead of
  four. This is the failure the instance is built to trigger.
- **Negated membership over a nullable column:** A membership test negated with
  `NOT IN` has the same defect in a sharper form. Comparing against a list that
  contains `NULL` makes every negated result $\mathit{Unknown}$, and even a list
  without `NULL` still yields $\mathit{Unknown}$ for a `NULL` attribute, so
  unreferred customers are lost.
- **Reading `Unknown` as `False`:** The intuition "this customer was obviously
  not referred by $2$" is a statement about the world, not about the predicate.
  A filter is governed by evaluation, not by intent.
- **Choosing a colliding sentinel:** Substituting a value that a genuine
  `referee_id` can take converts a keep into a drop. The sentinel must lie
  outside the domain of real identifiers.
- **Reinstating the dropped rows with a union of two separate filters:** This is
  correct but redundant. The disjunctive predicate already expresses both
  branches, and duplicating the two branches risks overlapping them.
- **Widening the selection to fix nulls:** Replacing the inequality with a plain
  null test would keep every unreferred customer *and* every customer referred by
  $2$ except those with `referee_id = 2` — which is the same thing only by
  accident here; the general predicate must test both branches.
- **Projecting extra columns:** The response schema is a single column; carrying
  `id` or `referee_id` through the projection violates it.

---

## 7. Complexity Derivation

Let $N = \lvert \texttt{Customer} \rvert$ be the number of tuples.

**Selection.** The predicate inspects one tuple at a time. Sentinel substitution
and the inequality are each constant-time operations, and the disjunctive form
performs two constant-time tests. Each tuple is tested once, so the selection is
a single linear pass:

$$
T_{\text{select}}(N) = \Theta(N).
$$

No ordering attribute is involved in the predicate, so no index can narrow the
scan to a sublinear range: `referee_id` is not compared against a range or a
sorted key, and the `NULL` branch disqualifies any plan that would prune on the
`referee_id` value alone. The scan is therefore a full relation scan, and
$\Theta(N)$ is not merely an upper bound but the realised cost.

**Projection.** Each surviving tuple contributes one output row and the
projection copies one attribute, so the projection is linear in the number of
survivors $K$, and $K \le N$:

$$
T_{\text{project}}(K) = \Theta(K) \;\subseteq\; \Theta(N).
$$

**Total.**

$$
T(N) \;=\; \Theta(N) + \Theta(K) \;=\; \Theta(N).
$$

On the worked instance $N = 6$ and $K = 4$: six predicate evaluations, four
projected rows.

**Auxiliary space.** The predicate is evaluated on one tuple at a time and
nothing needs to be remembered between tuples: there is no grouping, no join, no
sort, and no deduplication. The filter is therefore a streaming pipeline whose
auxiliary state is constant. The output relation itself may hold up to $N$ rows,
but that is produced space rather than working space:

$$
M(N) = \Theta(1).
$$
