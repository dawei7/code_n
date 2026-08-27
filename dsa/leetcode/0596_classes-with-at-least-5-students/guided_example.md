# Guided Example: Classes With at Least 5 Students

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Courses": [{"student": "s1", "class": "Math"}, {"student": "s2", "class": "Math"}, {"student": "s3", "class": "Math"}, {"student": "s4", "class": "Math"}, {"student": "s5", "class": "Math"}, {"student": "s1", "class": "Art"}]}}`
- **Required output:** `{"columns": ["class"], "rows": [["Math"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Courses`

The objective is to compute `{"columns": ["class"], "rows": [["Math"]]}` from `{"tables": {"Courses": [{"student": "s1", "class": "Math"}, {"student": "s2", "class": "Math"}, {"student": "s3", "class": "Math"}, {"student": "s4", "class": "Math"}, {"student": "s5", "class": "Math"}, {"student": "s1", "class": "Art"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Creating one group per class

The query selects `class` and writes:



The ordinal `1` refers to the first expression in the `SELECT` list, which is `class`. It is therefore equivalent to `GROUP BY class`. All Math enrollments become one group, all English enrollments another, and so on.

Ordinal grouping is concise, but spelling out the column can be easier to maintain: if the select-list order changes, `GROUP BY 1` may begin referring to a different expression. In this exact query, its meaning is unambiguous.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Courses": [{"student": "s1", "class": "Math"}, {"student": "s2", "class": "Math"}, {"student": "s3", "class": "Math"}, {"student": "s4", "class": "Math"}, {"student": "s5", "class": "Math"}, {"student": "s1", "class": "Art"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why counting rows counts students

`COUNT(1)` counts every row in a group because the literal 1 is never `NULL`. The composite primary key `(student, class)` guarantees that the same student-class enrollment cannot appear twice. Therefore, the number of rows in a class group equals the number of distinct students enrolled in that class.

Without that uniqueness guarantee, repeated duplicate enrollment rows could inflate `COUNT(1)`, and `COUNT(DISTINCT student)` would be necessary. Here, ordinary row count is sufficient and simpler.

For the sample, Math’s group contains rows for A, C, E, G, H, and I, giving count six. Every other class group has count one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `COUNT(1)` counts every row in a group because the literal 1... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the condition belongs in `HAVING`

The query uses:



`WHERE` filters individual rows before grouping; it cannot decide based on the final size of a group. `HAVING` filters after aggregation, so it can retain or discard an entire class according to `COUNT(1)`.

The comparison is `>= 5` because “at least five” includes exactly five. A strict `> 5` would incorrectly exclude a class with precisely five students.

The aggregate count guides filtering but is not selected. The output needs only the class names, so each surviving group contributes its `class` value and nothing else.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["class"], "rows": [["Math"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Courses": [{"student": "s1", "class": "Math"}, {"student": "s2", "class": "Math"}, {"student": "s3", "class": "Math"}, {"student": "s4", "class": "Math"}, {"student": "s5", "class": "Math"}, {"student": "s1", "class": "Art"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["class"], "rows": [["Math"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Grouped subquery:** Compute `class, COUNT(*) A:** - **Grouped subquery:** Compute `class, COUNT(*) AS total` in a subquery and filter `total >= 5` outside. Correct, but `HAVING` expresses the same operation more directly.
- **`COUNT(DISTINCT student)`:** Robust if duplicate enrollment rows are possible, but redundant under the composite primary key.
- **`WHERE COUNT(...)`:** Invalid logical placement because `WHERE` runs before aggregate groups exist.
- **Window count:** Annotate each row with `COUNT(*) OVER (PARTITION BY class)`, filter, then use `DISTINCT class`. It retains unnecessary row detail and needs deduplication.
- **Exactly five students:** Must be included; the boundary operator is `>=`.
- **Four students:** Must be excluded.
- **One student in several classes:** Counted once in each class group, which is correct.
- **Duplicate enrollment pair:** Forbidden by the primary key. If the schema changed, row counting could overcount.
- **Empty table:** No groups exist, so the result is empty.
- **Any output order:** No sorting is required.
- **Ordinal grouping:** `GROUP BY 1` means the selected `class` column here; explicit naming is clearer if columns may be reordered.
- **Counting a nullable column:** `COUNT(1)` avoids null-sensitive undercounting. Every row contributes exactly one.
- **Output schema:** The count is used only by `HAVING`; returning it would add an unrequested column.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $n$ be the number of enrollment rows and $c$ the number of distinct classes. A hash aggregation reads all $n$ rows and keeps one counter per class, taking expected $O(n)$ time and $O(c)$ state.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
