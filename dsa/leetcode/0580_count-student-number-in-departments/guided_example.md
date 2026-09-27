# Guided Example: Count Student Number in Departments

We trace one census report through the complete relational pipeline: anchoring a
left outer join on the master `Department` relation, counting a null-capable
attribute instead of counting rows, normalizing empty departments to a true zero,
and applying the two-key ordering `student_number DESC, dept_name ASC`.

- **Input relations:**
  - `Department`, keyed by `dept_id`:

    | `dept_id` | `dept_name` |
    |:---:|:---:|
    | $1$ | `Engineering` |
    | $2$ | `Science` |
    | $3$ | `Law` |

  - `Student`, keyed by `student_id`, with `dept_id` referencing `Department`:

    | `student_id` | `student_name` | `gender` | `dept_id` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `Jack` | `M` | $1$ |
    | $2$ | `Jane` | `F` | $1$ |
    | $3$ | `Mark` | `M` | $2$ |

- **Required output** — every department with its enrolled-student count:

    | `dept_name` | `student_number` |
    |:---:|:---:|
    | `Engineering` | $2$ |
    | `Science` | $1$ |
    | `Law` | $0$ |

The single decisive idea in this instance is that `Law` has no students at all.
An inner join would erase it; a row count would resurrect it as a phantom $1$.
Only the pairing of an outer join with a null-discriminating count yields the
required $0$.

---

## 1. Instance & Teaching Goal

Report, for **every** row of `Department`, the department name together with the
number of students whose `dept_id` points at it. A department with no current
students must still appear, reporting `0`. Sort the result by
`student_number` in descending order; break ties alphabetically by `dept_name`
in ascending order.

The test instance contains three departments and three students, so the three
populations $0$, $1$, and $2$ are all witnessed at once. That makes it a
compact laboratory for two independent traps: **entity loss** (a department
disappearing because no student matches it) and **phantom counting** (an empty
department reporting a spurious $1$).

Write $D = \lvert \texttt{Department} \rvert = 3$ and
$S = \lvert \texttt{Student} \rvert = 3$. The correct answer is a relation with
exactly $D$ rows, not $S$ rows and not the number of matching pairs.

### Why a row count is not a student count

The two traps interact. An empty department survives the join only because the
join synthesizes a placeholder row; but that same placeholder row makes the
group non-empty, so a naive row count reports $1$ where the truth is $0$. The
placeholder is a *structural* artefact of the outer join, not a student.

---

## 2. The Counting Invariant

The solution rests on a single invariant that must hold at every stage.

> **Departure-balance invariant.** After the left outer join, the intermediate
> relation contains exactly one tuple for every student, plus exactly one
> null-padded tuple for every department that has no student. Consequently the
> count of **non-null** `student_id` values inside a department's group equals
> the number of real students in that department.

Two consequences follow immediately, and both are needed.

1. **Entity preservation.** Because the join is anchored on `Department`, each
   department contributes at least one tuple to the intermediate relation. No
   department can be dropped downstream, so no department can vanish from the
   report.
2. **Null discrimination.** Because the count is taken over a column of the
   *nullable* relation (`Student`), the synthesized placeholder contributes
   nothing. The empty department's group is present but scores zero.

### Row counting versus value counting

Aggregate counters disagree precisely on placeholder groups:

| Aggregate | What it enumerates | Value for `Engineering` | Value for `Science` | Value for `Law` | Correct for this problem? |
|:---|:---|:---:|:---:|:---:|:---|
| Row count | Tuples in the group, placeholder included | $2$ | $1$ | $1$ | No — inflates empty departments |
| Non-null value count over `student_id` | Real student identifiers in the group | $2$ | $1$ | $0$ | Yes — placeholder is skipped |
| Non-null value count over `dept_id` | Department identifiers, which the placeholder also carries | $2$ | $1$ | $1$ | No — the placeholder still carries `dept_id` from the left relation |

The third row of that table is the sharpest lesson: the placeholder supplies
concrete values for all `Department` columns and `NULL` for all `Student`
columns. Any counter that reads a left-side attribute therefore cannot
distinguish a real enrollment from a synthesized row; only a counter that reads
a right-side attribute can.

### Relational formulation

The whole pipeline is a composition of three relational operations. It begins
with a join on the shared attribute `dept_id` whose *retention rule* keeps
left-side tuples that find no partner, extending them with `NULL` for every
attribute contributed by the right relation. It continues with a grouping of the
joined relation on the department key and an aggregation that counts non-null
values of the student identifier. It ends with a projection onto `dept_name`
together with the aggregate, ordered by the aggregate descending and then by
`dept_name` ascending. Naming the operations is the lesson; their concrete
spelling belongs to the Reference workflow.

Why group on the key rather than the name? Grouping on `dept_id` respects the
primary key, so two distinct departments that happen to share a `dept_name`
still receive separate, individually correct counts. Grouping on the name alone
would fuse them into one inflated row.

---

## 3. Step-by-Step Worked Execution

### Step 1 — Anchor the join on `Department`

Each department tuple is paired with every student tuple whose `dept_id` agrees
with it. Where no partner exists, the department tuple is retained and every
`Student` attribute is set to `NULL`.

| Left tuple | `dept_id` | Matching `Student` tuples | Joined tuple |
|:---|:---:|:---|:---|
| `(1, Engineering)` | $1$ | `(1, Jack, M, 1)`, `(2, Jane, F, 1)` | `(1, Engineering, 1, Jack, M, 1)` and `(1, Engineering, 2, Jane, F, 1)` |
| `(2, Science)` | $2$ | `(3, Mark, M, 2)` | `(2, Science, 3, Mark, M, 2)` |
| `(3, Law)` | $3$ | none | `(3, Law, NULL, NULL, NULL, NULL)` |

Four intermediate tuples result from three students and three departments: the
three students each produced exactly one pair, and `Law` contributed one
null-padded tuple. This is precisely the departure balance the invariant
predicts, and it is why $\lvert \text{joined} \rvert = S + (\text{empty
departments}) = 3 + 1 = 4$.

### Step 2 — Group and count non-null student identifiers

Partition the intermediate relation by `dept_id` and count the non-null values of
`student_id` inside each group.

| Group key `dept_id` | `dept_name` | `student_id` values in the group | Non-null values | Count |
|:---:|:---:|:---|:---:|:---:|
| $1$ | `Engineering` | $1, 2$ | $1, 2$ | $2$ |
| $2$ | `Science` | $3$ | $3$ | $1$ |
| $3$ | `Law` | `NULL` | none | $0$ |

The `Law` group is not empty — it holds one tuple — yet its count is zero,
because the only candidate value in the counted column is `NULL`. That is the
whole point of the invariant.

### Step 3 — Order by count descending, then name ascending

| Rank | `dept_name` | `student_number` | Deciding comparison |
|:---:|:---:|:---:|:---|
| $1$ | `Engineering` | $2$ | Largest count, so first |
| $2$ | `Science` | $1$ | $1 < 2$, so after `Engineering` |
| $3$ | `Law` | $0$ | Smallest count, so last |

Every count here is distinct, so the secondary key never fires. It still has to
be present in the contract, because a table may contain several equally sized
departments.

### Step 4 — Emit the projection

| `dept_name` | `student_number` |
|:---:|:---:|
| `Engineering` | $2$ |
| `Science` | $1$ |
| `Law` | $0$ |

---

## 4. Why the Reasoning Is Correct

**Every department is reported exactly once.** The outer join retains all $D$
left tuples, and grouping partitions those tuples disjointly on the department
key. Each department therefore owns exactly one group and yields exactly one
output row, so the result cardinality is exactly $D$.

**Every reported count is the true enrollment.** For a department with at least
one student, its group consists of one correctly paired tuple per enrolled
student; the paired `student_id` values are all non-null (the attribute is the
primary key of `Student`), so the non-null count is the enrollment size. For a
department with no student, its group consists solely of the null-padded tuple;
the non-null count over `student_id` is therefore $0$, which is the enrollment
size. The two cases cover all possibilities, so the aggregate is exact on every
group.

**The ordering is total and deterministic.** The count is the primary key of the
sort; among equal counts, `dept_name` is compared lexicographically in ascending
order. Any two rows of the answer are therefore distinguished by at least one
key, so the emitted order is well defined. Because `dept_name` is the only
attribute in the output besides the count, a tie on both keys would mean two
identical output rows, which the projection is entitled to produce.

---

## 5. Boundary and Degenerate Cases

| Instance | Intermediate relation | Reported counts | Teaching point |
|:---|:---|:---|:---|
| `Student` entirely empty | One null-padded tuple per department | All $0$ | The join alone supplies every report row; the count supplies every zero |
| One department, many students | One tuple per student | That department's enrollment | Aggregation degenerates to a single group and the sort is vacuous |
| Two departments share a name but differ in `dept_id` | Both groups present separately | Two separate rows, possibly identical text | Identity comes from the key, not from the comparable label |
| One department with exactly one student | One real tuple plus no placeholder | $1$ | Indistinguishable at the count level from a wrongly counted empty department; the invariant is what distinguishes them |
| Identifiers not contiguous, e.g. `5`, `42`, `100` | Unchanged grouping behaviour | Correct per key | Nothing may assume densely packed or consecutive keys |

The fourth row deserves emphasis. On an instance where a wrong method happens to
be right, the only defence is the argument, not the data. This is why the
invariant is stated as a property of the intermediate relation rather than as an
observation about the sample.

---

## 6. Traps This Instance Exposes

- **Inner join instead of left outer join:** `Law` has no student, so the join
  predicate never fires for `dept_id = 3`. An inner join returns two rows and
  silently omits a department that the contract requires.
- **Counting rows instead of non-null student identifiers:** The placeholder row
  that preserved `Law` also makes its group size $1$. Reporting $1$ for `Law` is
  the classic phantom count.
- **Counting a left-side attribute:** The placeholder carries a genuine
  `dept_id` and `dept_name`. Counting `dept_id` inside the group also yields $1$
  for `Law`, so the null-discrimination trick only works on the nullable side.
- **Filtering the placeholder away before aggregating:** A predicate such as
  "keep only tuples whose `student_id` is not null" removes the placeholder and
  reverts the query to an inner join, deleting `Law`.
- **Grouping by name only:** Two departments with the same `dept_name` collapse
  into a single row and their enrollments are summed, violating the one-row-per-
  department requirement.
- **Omitting the tie-breaker:** With several equal counts the contract still
  demands alphabetical order; a single ascending-or-descending count sort leaves
  the output order unspecified.
- **Returning the raw group size instead of projecting the required columns:**
  Surrogate keys such as `dept_id` are not part of the requested schema.

---

## 7. Complexity Derivation

Let $D = \lvert \texttt{Department} \rvert$ and
$S = \lvert \texttt{Student} \rvert$.

**Join.** A hash join on `dept_id` builds a hash table over the smaller input and
probes it once per tuple of the other input, giving expected $\Theta(D + S)$
work. The intermediate relation it emits has $\Theta(S + e)$ tuples, where $e$
is the number of empty departments and $e \le D$; in the worst case this is
$\Theta(D + S)$.

**Aggregation.** Grouping the intermediate relation and evaluating the non-null
count visits each joined tuple once and touches each of the $D$ groups once:
$\Theta(D + S)$.

**Ordering.** A comparison sort over the $D$ aggregated rows costs
$\Theta(D \log D)$ in the worst case. A top-$k$ style plan cannot help here,
because the contract demands the complete ordering of all departments.

$$
T(D, S) \;=\; \underbrace{\Theta(D + S)}_{\text{join}} \;+\;
\underbrace{\Theta(D + S)}_{\text{group and count}} \;+\;
\underbrace{\Theta(D \log D)}_{\text{order}}
\;=\; \Theta\bigl(D \log D + S\bigr).
$$

On the worked instance, $D = S = 3$: the join touches six tuples, the aggregation
touches four joined tuples and three groups, and the ordering touches three rows.

**Auxiliary space.** The hash table for the join holds one entry per distinct
`dept_id`, the aggregation holds one accumulator per department, and the ordered
output buffers $D$ rows:

$$
M(D, S) \;=\; \Theta(D).
$$

The output relation itself is $\Theta(D)$ and is not auxiliary, but the
accumulator state and the sort buffer are, so the bound stands. If the engine
chooses a sort-merge join instead of a hash join, the leading term becomes
$\Theta(D \log D + S \log S)$; the achieved plan for this instance is the hash
plan above.
