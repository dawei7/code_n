# Guided Example: Subsequences with a Unique Middle Mode I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 1, 1, 1, 1]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, find the number of subsequences of size 5 of `nums` with a **unique middle mode**.

The objective is to compute `6` from `{"nums": [1, 1, 1, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Fix the middle index first.** A length-five subsequence with middle at index `index` must choose exactly two indices to its left and exactly two to its right. Let middle value be `m`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 1, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

total index choices, where $L=\texttt{index}$ and $R=n-\texttt{index}-1$. The source counts all of them and subtracts selections where `m` is not the unique mode.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 1, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all five-index subsequences:** It costs $O(n^5)$ and is impossible at $n=1000$.
- **Enumerate competing values per middle:** It can become $O(n^2)$; maintained moments collapse those sums.
- **At least three middle copies:** The middle is automatically unique mode.
- **Exactly two middle copies:** Any other value appearing twice creates a tie and is invalid.
- **Only one middle copy:** It cannot be unique mode among five positions.
- **Not enough positions on one side:** Combination helper returns zero naturally for counts below two.
- **Negative and large values:** Counter keys handle them without coordinate compression.
- **Repeated equal values:** Distinct indices are counted through combination factors.
- **Middle removal timing:** The current occurrence must leave right before formulas are evaluated.
- **Left insertion timing:** It happens only after the current middle contribution is counted.
- **Modulo:** Subtraction may be negative before Python's final modulo normalizes it.
- **Moment exclusion:** Middle-value contributions are subtracted before counting competitors.
- **Generated source:** No local editorial exists; the explanation follows the exact inclusion-exclusion formulas.
- **Input preservation:** Only counters and scalar moments change.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Building the right counter costs $O(n)$. Each middle iteration performs a constant number of counter accesses, arithmetic updates, and aggregate formulas, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
