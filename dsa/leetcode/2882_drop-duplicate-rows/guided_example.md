# Guided Example: Drop Duplicate Rows

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"customers": [{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 5, "name": "Finn", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]}}`
- **Required output:** `{"columns": ["customer_id", "name", "email"], "rows": [[1, "Ella", "emily@example.com"], [2, "David", "michael@example.com"], [3, "Zachary", "sarah@example.com"], [4, "Alice", "john@example.com"], [6, "Violet", "alice@example.com"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are some duplicate rows in the DataFrame based on the `email` column.

The objective is to compute `{"columns": ["customer_id", "name", "email"], "rows": [[1, "Ella", "emily@example.com"], [2, "David", "michael@example.com"], [3, "Zachary", "sarah@example.com"], [4, "Alice", "john@example.com"], [6, "Violet", "alice@example.com"]]}` from `{"tables": {"customers": [{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 5, "name": "Finn", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Duplicate identity is defined by email only.** Two customer rows may have different identifiers or names and still be duplicates for this task when their `email` values match. Conversely, rows with the same name are not duplicates if their email addresses differ. The `subset` argument tells pandas exactly which columns define equivalence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"customers": [{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 5, "name": "Finn", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

`customers.drop_duplicates(subset=['email'])`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `customers.drop_duplicates(subset=['email'])`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Passing a one-element list selects `email` as the sole duplicate key. Other columns are carried along from whichever row survives; they do not participate in deciding whether two rows belong to the same group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "name", "email"], "rows": [[1, "Ella", "emily@example.com"], [2, "David", "michael@example.com"], [3, "Zachary", "sarah@example.com"], [4, "Alice", "john@example.com"], [6, "Violet", "alice@example.com"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"customers": [{"customer_id": 1, "name": "Ella", "email": "emily@example.com"}, {"customer_id": 2, "name": "David", "email": "michael@example.com"}, {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"}, {"customer_id": 4, "name": "Alice", "email": "john@example.com"}, {"customer_id": 5, "name": "Finn", "email": "john@example.com"}, {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "name", "email"], "rows": [[1, "Ella", "emily@example.com"], [2, "David", "michael@example.com"], [3, "Zachary", "sarah@example.com"], [4, "Alice", "john@example.com"], [6, "Violet", "alice@example.com"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit `keep='first'`:** Adding the argument:** - **Explicit `keep='first'`:** Adding the argument makes the default visible and produces the same result.
- **In-place deletion:** `inplace=true` modifies the caller's DataFrame and returns `null`; the exact source instead returns a new result.
- **Group by email:** Taking the first row of every group can work but may change ordering or index structure and is unnecessarily complex.
- **All emails unique:** Every row survives in original order.
- **All emails equal:** Only the first row survives.
- **Nonconsecutive index:** Surviving labels are preserved; call `reset_index(drop=true)` only if a new index is explicitly required.
- **Duplicate names but different emails:** Both rows survive because `name` is outside the subset.
- **Repeated missing emails:** pandas retains the first and treats later missing keys as duplicates for this operation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of customer rows. Hash-based duplicate detection examines one email per row, giving expected $O(n)$ time. Building the keep mask or hash state and producing the result can require $O(n)$ auxiliary or output storage in the worst case, especially when all emails are unique. These are the manifest's stated bounds.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
