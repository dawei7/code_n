# Guided Example: Change Null Values in a Table to the Previous Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"CoffeeShop": [{"id": 9, "drink": "Rum and Coke"}, {"id": 6, "drink": null}, {"id": 7, "drink": null}, {"id": 3, "drink": "St Germain Spritz"}, {"id": 1, "drink": "Orange Margarita"}, {"id": 2, "drink": null}]}}`
- **Required output:** `{"columns": ["id", "drink"], "rows": [[9, "Rum and Coke"], [6, "Rum and Coke"], [7, "Rum and Coke"], [3, "St Germain Spritz"], [1, "Orange Margarita"], [2, "Orange Margarita"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `CoffeeShop`

The objective is to compute `{"columns": ["id", "drink"], "rows": [[9, "Rum and Coke"], [6, "Rum and Coke"], [7, "Rum and Coke"], [3, "St Germain Spritz"], [1, "Orange Margarita"], [2, "Orange Margarita"]]}` from `{"tables": {"CoffeeShop": [{"id": 9, "drink": "Rum and Coke"}, {"id": 6, "drink": null}, {"id": 7, "drink": null}, {"id": 3, "drink": "St Germain Spritz"}, {"id": 1, "drink": "Orange Margarita"}, {"id": 2, "drink": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Carry one remembered drink through the presented rows

The required transformation is a forward fill: a non-null `drink` becomes the current remembered value, while a null `drink` receives the most recently remembered non-null value.

The exact MySQL query stores that memory in the session user variable `@cur`. Each output row evaluates:



For a non-null row, assignment expression `@cur := drink` both updates the variable and evaluates to the assigned drink, so the original value is returned. For a null row, no assignment occurs; the expression returns whatever drink the variable remembers from an earlier row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"CoffeeShop": [{"id": 9, "drink": "Rum and Coke"}, {"id": 6, "drink": null}, {"id": 7, "drink": null}, {"id": 3, "drink": "St Germain Spritz"}, {"id": 1, "drink": "Orange Margarita"}, {"id": 2, "drink": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first-row guarantee matters

The statement guarantees that the first presented row has a non-null drink. On that row, `@cur` is assigned before any null row needs it. Every later null can therefore inherit a real drink value.

If the first row were null and `@cur` had no value, the query would return null there because no preceding non-null drink exists. The guarantee removes that undefined logical case.

In a fresh MySQL session, an unset user variable reads as `NULL`. The source does not explicitly initialize `@cur`, so it relies on the first processed row overwriting it before the else branch is used. In a reused session where `@cur` had an old value, proper first-row processing still replaces it immediately.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the example state

Assume rows are evaluated in the displayed sequence.

- ID `9` contains `"Rum and Coke"`. The true branch assigns that string to `@cur` and returns it.
- ID `6` is null. The else branch returns the remembered `"Rum and Coke"`.
- ID `7` is also null and receives the same value.
- ID `3` contains `"St Germain Spritz"`, so `@cur` changes.
- ID `1` then changes it again to `"Orange Margarita"`.
- ID `2` is null and receives that latest value.

The output ID and computed drink are selected together, so every row retains its ID while only the drink field may be filled.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "drink"], "rows": [[9, "Rum and Coke"], [6, "Rum and Coke"], [7, "Rum and Coke"], [3, "St Germain Spritz"], [1, "Orange Margarita"], [2, "Orange Margarita"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"CoffeeShop": [{"id": 9, "drink": "Rum and Coke"}, {"id": 6, "drink": null}, {"id": 7, "drink": null}, {"id": 3, "drink": "St Germain Spritz"}, {"id": 1, "drink": "Orange Margarita"}, {"id": 2, "drink": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "drink"], "rows": [[9, "Rum and Coke"], [6, "Rum and Coke"], [7, "Rum and Coke"], [3, "St Germain Spritz"], [1, "Orange Margarita"], [2, "Orange Margarita"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive CTE with an order column:** Number rows, then recurse from row `r` to `r+1` carrying `COALESCE(current_drink, previous_drink)`. This is more explicit but needs a real ordering attribute.
- **Window function with `IGNORE NULLS`:** `LAST_VALUE` over a defined row order can express forward fill on engines supporting the needed null semantics; MySQL support and syntax vary.
- **Correlated previous-row lookup:** Find the greatest earlier ordered row with non-null drink. It is portable only when “earlier” has a schema key and may be less efficient.
- **Consecutive null rows:** They all reuse the same unchanged `@cur` value.
- **First row:** Its non-null guarantee initializes the carried value.
- **Later non-null row:** It replaces `@cur` and begins a new fill region.
- **No nulls:** Every row assigns and returns its own drink.
- **No explicit order column:** This is the central portability limitation; primary-key `id` does not encode displayed order.
- **Session-variable state:** A clean first processed row overwrites old state, but user-variable evaluation order remains MySQL-specific.
- **Output order:** The exact query relies on provider row presentation because it has no relational `ORDER BY` expression that can reproduce the requested sequence.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of rows. Under the intended streaming execution, the query examines each row once, performs one null test and at most one variable assignment, so its logical time is $O(R)$. The mutable state `@cur` uses $O(1)$ additional space beyond the $R$-row result.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
