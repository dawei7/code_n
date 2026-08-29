# Guided Example: Find Candidates for Data Scientist Position

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Candidates": [{"candidate_id": 123, "skill": "Python"}, {"candidate_id": 234, "skill": "R"}, {"candidate_id": 123, "skill": "Tableau"}, {"candidate_id": 123, "skill": "PostgreSQL"}, {"candidate_id": 234, "skill": "PowerBI"}, {"candidate_id": 234, "skill": "SQL Server"}, {"candidate_id": 147, "skill": "Python"}, {"candidate_id": 147, "skill": "Tableau"}, {"candidate_id": 147, "skill": "Java"}, {"candidate_id": 147, "skill": "PostgreSQL"}, {"candidate_id": 256, "skill": "Tableau"}, {"candidate_id": 102, "skill": "DataAnalysis"}]}}`
- **Required output:** `{"columns": ["candidate_id"], "rows": [[123], [147]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Candidates`

The objective is to compute `{"columns": ["candidate_id"], "rows": [[123], [147]]}` from `{"tables": {"Candidates": [{"candidate_id": 123, "skill": "Python"}, {"candidate_id": 234, "skill": "R"}, {"candidate_id": 123, "skill": "Tableau"}, {"candidate_id": 123, "skill": "PostgreSQL"}, {"candidate_id": 234, "skill": "PowerBI"}, {"candidate_id": 234, "skill": "SQL Server"}, {"candidate_id": 147, "skill": "Python"}, {"candidate_id": 147, "skill": "Tableau"}, {"candidate_id": 147, "skill": "Java"}, {"candidate_id": 147, "skill": "PostgreSQL"}, {"candidate_id": 256, "skill": "Tableau"}, {"candidate_id": 102, "skill": "DataAnalysis"}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Core Step 1

**Discard irrelevant skills first.** The `WHERE` clause retains only rows whose `skill` is one of:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Candidates": [{"candidate_id": 123, "skill": "Python"}, {"candidate_id": 234, "skill": "R"}, {"candidate_id": 123, "skill": "Tableau"}, {"candidate_id": 123, "skill": "PostgreSQL"}, {"candidate_id": 234, "skill": "PowerBI"}, {"candidate_id": 234, "skill": "SQL Server"}, {"candidate_id": 147, "skill": "Python"}, {"candidate_id": 147, "skill": "Tableau"}, {"candidate_id": 147, "skill": "Java"}, {"candidate_id": 147, "skill": "PostgreSQL"}, {"candidate_id": 256, "skill": "Tableau"}, {"candidate_id": 102, "skill": "DataAnalysis"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

Skills such as Java or PowerBI do not help satisfy the requirement and do not need to participate in aggregation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Group the remaining rows by candidate.** `GROUP BY 1` groups by the first selected column, `candidate_id`. After filtering, a candidate's group can contain only required-skill rows.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["candidate_id"], "rows": [[123], [147]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Candidates": [{"candidate_id": 123, "skill": "Python"}, {"candidate_id": 234, "skill": "R"}, {"candidate_id": 123, "skill": "Tableau"}, {"candidate_id": 123, "skill": "PostgreSQL"}, {"candidate_id": 234, "skill": "PowerBI"}, {"candidate_id": 234, "skill": "SQL Server"}, {"candidate_id": 147, "skill": "Python"}, {"candidate_id": 147, "skill": "Tableau"}, {"candidate_id": 147, "skill": "Java"}, {"candidate_id": 147, "skill": "PostgreSQL"}, {"candidate_id": 256, "skill": "Tableau"}, {"candidate_id": 102, "skill": "DataAnalysis"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["candidate_id"], "rows": [[123], [147]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation:** Group all rows and require three separate sums such as `SUM(skill='Python')>0`. It works and does not rely as directly on filtered count, but is more verbose.
- **Three self-joins:** Joining one row per required skill proves presence, but repeats the table and can create more complex plans.
- **Relational division with `NOT EXISTS`:** It can express “no required skill is missing,” though it is heavier for a fixed three-item requirement.
- **Candidate has extra skills:** They are removed by `WHERE` and do not disqualify the candidate.
- **Candidate has only two required skills:** Filtered count is two, so the group fails.
- **Duplicate required skill:** The composite primary key forbids it; the count proof depends on that guarantee.
- **No candidate qualifies:** The result is an empty table.
- **Skill spelling and case:** Comparisons use the exact literals shown. Behavior under other casing depends on column collation, but the contract supplies the named values.
- **Ascending order:** `ORDER BY 1` refers to `candidate_id` and satisfies the output requirement.
- **COUNT(1):** For grouped rows it counts every row, equivalent here to `COUNT(*)`.
- **Why `COUNT(DISTINCT skill)` is not required:** Primary-key uniqueness already makes each candidate-skill pair singular. A distinct aggregate would be redundant under the schema, though it could make the query more defensive if that guarantee were removed.
- **Candidate with none of the skills:** All of that candidate's rows disappear in `WHERE`, so no group is formed and no output row can be produced.
- **Group alias by ordinal:** `GROUP BY 1` is accepted MySQL shorthand for the first select expression. Writing `GROUP BY candidate_id` would improve readability without changing execution.
- **Exact-match requirement:** `IN` compares complete skill values. A value such as `'Python Programming'` does not qualify unless collation or data normalization explicitly makes it equal to `'Python'`.
- **Stable result shape:** Aggregation emits only `candidate_id`, so the requested table contains no repeated skill rows and no accidental extra columns from the source schema.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + c log c)$. Let $R$ be the number of table rows and $C$ the number of candidates that have at least one required skill. The engine scans or indexes the relevant rows, groups by candidate, and sorts the passing identifiers. A common logical bound is $O(R+C\log C)$ time.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
