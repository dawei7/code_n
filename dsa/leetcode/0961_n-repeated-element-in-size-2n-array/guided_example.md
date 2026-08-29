# Guided Example: N-Repeated Element in Size 2N Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` with the following properties:

The objective is to compute `3` from `{"nums": [1, 2, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The contract makes the first duplicate decisive

The array contains exactly one value that occurs more than once: it appears `n` times. Every other distinct value occurs exactly once.

Therefore, as soon as a left-to-right scan encounters a value already seen, that value must be the required repeated element. No other value can produce a duplicate encounter.

The solution uses set `s` to remember values from earlier positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Step-by-step scan

For each value `x`:

1. Check whether `x in s`.
2. If it is present, return `x` immediately.
3. Otherwise, add `x` to the set and continue.

The membership check must happen before insertion. Inserting first would make every value appear present and incorrectly return the first element.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a duplicate must eventually appear

The repeated value occurs `n` times and the constraints give `n >= 2`. Its second occurrence therefore exists.

By the time that second occurrence is scanned, the first is already in `s`, so the method returns no later than that position.

This is why the exact function has no explicit return after the loop. Under the promised input contract, control can never fall through.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency counter:** Count all values and return the one with count `n`. It has the same asymptotic bounds but may scan more than necessary.
- **Fixed value-range array:** Values are at most ten thousand, so a Boolean array can replace the hash set at the cost of range-sized storage.
- **Constant-space distance observation:** The frequent element must repeat within a small index gap; comparing nearby positions can yield `O(1)` space, but its proof is less direct.
- **Sort the array:** Equal copies become adjacent, but sorting costs `O(N log N)` and may mutate input.
- **Second element is duplicate:** The method returns immediately after one insertion.
- **Duplicate appears late:** Singleton values accumulate in the set until the second target occurrence.
- **Value zero:** It is an ordinary hashable integer and needs no sentinel handling.
- **No explicit fallback return:** Safe only because the input guarantees a repeated value with at least two copies.
- **Other values unique:** This promise is essential. Without it, the first duplicate need not be the most frequent value.
- **Input preservation:** The set-based scan does not modify `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the array length, which equals `2n` in the statement.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
