# Guided Example: Reshape Data: Concatenate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"df1": [{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}], "df2": [{"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]}}`
- **Required output:** `{"columns": ["student_id", "name", "age"], "rows": [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17], [5, "Leo", 7], [6, "Alex", 7]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to concatenate these two DataFrames **vertically** into one DataFrame.

The objective is to compute `{"columns": ["student_id", "name", "age"], "rows": [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17], [5, "Leo", 7], [6, "Alex", 7]]}` from `{"tables": {"df1": [{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}], "df2": [{"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Vertical concatenation appends rows, not columns.** Both input DataFrames have the same three-column schema. The desired output places every row of `df1` first and then every row of `df2` underneath it. pandas calls this concatenation along axis zero, which is also the default for `pd.concat`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"df1": [{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}], "df2": [{"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source passes the two tables as an ordered list:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`pd.concat([df1, df2], ignore_index=true)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "name", "age"], "rows": [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17], [5, "Leo", 7], [6, "Alex", 7]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"df1": [{"student_id": 1, "name": "Mason", "age": 8}, {"student_id": 2, "name": "Ava", "age": 6}, {"student_id": 3, "name": "Taylor", "age": 15}, {"student_id": 4, "name": "Georgia", "age": 17}], "df2": [{"student_id": 5, "name": "Leo", "age": 7}, {"student_id": 6, "name": "Alex", "age": 7}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "name", "age"], "rows": [[1, "Mason", 8], [2, "Ava", 6], [3, "Taylor", 15], [4, "Georgia", 17], [5, "Leo", 7], [6, "Alex", 7]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Omit `axis=0`:** The source does so because vertical concatenation is pandas' default; writing it explicitly would be equivalent.
- **Preserve old indexes:** Leaving `ignore_index=false` yields possibly duplicate source labels and does not match the continuous-index behavior of this solution.
- **Horizontal concatenation:** `axis=1` places columns beside each other and solves a different reshape problem.
- **One input empty:** The result contains the other input's rows with a fresh continuous index.
- **Both inputs empty:** The output remains empty while preserving the aligned column schema.
- **Duplicate student identifiers:** They are retained because concatenation is not deduplication.
- **Different column order:** pandas aligns by label; under the promised same schema, values still reach the correct columns.
- **Unexpected extra column:** General concat forms a union and inserts missing values, but valid inputs avoid that schema mismatch.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m)$. Let $n$ and $m$ be the input row counts. With the fixed three-column schema, the output contains $n+m$ records and concatenation takes $O(n+m)$ time to construct the combined table and index. The returned table requires $O(n+m)$ space. These are the manifest's stated bounds.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
