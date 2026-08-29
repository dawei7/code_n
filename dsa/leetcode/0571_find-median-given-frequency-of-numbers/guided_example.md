# Guided Example: Find Median Given Frequency of Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Numbers": [{"num": 1, "frequency": 1}, {"num": 3, "frequency": 1}]}}`
- **Required output:** `{"columns": ["median"], "rows": [[2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Numbers`

The objective is to compute `{"columns": ["median"], "rows": [[2]]}` from `{"tables": {"Numbers": [{"num": 1, "frequency": 1}, {"num": 3, "frequency": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The table is a compressed sorted multiset: row `(num, frequency)` means `num` appears that many times. The query locates the middle position or positions without physically expanding those copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Numbers": [{"num": 1, "frequency": 1}, {"num": 3, "frequency": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

CTE `t` attaches three cumulative quantities to each distinct number row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Count copies at or below the current number.** The ascending window:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["median"], "rows": [[2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Numbers": [{"num": 1, "frequency": 1}, {"num": 3, "frequency": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["median"], "rows": [[2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Expand every occurrence:** It makes median positions obvious but costs $O(T)$ time and space rather than working with $R$ compressed rows.
- **Compute cumulative ascending positions only:** It can locate explicit middle ranks, but the two-sided condition elegantly handles odd and even totals.
- **Odd total:** Exactly one value block contains the middle.
- **Even total, distinct middle values:** Two rows are averaged.
- **Even total, same middle value:** One compressed row is sufficient.
- **One distinct number:** It is the median regardless of frequency.
- **Large frequency:** Window sums handle it without row expansion.
- **Negative numbers:** Numeric ordering and averaging work unchanged.
- **Rounding:** Applied after the median average, to one decimal place.
- **Supporting index:** It may improve physical execution without changing query semantics.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be the number of compressed rows. A typical engine sorts rows by `num` for ordered windows, requiring $O(R\log R)$ time without a supporting index. Computing cumulative sums and filtering adds $O(R)$ work.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
