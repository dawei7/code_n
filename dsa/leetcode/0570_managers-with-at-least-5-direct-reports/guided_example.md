# Guided Example: Managers with at Least 5 Direct Reports

## 1. The Direct-Report Counting Task and Its Instance

A single `Employee` relation stores the whole organization. Each row carries a unique
integer `id` as primary key, a `name`, a `department`, and a `managerId` that points
back at the `id` of another row in the same relation. The reference is optional: when
`managerId` is null the employee has no manager, and the contract also guarantees
that nobody manages themselves.

Because managers and their reports live in the same relation, a manager is simply an
employee whose `id` happens to appear in some other row's `managerId`. The task asks
for the `name` of every manager with **at least five direct reports**, that is, at
least five rows whose `managerId` equals that manager's `id`.

| `id` | `name` | `department` | `managerId` |
|:---:|:---|:---:|:---:|
| 101 | `John` | `A` | null |
| 102 | `Dan` | `A` | 101 |
| 103 | `James` | `A` | 101 |
| 104 | `Amy` | `A` | 101 |
| 105 | `Anne` | `A` | 101 |
| 106 | `Ron` | `B` | 101 |

Rows 102 through 106 all name 101 as their manager, so the manager identifier 101
heads a group of five reports and meets the threshold exactly. Row 101 itself names
no manager, so it belongs to no manager's report group. The required output is the
one-column relation containing the single name `John`.

| `name` |
|:---:|
| `John` |

Note how narrow the margin is: this instance sits exactly on the threshold, so an
off-by-one comparison in either direction would change the answer. Replacing "at
least five" with "more than five" would empty the result, and replacing it with
"more than four" would produce the same answer here while differing on other inputs.

## 2. The Manager-Report Relation and the Role Invariant

The self-reference induces a bipartite reading of one relation. A row plays the role
of a **report** when it is read through its own `managerId`, and the role of a
**manager** when it is read through the `id` values that other rows point at. The
same physical row may play both roles in different parts of the same computation:
whether employee 101 is a manager depends on how many rows name 101, not on anything
stored in row 101 itself.

Define the direct-report set of an identifier $m$ as

$$R(m) = \{\, e \in \texttt{Employee} \;\mid\; e.\text{managerId} = m \,\},$$

and let $\lvert R(m) \rvert$ be its cardinality. The qualifying manager identifiers
are then

$$Q = \{\, m \;\mid\; \lvert R(m) \rvert \ge 5 \,\},$$

and the answer is the projection onto `name` of the rows whose `id` lies in $Q$.

> **Role invariant.** $\lvert R(m) \rvert$ counts exactly the rows that name $m$ as
> their immediate manager. It never counts reports of reports, and it never counts
> the row whose own `id` is $m$, because that row's `managerId` is a different value.

Three structural facts follow from the definitions and drive the whole method.

**Grouping by the manager identifier is the natural partition.** Every row with a
non-null `managerId` belongs to exactly one group, namely the group of the manager it
names. So the groups are disjoint and their sizes are exactly the report counts.

**The threshold is a property of a group, not of a row.** A row-level test cannot
decide whether a manager qualifies, because the deciding quantity is the size of the
whole group. The count must therefore be formed first and the threshold applied to
the formed groups.

**Grouping produces keys, not names.** The grouping key is the manager identifier.
A report row records only that identifier, never the manager's name, so the name must
be recovered in a later step by matching the qualifying identifiers against the
primary key of the same relation.

## 3. Worked Trace: Grouping Direct Reports by Manager Identifier

Partition the rows by their `managerId` value.

| Group key `managerId` | Rows in the group (`id`) | Reports in the group | $\lvert R(m) \rvert$ | Threshold test | Group survives? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 101 | 102, 103, 104, 105, 106 | `Dan`, `James`, `Amy`, `Anne`, `Ron` | 5 | $5 \ge 5$ is true | **yes** |
| null | 101 | `John` | 1 | $1 \ge 5$ is false | no |

Row 101 contributes to the null group, because its `managerId` is unset. That group
has size one and fails the threshold, so it is discarded. It would be discarded in
any case: null is not equal to any employee identifier, so even a null group that
somehow reached the threshold could not be matched to a manager row and could never
produce a name. The null group is therefore harmless but structurally incapable of
contributing output.

The decisive arithmetic for the instance is the group cardinality itself:

$$\lvert R(101) \rvert = \bigl\lvert\{102, 103, 104, 105, 106\}\bigr\rvert = 1 + 1 + 1 + 1 + 1 = 5 .$$

Since $5 \ge 5$, the identifier 101 is retained as a qualifying manager identifier,
and the only other candidate group is eliminated.

| Stage | Content after the stage | Rows |
|:---|:---|:---:|
| Input relation | six employee rows | 6 |
| Grouped by `managerId` | $\{(101, 5), (\text{null}, 1)\}$ | 2 groups |
| Threshold applied | $\{(101, 5)\}$ | 1 group |
| Projected answer | `John` | 1 |

## 4. Resolving Manager Identifiers to Names

A qualifying identifier is not yet a name. The final step matches each retained
identifier against the primary key `id` of the relation and projects the `name`
attribute.

| Qualifying `managerId` | Matched `Employee` row | `id` matches? | Projected `name` |
|:---:|:---|:---:|:---|
| 101 | `(101, John, A, null)` | yes, $101 = 101$ | `John` |
| (any identifier with no matching row) | no row exists | no | nothing is projected |

Because `id` is the primary key, a retained identifier matches at most one employee
row, so each qualifying manager contributes exactly one output row and the match
cannot multiply rows. This is also why counting by name instead of by identifier
would be a mistake: names are not declared unique, so grouping on `name` could merge
two genuinely different managers into one group, while grouping on the identifier
keeps distinct entities distinct. Two managers who happen to share a name are still
different managers, and the query may legitimately return that name twice.

The match also supplies an independent guarantee that the identifier is real. A
report whose `managerId` pointed at an identifier absent from the relation would
produce a group that fails to match any row, so the inner match drops it and the
output never contains a phantom manager.

## 5. Why the Reasoning Is Correct

**Soundness.** Suppose a name is returned. Then some identifier $m$ survived the
threshold test and matched exactly one employee row, whose `name` is the projected
value. Survival means $\lvert R(m) \rvert \ge 5$, so at least five rows in the
relation name $m$ as their immediate manager, and the matched row is the manager
those reports point at. The returned name is therefore a manager with at least five
direct reports.

**Completeness.** Suppose an employee $e$ has at least five direct reports. Then
$\lvert R(e.\text{id}) \rvert \ge 5$, so the group keyed by $e.\text{id}$ survives
the threshold test, and since $e$'s own row exists and carries that identifier as its
primary key, the match finds it and projects $e.\text{name}$. Every qualifying
manager is therefore reported.

**Why direct reports are exactly group members.** A row enters the group of $m$ if
and only if its `managerId` equals $m$. Rows further down the hierarchy name a
different manager, so they enter a different group. In a chain where A manages B and
B manages C, C appears in B's group and never in A's group, even though A is above C
in the organization. The count is of immediate subordinates only, which is what the
statement asks for.

**Why a manager with many reports still appears once.** Grouping collapses all
reports of $m$ into a single row keyed by $m$, whatever the count. The subsequent
primary-key match finds one employee row, so the name is projected once regardless of
whether the manager has five reports or five hundred.

**Why non-managers vanish.** An employee whose identifier heads no group, or whose
group fails the threshold, does not appear among the qualifying identifiers, so the
match has no partner for that row and it is dropped from the projection.

## 6. Traps This Instance Exposes

| Trap | What the instance shows | Why it is wrong |
|:---|:---|:---|
| Applying the count threshold before the rows are grouped | The count $5$ exists only after the five reports of 101 are collected | The deciding quantity is a group aggregate, so a row-level condition cannot express it |
| Using a non-aggregate filter position for the threshold | The threshold tests a value produced by grouping | Aggregate results are not available to a pre-group filter; the test must be applied to the formed groups |
| Using a strict inequality instead of "at least" | The instance's manager has exactly five reports | $5 > 5$ is false, so a strict comparison would wrongly return nothing |
| Counting indirect reports | Group membership follows `managerId` exactly one level | Descendants two or more levels down carry a different `managerId` and belong to another group |
| Grouping by `name` rather than by identifier | Names are not unique | Distinct managers sharing a name would be merged, changing their combined count and possibly qualifying a manager who does not qualify |
| Returning the identifier instead of the name | The answer column is `name` | The grouping key is a numeric identifier; the human-readable name must be recovered by matching it back to the relation |
| Trusting a null group to resolve | Row 101 forms a size-one null group | Null never equals any primary-key value, so no match can occur and no name can be produced |
| Expecting a row per report | Grouping collapses a manager's reports into one group row | The output has one row per qualifying manager, not one per direct report |
| Expecting a fixed row order | The contract permits any order | No ordering step is required, and the engine may return qualifying managers in any sequence |
| Missing `DISTINCT` anxiety for duplicate names | Two different managers may share a name | Grouping by identifier already keeps them separate; suppressing one of them would drop a legitimate answer |

## 7. Complexity Derivation

Let $E$ be the number of rows in `Employee` and $K$ the number of qualifying
managers, so $K \le E$. All identifiers and counts are integers, and no numeric value
is assumed to be contiguous or bounded by the row count.

- **Forming the groups.** Every row with a non-null `managerId` is assigned to
  exactly one group keyed by that identifier. Hash aggregation performs one keyed
  update per row and is expected $O(E)$; sort-based grouping orders the rows by
  manager identifier first and costs $O(E \log E)$. A plan with a B-tree index on
  `managerId` can stream reports in key order and aggregate them without a separate
  sort, which is the practical middle ground.
- **Applying the threshold.** Each group is tested once against the constant
  threshold. The number of groups is at most $E$, so this pass is $O(E)$ and does not
  change the asymptotic class.
- **Resolving names.** Matching each surviving identifier against the primary key
  `id` is one indexed lookup per qualifying manager, costing $O(\log E)$ each, so the
  resolution phase is $O(K \log E)$. Because `id` is a primary key, each lookup
  returns at most one row and the phase cannot expand the output beyond $K$ rows.
- **Total time.** $O(E \log E)$ for a sort-grouping plan, or expected $O(E)$ with
  hash aggregation, matching the conservative representative bound recorded in the
  package manifest. The resolution phase is absorbed because $K \le E$ and
  $\log E$ is sublinear.
- **Auxiliary space.** $O(E)$ in the worst case for grouping state, since every row
  may head its own group when all identifiers are distinct; in the instance only two
  groups exist, so the live grouping state is far smaller. The name-resolution phase
  needs $O(K)$ for the qualifying identifiers, and the emitted relation holds exactly
  $K$ rows. The stored tables and indexes are not counted as working memory.

The structural payoff of the grouping formulation is that the threshold test touches
one row per manager rather than one row per employee, so the expensive comparison is
paid at most $K$ times instead of $E$ times, and no report pair is ever carried
through the final projection.
