# Guided Example: Count Subarrays of Length Three With a Condition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 4, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return the number of subarrays of length 3 such that the sum of the first and third numbers equals *exactly* half of the second number.

The objective is to compute `1` from `{"nums": [1, 2, 1, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Every length-three subarray has one middle index.** A window ending around center `i` is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

Valid centers range from one through `len(nums)-2`. This visits every contiguous length-three subarray exactly once: its middle position uniquely identifies it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Rewrite the half condition using integers.** The statement requires

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit loop and counter:** It is equivalent and may be easier for beginners to debug.
- **Sliding window object:** Maintaining a queue is unnecessary because direct indexing already exposes all three values.
- **Floating-point half:** It is avoidable and less exact than multiplication.
- **Floor division:** It would incorrectly accept some odd-middle cases.
- **Odd-center counterexample:** `[0,1,0]` exposes the floor-division bug.
- **Minimum length three:** Exactly one center is examined.
- **Odd middle:** It can never satisfy the doubled integer equation.
- **Even middle:** It qualifies only when endpoints sum to its exact half.
- **Negative middle:** Cross-multiplication handles it normally.
- **Zero middle:** Endpoints must sum to zero.
- **Different cancelling endpoints:** Values such as -3 and 3 can qualify around zero.
- **Overlapping valid windows:** Each is counted independently.
- **Repeated values:** They have no special behavior.
- **Boolean arithmetic:** `true` contributes one and `false` contributes zero.
- **Return type:** Summing Booleans produces an integer.
- **Index safety:** Center range guarantees both neighbors exist.
- **Input preservation:** No element is changed.
- **Annotation import:** `List` must be available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For array length $n$, the generator evaluates $n-2$ centers. Each does constant arithmetic and indexing, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
