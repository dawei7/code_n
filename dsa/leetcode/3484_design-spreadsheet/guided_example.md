# Guided Example: Design Spreadsheet

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"], "arguments": [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]}`
- **Required output:** `[null, 12, null, 16, null, 25, null, 15]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A spreadsheet is a grid with 26 columns (labeled from `'A'` to `'Z'`) and a given number of `rows`. Each cell in the spreadsheet can hold an integer value between 0 and $10^{5}$.

The objective is to compute `[null, 12, null, 16, null, 25, null, 15]` from `{"operations": ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"], "arguments": [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Store only cells that have been explicitly assigned.** Every spreadsheet cell begins at zero, so allocating all `rows * 26` positions is optional. The protected class keeps dictionary `d` from a cell-reference string such as `"A1"` to its current explicitly stored value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"], "arguments": [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The constructor accepts `rows` because the required interface includes it, but the source does not use the number to allocate storage or validate references. Valid cell references are guaranteed by the problem, so no runtime bounds check is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The constructor accepts `rows` because the required interfac... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Setting a cell is a direct dictionary update.** `setCell(cell, value)` assigns `d[cell] = value`. Setting the same cell again replaces its previous mapping, which matches spreadsheet assignment semantics. The dictionary key is the complete reference string, so no row-and-column parsing is needed for storage.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 12, null, 16, null, 25, null, 15]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"], "arguments": [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 12, null, 16, null, 25, null, 15]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Allocate a full two-dimensional grid:** It giv:** - **Allocate a full two-dimensional grid:** It gives direct indexed access but uses $O(26\cdot rows)$ space even when very few cells are set.
- **Parse references into numeric coordinates:** This is necessary for an array grid but optional for a dictionary with canonical string keys.
- **Store reset cells as zero:** It is correct but keeps unnecessary entries; removing them restores the sparse default representation.
- **Unset cell in a formula:** `get(cell, 0)` supplies the required zero.
- **Repeated `setCell`:** Dictionary assignment replaces the old value, so only the latest setting matters.
- **Repeated `resetCell`:** `pop(..., null)` makes resetting an absent cell harmless.
- **Explicitly set zero:** The source stores it until reset; value semantics are still identical to an absent cell.
- **Two numeric operands:** No spreadsheet state is needed and both tokens are converted with `int`.
- **Two cell operands:** Each is looked up independently, including when both references are the same.
- **Mixed operand order:** The token test handles either `cell+number` or `number+cell`.
- **Constructor row count:** The source ignores it because inputs guarantee valid references; an API requiring validation would need to retain and check it.
- **No formula caching:** Results should reflect the latest cell values, so evaluating fresh lookups is the correct simple design.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Let $q$ be the total number of method calls and $s$ the number of dictionary entries currently stored. Dictionary set, pop, and get operations take expected $O(1)$ time. Parsing a reference or formula technically costs time proportional to its short string length, but column count, row digits, and numeric literal digits are bounded by the constraints. Under the problem's model, each operation is $O(1)$ expected time and all $q$ calls cost $O(q)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(s)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
