# Guided Example: Reshape Data: Melt

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"report": [{"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611}, {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}]}}`
- **Required output:** `{"columns": ["product", "quarter", "sales"], "rows": [["Umbrella", "quarter_1", 417], ["SleepingBag", "quarter_1", 800], ["Umbrella", "quarter_2", 224], ["SleepingBag", "quarter_2", 936], ["Umbrella", "quarter_3", 379], ["SleepingBag", "quarter_3", 93], ["Umbrella", "quarter_4", 611], ["SleepingBag", "quarter_4", 875]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a solution to **reshape** the data so that each row represents sales data for a product in a specific quarter.

The objective is to compute `{"columns": ["product", "quarter", "sales"], "rows": [["Umbrella", "quarter_1", 417], ["SleepingBag", "quarter_1", 800], ["Umbrella", "quarter_2", 224], ["SleepingBag", "quarter_2", 936], ["Umbrella", "quarter_3", 379], ["SleepingBag", "quarter_3", 93], ["Umbrella", "quarter_4", 611], ["SleepingBag", "quarter_4", 875]]}` from `{"tables": {"report": [{"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611}, {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Melt is the inverse shape of a pivot.** The input is wide: one product row contains four separate quarter columns. The desired result is long: each product-quarter combination becomes its own row, with the former column name stored in `quarter` and the former cell value stored in `sales`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"report": [{"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611}, {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

`pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Each argument defines one part of that reshape.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product", "quarter", "sales"], "rows": [["Umbrella", "quarter_1", 417], ["SleepingBag", "quarter_1", 800], ["Umbrella", "quarter_2", 224], ["SleepingBag", "quarter_2", 936], ["Umbrella", "quarter_3", 379], ["SleepingBag", "quarter_3", 93], ["Umbrella", "quarter_4", 611], ["SleepingBag", "quarter_4", 875]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"report": [{"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611}, {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product", "quarter", "sales"], "rows": [["Umbrella", "quarter_1", 417], ["SleepingBag", "quarter_1", 800], ["Umbrella", "quarter_2", 224], ["SleepingBag", "quarter_2", 936], ["Umbrella", "quarter_3", 379], ["SleepingBag", "quarter_3", 93], ["Umbrella", "quarter_4", 611], ["SleepingBag", "quarter_4", 875]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit `value_vars`:** Listing the four quarter labels makes the accepted schema narrower and prevents accidental melting of extra columns.
- **`DataFrame.melt` method:** `report.melt(...)` is equivalent to the top-level `pd.melt(report, ...)` used by the source.
- **Manual row construction:** Nested loops can emit product-quarter records but are slower and more error-prone than the native reshape.
- **Unexpected extra column:** Because `value_vars` is omitted, every non-product column would be melted.
- **Missing sales value:** It remains a missing `sales` entry; melt reshapes but does not fill or drop data.
- **Empty report:** The result is empty but still has `product`, `quarter`, and `sales` columns.
- **Quarter-column order:** It controls the block order of output rows because no explicit sort follows.
- **Original index:** Default melt behavior creates a fresh result index rather than preserving repeated source labels.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nq)$. Let $n$ be the number of products and $q$ the number of melted quarter columns. Every one of the $nq$ measurement cells becomes one output row, so time and output space are $O(nq)$. Here $q=4$ is fixed by the schema, reducing both to $O(n)$ as stated in the manifest.
- **Auxiliary Space Complexity:** $O(nq)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
