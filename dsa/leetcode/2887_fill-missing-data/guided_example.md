# Guided Example: Fill Missing Data

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"products": [{"name": "Wristwatch", "quantity": null, "price": 135}, {"name": "WirelessEarbuds", "quantity": null, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]}}`
- **Required output:** `{"columns": ["name", "quantity", "price"], "rows": [["Wristwatch", 0, 135], ["WirelessEarbuds", 0, 821], ["GolfClubs", 779, 9319], ["Printer", 849, 3051]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to fill in the missing value as `**0**` in the `quantity` column.

The objective is to compute `{"columns": ["name", "quantity", "price"], "rows": [["Wristwatch", 0, 135], ["WirelessEarbuds", 0, 821], ["GolfClubs", 779, 9319], ["Printer", 849, 3051]]}` from `{"tables": {"products": [{"name": "Wristwatch", "quantity": null, "price": 135}, {"name": "WirelessEarbuds", "quantity": null, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Restrict missing-value repair to the quantity column.** The DataFrame also contains `name` and `price`, but the task asks to replace missing values only in `quantity`. The exact source selects that Series, fills its missing entries, and assigns the result back:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"products": [{"name": "Wristwatch", "quantity": null, "price": 135}, {"name": "WirelessEarbuds", "quantity": null, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`products['quantity'] = products['quantity'].fillna(0)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `products['quantity'] = products['quantity'].fillna(0)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This preserves missing values elsewhere rather than applying a table-wide fill that could replace unrelated data with an inappropriate number.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "quantity", "price"], "rows": [["Wristwatch", 0, 135], ["WirelessEarbuds", 0, 821], ["GolfClubs", 779, 9319], ["Printer", 849, 3051]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"products": [{"name": "Wristwatch", "quantity": null, "price": 135}, {"name": "WirelessEarbuds", "quantity": null, "price": 821}, {"name": "GolfClubs", "quantity": 779, "price": 9319}, {"name": "Printer", "quantity": 849, "price": 3051}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "quantity", "price"], "rows": [["Wristwatch", 0, 135], ["WirelessEarbuds", 0, 821], ["GolfClubs", 779, 9319], ["Printer", 849, 3051]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **DataFrame-level dictionary fill:** `products.f:** - **DataFrame-level dictionary fill:** `products.fillna({'quantity': 0})` expresses the same column-specific replacement and can return a new DataFrame.
- **In-place Series fill:** It is concise but can trigger chained-view warnings or changing pandas semantics; explicit reassignment is safer.
- **`assign` method:** `products.assign(quantity=products['quantity'].fillna(0))` is convenient when mutation should be avoided.
- **Existing zero quantity:** It remains zero because zero is a real value, not a missing marker.
- **Missing values in `name` or `price`:** They remain untouched because only `quantity` is selected.
- **No missing quantities:** Values remain the same, though a result Series is still formed.
- **All quantities missing:** Every row receives zero.
- **Dtype:** Filling may not convert a float-backed column to integer; the exact source repairs values only.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of products. `fillna` inspects $n$ quantity positions and creates a result of length $n$, so time is $O(n)$ and temporary or replacement storage is $O(n)$. Assignment connects that result to the DataFrame. These bounds match the manifest.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
