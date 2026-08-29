# Guided Example: Count Salary Categories

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Accounts": [{"account_id": 3, "income": 108939}, {"account_id": 2, "income": 12747}, {"account_id": 8, "income": 87709}, {"account_id": 6, "income": 91796}]}}`
- **Required output:** `{"columns": ["category", "accounts_count"], "rows": [["Low Salary", 1], ["Average Salary", 0], ["High Salary", 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Accounts`

The objective is to compute `{"columns": ["category", "accounts_count"], "rows": [["Low Salary", 1], ["Average Salary", 0], ["High Salary", 3]]}` from `{"tables": {"Accounts": [{"account_id": 3, "income": 108939}, {"account_id": 2, "income": 12747}, {"account_id": 8, "income": 87709}, {"account_id": 6, "income": 91796}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate the required labels from observed data.** A normal `GROUP BY` returns only categories that occur. This problem requires all three rows even when one count is zero. CTE `S` explicitly constructs the three category labels using constant `SELECT` statements combined by `UNION`. It is the guaranteed output skeleton.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Accounts": [{"account_id": 3, "income": 108939}, {"account_id": 2, "income": 12747}, {"account_id": 8, "income": 87709}, {"account_id": 6, "income": 91796}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Classify every account exactly once.** CTE `T` uses a `CASE` expression. Income below 20000 maps to `"Low Salary"`. Income above 50000 maps to `'High Salary'`. Every remaining income falls in the inclusive interval 20000 through 50000 and maps to `'Average Salary'`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The order of branches makes the boundaries precise. Exactly 20000 fails the low test and reaches the else branch. Exactly 50000 fails the high test and also reaches else. Values cannot belong to two categories, and every ordinary integer income belongs to one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["category", "accounts_count"], "rows": [["Low Salary", 1], ["Average Salary", 0], ["High Salary", 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Accounts": [{"account_id": 3, "income": 108939}, {"account_id": 2, "income": 12747}, {"account_id": 8, "income": 87709}, {"account_id": 6, "income": 91796}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["category", "accounts_count"], "rows": [["Low Salary", 1], ["Average Salary", 0], ["High Salary", 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three conditional aggregates with `UNION ALL`:** Each branch can count one category and always returns a row, but may conceptually scan `Accounts` three times. It is correct and simple for three fixed labels.
- **Single-row conditional sums then unpivot:** Compute all three counts in columns and convert them to rows. This can ensure one scan but uses more SQL machinery.
- **Inner join from `S` to `T`:** Incorrect when a category is empty because that required row disappears.
- **Income exactly 20000:** It belongs to Average Salary through the `ELSE` branch.
- **Income exactly 50000:** It also belongs to Average Salary; high is strictly greater.
- **No accounts in a category:** Missing grouped row becomes zero through `COALESCE`.
- **No accounts at all:** All three skeleton rows survive and each count is zero.
- **Positional grouping:** `GROUP BY 1` refers to computed category because it is selected first. Naming it explicitly would be more maintainable but equivalent.
- **Double-quoted low label:** MySQL normally treats `"Low Salary"` as a string unless ANSI_QUOTES mode changes quoting semantics; single quotes are more portable, but the exact source uses both styles.
- **Count reconciliation:** Because each non-null income reaches exactly one `CASE` result, the three returned counts should add up to the number of accounts. A different total signals altered null or boundary assumptions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A)$. Let $A$ be the number of account rows. Classification and aggregation inspect each account once, giving expected $O(A)$ time with hash grouping. Sorting-based grouping may use $O(A\log A)$ physically, but only three possible group keys exist, so engines can maintain constant-sized aggregate state efficiently.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
