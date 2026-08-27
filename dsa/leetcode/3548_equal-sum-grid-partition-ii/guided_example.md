# Guided Example: Equal Sum Grid Partition II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 4], [2, 3]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `grid` of positive integers. Your task is to determine if it is possible to make **either one horizontal or one vertical cut** on the grid such that:

The objective is to compute `true` from `{"grid": [[1, 4], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: For a fixed cut, only one value can repair unequal sums

Consider a horizontal cut after row `i`. Let:

- `s1` be the sum above the cut;
- `s2` be the sum below the cut.

If `s1=s2`, no discount is needed and the cut is immediately valid.

If `s1>s2`, discounting a cell from the smaller bottom side would make the imbalance worse. The cell must come from the top and must have value exactly:

`diff = s1-s2`.

Then `s1-diff=s2`.

The symmetric rule applies when `s2>s1`. Because every grid value is positive, no other deletion value or side can equalize the sums. This turns the numerical part of each cut into one membership lookup.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 4], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain both side sums and value frequencies

At the start of `check(g)`:

- `s1=0` and `cnt1` is empty for the top side;
- `s2` is the total grid sum and `cnt2` counts every cell for the bottom side.

The scan moves one complete row at a time from side two to side one. After row `i` is moved:

- `s1` and `cnt1` describe rows zero through `i`;
- `s2` and `cnt2` describe rows `i+1` through `m-1`.

The loop stops at `m-2`, so both sections are always non-empty.

Frequency dictionaries are necessary because the same value may occur several times. Decrementing `cnt2[x]` as cells move ensures a lookup refers to the correct side of the current cut.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the start of `check(g)`:

- `s1=0` and `cnt1` is empty fo... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Connectivity is automatic for a true rectangle

If a section has at least two rows and at least two columns, deleting any one cell leaves it connected under four-direction movement.

Intuitively, a missing cell can be bypassed through an adjacent row or column. Even the smallest two-by-two rectangle leaves three cells forming a connected L shape. Larger rectangles contain enough alternate routes around one removed vertex.

Therefore, when the larger-sum side has both dimensions greater than one, the source needs only `cnt[diff] > 0`. Any occurrence of the required value is safe to discount.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 4], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rotate four times as in the editorial:** It al:** - **Rotate four times as in the editorial:** It also covers cut orientation and deletion side. The protected source checks both larger-side branches directly and needs only one transpose.
- **Use only a set:** Counts are needed while rows move between sides; a value may remain below after one copy moves above.
- **Ignore connectivity:** This falsely accepts deleting an interior cell from a one-row or one-column section.
- **Run graph connectivity after every candidate deletion:** Correct but far too expensive. Rectangle geometry reduces connectivity to a dimension/endpoint rule.
- **Equal section sums:** No deletion is selected, so connectivity remains automatic.
- **Required diff absent:** That cut cannot be repaired by one discount.
- **Required value occurs only at an unsafe interior path cell:** Frequency membership succeeds but endpoint checks correctly reject it.
- **Two-by-two section:** Removing any single cell leaves three connected cells.
- **One-cell section:** Its only cell is both endpoints; discounting it would leave the section empty. Could the source accept this? For a one-cell larger side, deleting its sole positive value would make its sum zero while the other non-empty side has positive sum, so equality is impossible; `diff` cannot equal that sole value when the other sum is positive.
- **Single-row original grid:** The first check has no horizontal cut; transposition converts vertical cuts into a multirow one-column case.
- **Single-column grid:** Endpoint rules apply directly to horizontal sections.
- **Duplicate values:** Side-specific counts ensure presence is tracked after row transfers.
- **Positive values:** They guarantee the larger side and exact positive difference determine the only possible discount.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let `N=mn`. One `check` first scans all `N` cells to initialize bottom counts, then moves each cell at most once while testing cuts. It takes `O(N)` expected time with hash-table operations.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
