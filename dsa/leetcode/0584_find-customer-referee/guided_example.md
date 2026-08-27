# Guided Example: Find Customer Referee

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customer": [{"id": 1, "name": "Alice", "referee_id": 1}, {"id": 2, "name": "Bob", "referee_id": 2}, {"id": 3, "name": "Cara", "referee_id": null}]}}`
- **Required output:** `{"columns": ["name"], "rows": [["Alice"], ["Cara"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customer`

The objective is to compute `{"columns": ["name"], "rows": [["Alice"], ["Cara"]]}` from `{"tables": {"Customer": [{"id": 1, "name": "Alice", "referee_id": 1}, {"id": 2, "name": "Bob", "referee_id": 2}, {"id": 3, "name": "Cara", "referee_id": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why `NULL != 2` is not true

SQL uses three-valued logic. A comparison can evaluate to true, false, or unknown. `NULL` represents an absent or unknown value, so comparing it with an ordinary value does not produce true or false:



evaluates to unknown. A `WHERE` clause retains only rows whose condition is true; it discards both false and unknown results. Therefore, a plain inequality would accidentally remove customers with no referee even though the problem explicitly wants them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customer": [{"id": 1, "name": "Alice", "referee_id": 1}, {"id": 2, "name": "Bob", "referee_id": 2}, {"id": 3, "name": "Cara", "referee_id": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How `COALESCE` combines the two cases

The exact query uses:



`COALESCE` returns its first non-`NULL` argument.

- If `referee_id` is present, `COALESCE(referee_id, 0)` returns the actual ID. The row passes exactly when that ID is not 2.
- If `referee_id` is `NULL`, `COALESCE` returns 0. Since 0 is not 2, the row passes.

Zero is used only as a comparison substitute. It is not selected, written back to the table, or presented as the customer’s actual referee. Even if zero were itself an allowed stored ID, a real zero should qualify because it is not 2, so the substitution has the same truth outcome required for this particular predicate.

The more literal equivalent is:



That form explicitly names both categories. The `COALESCE` form compresses them into one two-valued comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact query uses:



`COALESCE` returns its first non-`N... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the query needs no join

The problem does not ask for the referee’s name or any other referee details. It asks only whether the stored referee ID equals 2. Every required value—customer name and referee ID—is already in the `Customer` row. A self-join would add work without supplying information needed by the condition.

The query projects only `name` because that is the requested output column:



Result order is unrestricted, so `ORDER BY` is intentionally absent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name"], "rows": [["Alice"], ["Cara"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customer": [{"id": 1, "name": "Alice", "referee_id": 1}, {"id": 2, "name": "Bob", "referee_id": 2}, {"id": 3, "name": "Cara", "referee_id": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name"], "rows": [["Alice"], ["Cara"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit disjunction:** `referee_id <> 2 OR re:** - **Explicit disjunction:** `referee_id <> 2 OR referee_id IS NULL` most directly mirrors the two requirements and avoids choosing a sentinel.
- **Null-safe comparison:** In MySQL, `NOT (referee_id <=> 2)` uses the null-safe equality operator and negates it. It is compact but less portable and less familiar.
- **Plain inequality:** `referee_id != 2` is incorrect because rows with `NULL` evaluate to unknown and are filtered out.
- **Equality to `NULL`:** `referee_id = NULL` is also unknown, never the proper null test. Use `IS NULL`.
- **`NOT IN (2)`:** This has the same null problem as ordinary inequality; `NULL NOT IN (2)` is unknown.
- **Self-join to referees:** Unnecessary because only the numeric referee ID is tested, not any referring customer attribute.
- **Customer whose own ID is 2:** The customer still qualifies unless their `referee_id` is 2. The two columns have different meanings.
- **No referee:** A `NULL` value must be included and remains unmodified in the table; zero is only a temporary predicate value.
- **Referee ID exactly 2:** The row is the only category excluded.
- **Any other referee ID:** Negative, zero, positive, or large values all satisfy “not 2” if the schema permits them.
- **Duplicate customer names:** The output can contain repeated names from distinct customer rows. Adding `DISTINCT` would change the row semantics without a requirement.
- **Any result order:** No `ORDER BY` is needed, avoiding unnecessary sorting.
- **Sentinel caution:** `COALESCE(referee_id, 0)` is valid because both missing and actual zero should pass `!= 2`. A sentinel must be reconsidered whenever the comparison changes.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of rows in `Customer`. Without a selective usable index for this predicate, the database scans all rows, evaluates one constant-time expression per row, and takes $O(n)$ time. It can stream qualifying names, requiring $O(1)$ auxiliary working memory outside the output.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
