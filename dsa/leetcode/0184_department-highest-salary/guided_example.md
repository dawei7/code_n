# Guided Example: Department Highest Salary

We trace one organization through a partitioned maximum computation and a pair-membership filter, and show why the obvious "one grouped row per department" formulation silently deletes half of the correct answer whenever a department's top salary is shared.

- **Representative relations:** `Employee` = `(1, "Joe", 70000, 1)`, `(2, "Jim", 90000, 1)`, `(3, "Henry", 80000, 2)`, `(4, "Sam", 60000, 2)`, `(5, "Max", 90000, 1)`; `Department` = `(1, "IT")`, `(2, "Sales")`.
- **Required result:** the three rows `("IT", "Jim", 90000)`, `("Sales", "Henry", 80000)`, `("IT", "Max", 90000)`, under the headers `Department`, `Employee`, `Salary`.
- **Decisive feature:** IT has a two-way tie at the top, so any method that returns one arbitrary employee per group is visibly wrong.

## 1. Instance and Required Outcome

`Employee(id, name, salary, departmentId)` holds one row per employee, with `id` as the primary key (a column of unique values) and `departmentId` a foreign key referencing `Department.id`. `Department(id, name)` supplies the textual names, with `id` as its primary key and a guaranteed non-null `name`.

| `Employee.id` | `name` | `salary` | `departmentId` |
|:---:|:---|:---:|:---:|
| 1 | `"Joe"` | 70000 | 1 |
| 2 | `"Jim"` | 90000 | 1 |
| 3 | `"Henry"` | 80000 | 2 |
| 4 | `"Sam"` | 60000 | 2 |
| 5 | `"Max"` | 90000 | 1 |

| `Department.id` | `name` |
|:---:|:---|
| 1 | `"IT"` |
| 2 | `"Sales"` |

Report, for every department that employs anyone, each employee whose salary equals that department's highest salary. This is a *per-group* extremum, not a global one: `90000` answers IT and `80000` answers Sales, even though `60000` and `70000` are unremarkable globally. The output schema is fixed at `Department`, `Employee`, `Salary`, in any row order.

## 2. Partition by Department and the Per-Group Maximum

The `departmentId` attribute induces a partition of the employee rows: two employees share a block when they share a department, every employee lies in exactly one block, and no block is empty. Writing the block of employee $e$ as $B(e) = \{\, e' \in \text{Employee} \mid e'.\text{departmentId} = e.\text{departmentId} \,\}$, the per-department threshold is the extremum

$$
M(e) = \max_{e' \in B(e)} e'.\text{salary}.
$$

A maximum over a finite non-empty multiset of integers always exists, so $M$ is well defined even for a one-person department. The algorithm needs the *pair set* $\mathcal{M}$, holding one ordered pair per distinct `departmentId`:

$$
\mathcal{M} = \{\, (d,\, \max_{e' : e'.\text{departmentId} = d} e'.\text{salary}) \;\mid\; d \text{ occurs in } \text{Employee} \,\}.
$$

Membership in $\mathcal{M}$ is the classifier: an employee belongs to the answer exactly when its own `(departmentId, salary)` pair is in $\mathcal{M}$.

> **Invariant.** An employee row $e$ is emitted if and only if $e.\text{salary} = M(e)$, that is, if and only if the pair $(e.\text{departmentId},\; e.\text{salary})$ occurs in $\mathcal{M}$. The condition is checked per row, so every tied top earner is classified identically.

## 3. Worked Trace of the Threshold Computation

Grouping the employees by `departmentId` and reducing each block to its maximum produces the threshold relation in a single pass.

| Department `id` | Employees in the block | Salary multiset | Block maximum $M$ | Pair in $\mathcal{M}$ |
|:---:|:---|:---|:---:|:---|
| 1 | `Joe`, `Jim`, `Max` | $\{70000, 90000, 90000\}$ | 90000 | `(1, 90000)` |
| 2 | `Henry`, `Sam` | $\{80000, 60000\}$ | 80000 | `(2, 80000)` |

Each block's reduction needs one comparison per additional member, so the whole relation is computed in one linear scan of `Employee`, with one accumulator per distinct department.

| $\mathcal{M}$: `departmentId` | $\mathcal{M}$: maximum salary |
|:---:|:---:|
| 1 | 90000 |
| 2 | 80000 |

## 4. The Tie-Preservation Invariant: Why One Grouped Row Is Not Enough

The tempting shortcut is to group `Employee` by department and select an employee name beside the block maximum. It fails twice on this instance.

It is first *ill-typed as a query*. After grouping, only the grouping keys and aggregates over the block have defined values; a bare employee name is neither, so a strict grouping-mode engine rejects the request rather than guessing which of `Joe`, `Jim`, and `Max` was meant.

It is then incomplete even where tolerated. A grouped row carries one value per group, so with `Jim` and `Max` both at 90000 in IT the shortcut can return at most one of them, and which one is an implementation detail rather than a fact about the data. The required output contains both.

Pair membership avoids this because it never asks a grouped row to carry a non-aggregated identity. The reduction yields only thresholds, which are legitimately aggregate values, and each employee's identity is recovered afterwards by testing that row individually. Ties stop being a special case: `Jim` and `Max` both present the pair `(1, 90000)`, so both pass and no arbitrary choice remains.

## 5. Evaluating the Pair-Membership Test on Every Employee

| `id` | `name` | `departmentId` | `salary` | Candidate pair | In $\mathcal{M}$? | Department | Emitted row |
|:---:|:---|:---:|:---:|:---|:---:|:---|:---|
| 1 | `"Joe"` | 1 | 70000 | `(1, 70000)` | no — behind the 90000 threshold | `"IT"` | — |
| 2 | `"Jim"` | 1 | 90000 | `(1, 90000)` | **yes** | `"IT"` | `("IT", "Jim", 90000)` |
| 3 | `"Henry"` | 2 | 80000 | `(2, 80000)` | **yes** | `"Sales"` | `("Sales", "Henry", 80000)` |
| 4 | `"Sam"` | 2 | 60000 | `(2, 60000)` | no — behind the 80000 threshold | `"Sales"` | — |
| 5 | `"Max"` | 1 | 90000 | `(1, 90000)` | **yes**, the same pair as row 2 | `"IT"` | `("IT", "Max", 90000)` |

The department name is resolved by a keyed lookup on `Department.id = departmentId`. Since `Department.id` is a primary key, that lookup returns exactly one name and adds no multiplicity.

| `Department` | `Employee` | `Salary` |
|:---|:---|:---:|
| `"IT"` | `"Jim"` | 90000 |
| `"IT"` | `"Max"` | 90000 |
| `"Sales"` | `"Henry"` | 80000 |

## 6. Correctness of the Threshold-Then-Membership Method

**Soundness.** Suppose a row is emitted. Its pair lies in $\mathcal{M}$, which contains only pairs of the form (department, maximum over that department), so the row's salary equals the maximum salary of its own department.

**Completeness.** Every employee belongs to a non-empty block, and every block contributes its maximum to $\mathcal{M}$. An employee attaining that maximum presents exactly the pair in $\mathcal{M}$ and survives. No top earner can be missed.

**Tie coverage.** The test is applied row by row, so whenever several employees in one department share the maximum they all present the identical pair and all pass. This is the property the grouped-row shortcut cannot supply, and it is why this instance yields three rows rather than two.

**Single-row output.** The employee relation supplies the rows being classified and the department relation only supplies a name, so the result holds exactly one row per qualifying employee; treating the department relation as the driving relation would let empty departments reach the output. Salaries are compared under plain integer ordering, so the maximum is unambiguous even where values tie.

## 7. Boundary and Semantic Traps

| Instance | Input shape | Expected result | Why it matters |
|:---|:---|:---|:---|
| Two-way tie at the top | IT has `Jim` 90000 and `Max` 90000 | both employees | The case this lesson is built around; the grouped-row shortcut fails |
| Whole department tied | three employees at 10 in one department | all three | The threshold is attained by every member |
| Empty department | a `Department` row with no `Employee` rows | no output row for it | $\mathcal{M}$ has no pair for it, so nothing can match |
| Single-employee department | one employee at 7 | that employee | A maximum over a one-element multiset is that element |
| Negative salaries | the department maximum is $-2$ | the employee at $-2$ | Ordering is total on integers; a "greatest positive value" assumption is wrong |
| Missing department name | employee whose `departmentId` matches no `Department` row | no output row under an inner pairing | The name lookup is a genuine dependency |
| Equal maxima across departments | `Sales` also tops out at 90000 | both departments' top earners | Thresholds are per partition; a global maximum is the wrong classifier |

The last two rows separate per-group semantics from two misreadings: thresholds must be computed inside each department, and classification is on the pair rather than the salary alone, or a `Sales` employee earning an IT-level salary could be wrongly admitted or wrongly dropped.

## 8. Alternative Formulations and Their Costs

| Formulation | Relational shape | Handles ties? | Cost |
|:---|:---|:---:|:---|
| Partition, reduce each block to its maximum, then test each employee's pair for membership | One grouped reduction plus one membership filter | yes, by construction | $O(E)$ expected with hash grouping plus $O(E)$ probes |
| Dense rank over each department ordered by descending salary, then keep rank 1 | Sort or hash partition, windowed rank, row filter | yes | $O(E \log E)$ ordering plus $O(E)$ memory for the rank column |
| Group by department and select a name beside the maximum | One grouped reduction | no — one arbitrary member per group, rejected under strict grouping rules | $O(E)$ but semantically incomplete |
| Correlated search for a strictly greater salary in the same department | One scan with a nested probe per employee | yes — keep the employee when no greater salary exists | $O(E^2)$ without an index, $O(E \log E)$ with a sorted department index |

## 9. Complexity Derivation

Let $E = \lvert \text{Employee} \rvert$, $D = \lvert \text{Department} \rvert$, and $P \le \min(E, D)$ the number of distinct departments appearing in `Employee`.

**Time.** The grouping pass performs one bucket lookup and one comparison per employee row, giving $O(E)$ expected work and $P$ threshold pairs. The membership pass performs one expected-constant test per row plus one keyed name lookup per survivor, so it also costs $O(E)$. Hence

$$
T(E, D) = O(E) + O(E) = O(E)
$$

expected with hashing; index construction over the department relation contributes $O(D)$ at worst. Replacing hash grouping with sorted grouping raises the first pass to $O(E \log E)$.

**Auxiliary space.** One accumulator per distinct department in `Employee`, plus a result buffer of at most one row per employee:

$$
S(E, D) = O(P) + O(E) = O(E).
$$
