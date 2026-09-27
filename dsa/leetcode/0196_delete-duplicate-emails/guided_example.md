# Guided Example: Delete Duplicate Emails

## 1. The Destructive Task and Its Representative Instance

A `Person` relation stores one contact per row. The `id` column is an integer
primary key that uniquely labels a row, and `email` holds a lowercase address
string. A repeated address therefore appears as two distinct rows whose only
distinguishing feature is the identifier. The requested outcome is not a report:
the relation itself must be rewritten so that each distinct address is carried by
exactly one surviving row, namely the row whose `id` is smallest among all rows
that held that address.

| `id` | `email` |
|---|---|
| 1 | `john@example.com` |
| 2 | `bob@example.com` |
| 3 | `john@example.com` |

Two addresses are present. `bob@example.com` occurs once, in the row labelled 2,
so that row already satisfies the requirement and is left untouched. The address
`john@example.com` occurs twice, in rows 1 and 3. The smaller label is $1$, so row
1 is the survivor and row 3 must disappear. The required post-state is therefore:

| `id` | `email` |
|---|---|
| 1 | `john@example.com` |
| 2 | `bob@example.com` |

The judge compares the final relation as an unordered set of rows, so no ordering
work is required; only membership matters.

## 2. The Per-Address Equivalence-Class Invariant

Partition the relation by address. For an address $e$, its class is

$$C(e) = \{\, r \in \texttt{Person} \;\mid\; r.\text{email} = e \,\}.$$

Equality of addresses is an equivalence relation, so the classes are non-empty,
pairwise disjoint, and together cover every row. Within a class the identifier
supplies a total order, so each class has a unique least element:

$$m(e) = \min \{\, r.\text{id} \;\mid\; r \in C(e) \,\}.$$

The relation the task demands is precisely

$$\{\, r \in \texttt{Person} \;\mid\; r.\text{id} = m(r.\text{email}) \,\}.$$

> **Invariant.** A row $r$ survives the rewrite if and only if no other row $s$
> satisfies $s.\text{email} = r.\text{email}$ and $s.\text{id} < r.\text{id}$.
> Equivalently, $r$ is removed exactly when it is a non-minimal member of its own
> address class.

Because the classes are disjoint, the decision about one row never depends on a
row of a different class, and no row can be claimed as the representative of two
addresses. This is what makes a single grouping-level pass sufficient.

| Address $e$ | Class $C(e)$ by `id` | Least element $m(e)$ | Members removed |
|---|---|---|---|
| `john@example.com` | $1, 3$ | $1$ | $3$ |
| `bob@example.com` | $2$ | $2$ | none |

## 3. Worked Trace of the Comparison

Only rows sharing an address can ever compete. The relation below groups the rows
of the instance by address and shows the comparison that decides each membership.

| Candidate row $r$ | Peers sharing `r.email` | Witness $s$ with $s.\text{id} < r.\text{id}$ | Verdict on $r$ |
|:---:|:---:|:---|:---|
| 1 (`john@example.com`) | 1, 3 | none: the only peer is 3, and $3 < 1$ is false | survives |
| 2 (`bob@example.com`) | 2 | none: the only peer is the row itself | survives |
| 3 (`john@example.com`) | 1, 3 | 1, because $1 < 3$ is true | removed |

Expanding the same reasoning into ordered same-address pairs makes the direction
of the comparison explicit. Writing $r$ for the row under test and $s$ for the
potential witness:

| $r.\text{id}$ | $s.\text{id}$ | Shared address? | $s.\text{id} < r.\text{id}$ | Effect |
|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | yes | $1 < 1$ is false | self-comparison, no removal |
| 1 | 3 | yes | $3 < 1$ is false | row 1 is not beaten by row 3 |
| 2 | 2 | yes | $2 < 2$ is false | self-comparison, no removal |
| 3 | 1 | yes | $1 < 3$ is true | row 3 is beaten by row 1 and is removed |
| 3 | 3 | yes | $3 < 3$ is false | self-comparison, no removal |

Row 1 is the only member of its class that survives, and it does so because every
same-address row that could beat it has an identifier that is not smaller. Row 3 is
the only row in the relation for which a strictly smaller same-address witness
exists, so it is the only deletion.

## 4. Row-by-Row Evaluation and the Final Relation

| Step | Action | Relation state (as a set) | Rows |
|:---:|:---|:---|:---:|
| 0 | Initial relation | $\{(1,\text{john}), (2,\text{bob}), (3,\text{john})\}$ | 3 |
| 1 | Group by `email`; mark the least `id` of each group | $\{1 \to \text{john}, \; 2 \to \text{bob}\}$ | 3 |
| 2 | Keep rows whose `id` equals their group minimum | $\{(1,\text{john}), (2,\text{bob})\}$ | 2 |
| 3 | Remove every remaining non-minimal row | row 3 deleted | 2 |

The resulting relation is exactly the required post-state:

| `id` | `email` | Why this row survives |
|:---:|:---|:---|
| 1 | `john@example.com` | It is the least identifier in the class $\{1,3\}$ |
| 2 | `bob@example.com` | It is the only member of its class, hence trivially least |

Note that the survivor's address text is not modified and its identifier is not
renumbered. The rewrite deletes rows; it never rewrites keys. Renumbering would be
both unnecessary and harmful, because the task fixes the surviving identifiers to
the original smallest values.

## 5. Why the Reasoning Is Correct

**Soundness.** Suppose the rewrite keeps a row $r$. Then $r.\text{id} = m(r.\text{email})$,
so $r$ is the least identifier in its own class. No row $s$ in that class can then
satisfy $s.\text{id} < r.\text{id}$, and rows outside the class share no address and
are irrelevant. Hence every decision to keep a row is justified, and no duplicate
address can survive: if two kept rows had the same address they would both be the
unique minimum of that class, which is impossible.

**Completeness.** Suppose a row $r$ satisfies the invariant, that is, no same-address
row has a strictly smaller identifier. Then $r$ must itself be that class's minimum,
so the rule keeps it. Applied to the least element of every class, this guarantees
that each distinct address appears at least once in the final relation, and the
soundness argument guarantees it appears at most once. Exactness follows.

**Termination and idempotence.** The rewrite removes only rows that are provably
non-representatives, so re-running it on the result changes nothing: in the result
relation every class has exactly one member and that member is trivially its own
minimum. A destructive statement with this property is safe to apply even when the
caller is unsure whether duplicates were already cleaned.

## 6. Traps This Instance Exposes

| Trap | Why it fails | Correct reasoning |
|:---|:---|:---|
| Returning a projection instead of mutating the relation | The task requires the stored relation to change; a read-only report leaves the duplicates in place and fails validation | The final state of `Person`, not a result set, is what is graded |
| Reversing the comparison direction | Keeping the largest identifier instead of the smallest keeps row 3 and deletes row 1, the opposite of the requirement | The survivor is the class minimum, so the row to remove is the one with a strictly smaller same-address neighbour |
| Reading the relation while modifying it in the same un-materialized expression | Some engines refuse to base a modification on a subquery over the very table being modified and raise a target-table error | The set of identifiers to keep must be established first — logically as a separate derived relation or materialized temporary relation — and only then applied to the deletion |
| Removing all copies of a duplicated address | The requirement keeps one representative per address; deleting every copy would lose `john@example.com` entirely | Exactly one row per equivalence class survives |
| Assuming identifiers are contiguous or ordered by address | Identifiers are unique labels only; the instance's duplicate pair straddles a different address | Grouping must be driven by the address value, never by arithmetic on `id` |

## 7. Complexity Derivation

Let $N$ be the number of rows in `Person` and $U$ the number of distinct addresses,
so $1 \le U \le N$.

- **Grouping.** Detecting which rows share an address requires collecting the rows
  of each class. Hash grouping visits every row once and updates one bucket per
  row, giving expected $O(N)$ work; sort-based grouping costs $O(N \log N)$ and
  uses $O(N)$ spooled runs. Within each class the minimum identifier is maintained
  with a single comparison per row, which adds only $\Theta(N)$ total.
- **Applying the deletions.** Each surviving and each removed row is inspected
  once. With an index on the primary key `id`, removing a row costs $O(\log N)$,
  so the deletion pass is $O(N \log N)$ in the worst case; when the engine can
  drive deletions directly from the grouped relation, the pass is $O(N)$.
- **Total time.** $O(N)$ expected with hash grouping, and $O(N \log N)$ for a
  sort-grouping plan. Both are linear up to the logarithmic factor, so the method
  scales comfortably to the largest admissible relation.
- **Auxiliary space.** $O(U)$ to hold the per-address representative identifiers,
  which is $O(N)$ in the worst case when every address is distinct. The raw row
  data is mutated in place, so no second copy of the relation is required.

The decisive structural fact is that the algorithm never compares rows across
different address classes. That restriction, not any particular execution
strategy, is what turns a quadratic all-pairs comparison into a single grouped
pass.