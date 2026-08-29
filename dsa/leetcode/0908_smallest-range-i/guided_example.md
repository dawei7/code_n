# Guided Example: Smallest Range I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1], "k": 0}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `0` from `{"nums": [1], "k": 0}` while avoiding redundant calculations and unnecessary overhead.

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

Each original value $x$ may be moved anywhere in the closed interval

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1], "k": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The score depends only on the final maximum and minimum. Let

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

$$
\text{mi}=\min(\texttt{nums}),
\qquad
\text{mx}=\max(\texttt{nums}).
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1], "k": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Adjust every element greedily:** Explicit choices are unnecessary because the achievable optimum depends only on original extremes.
- **Sort the array:** The minimum and maximum would become endpoints, but sorting costs $O(n\log n)$ and is stronger than needed.
- **Binary search a target interval:** This can test feasibility but adds complexity when the closed-form intersection is immediate.
- **One element:** Maximum equals minimum, so the score is zero for every `k`.
- **`k = 0`:** No value changes, and the formula returns the original range.
- **Original range exactly `2k`:** Extreme intervals touch at one value, and score zero is achievable.
- **Original range smaller than `2k`:** The raw subtraction is negative, so `max(0, ...)` is essential.
- **Duplicate extremes:** Every occurrence has the same movement interval and can be moved into the same optimal final range.
- **Intermediate elements:** They cannot force a wider result because their original values lie between the two extremes.
- **Integer target:** All endpoints are integers, so a nonempty overlap contains an integer boundary point.
- **At most one operation:** Selecting the entire adjustment in one step reaches any point in `[x-k,x+k]`; repeated operations are unnecessary.
- **No input mutation:** The solution computes the minimum score without constructing a transformed array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Finding minimum and maximum each takes a linear scan. Two scans remain linear.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
