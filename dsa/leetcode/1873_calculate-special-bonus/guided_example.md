# Guided Example: Calculate Special Bonus

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3800}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7700}]}}`
- **Required output:** `{"columns": ["employee_id", "bonus"], "rows": [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["employee_id", "bonus"], "rows": [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]}` from `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3800}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7700}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Translate the rule into a row-by-row condition.** Every input employee must appear in the output exactly once, and only the computed `bonus` changes from row to row. An employee earns their full `salary` only when both positive requirements hold: `employee_id` is odd and `name` does not begin with uppercase `M`. The SQL source writes the logically equivalent negative form: assign zero when the ID is even **or** the first character is `M`; otherwise assign the salary. This use of De Morgan's law is worth making explicit:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3800}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7700}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\neg(\text{odd and not-M}) = \text{even or M}.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Because integer parity has only two possibilities, “not odd” is “even.” Because the relevant name test is specifically whether the first character is uppercase `M`, “not not-M” is that the first character is `M`. The query's condition therefore covers exactly the rows that are disqualified from a bonus.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "bonus"], "rows": [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"employee_id": 2, "name": "Meir", "salary": 3000}, {"employee_id": 3, "name": "Michael", "salary": 3800}, {"employee_id": 7, "name": "Addilyn", "salary": 7400}, {"employee_id": 8, "name": "Juan", "salary": 6100}, {"employee_id": 9, "name": "Kannon", "salary": 7700}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "bonus"], "rows": [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Positive-form `IF`:** `IF(employee_id % 2 = 1 AND LEFT(name, 1) <> 'M', salary, 0)` mirrors the statement directly. It is equivalent for the stated non-null data, while the source's disqualifier form makes the zero cases especially visible.
- **`CASE WHEN`:** A standard `CASE WHEN ... THEN 0 ELSE salary END` expression can replace MySQL-specific `IF` and is often more portable across database systems; it does not improve asymptotic complexity.
- **Regular-expression name test:** `name REGEXP '^M'` can detect the initial, but a regular-expression engine is unnecessary for a fixed one-character prefix. `LEFT(name, 1) = 'M'` states the exact operation simply.
- **Uppercase versus lowercase:** The rule names uppercase `'M'`. Whether a lowercase `m` compares equal can depend on the column collation in MySQL. The exact query follows the database's collation semantics rather than forcing binary case sensitivity.
- **Names with one character:** `LEFT(name, 1)` returns that character, so a name equal to `M` is correctly disqualified. No special length branch is necessary.
- **Null values:** The supplied table contract normally treats the relevant fields as populated. If `name` were `NULL`, SQL three-valued logic could make the condition `NULL` for an odd ID and MySQL `IF` would take its false branch, granting salary. A nullable extension would need an explicit policy and perhaps `COALESCE`; inventing one would change the stated contract.
- **Output ordering:** Omitting `ORDER BY` is incorrect even if a sample run happens to appear sorted, because relational tables have no guaranteed default row order. `ORDER BY 1` is valid here only because `employee_id` is the first selected expression.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `Employees`. Evaluating remainder, `LEFT` for one character, the comparison, and `IF` takes constant work per row under the usual bounded-field model, so producing the unsorted projection costs $O(R)$. The required `ORDER BY` can sort all $R$ result rows, giving $O(R\log R)$ total time in the general case. If the database can read through a suitable index on `employee_id` in ascending order, the optimizer may avoid an explicit sort, but the query does not require such an index beyond the logical uniqueness guarantee.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
