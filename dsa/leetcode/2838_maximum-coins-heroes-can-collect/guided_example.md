# Guided Example: Maximum Coins Heroes Can Collect

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heroes": [1, 4, 2], "monsters": [1, 1, 5, 2, 3], "coins": [2, 3, 4, 5, 6]}`
- **Required output:** `[5, 16, 10]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a battle and `n` heroes are trying to defeat `m` monsters. You are given two **1-indexed** arrays of **positive** integers `heroes` and `monsters` of length `n` and `m`, respectively. $\text{heroes}[i]$ is the power of $i^{\text{th}}$ hero, and $\text{monsters}[i]$ is the power of $i^{\text{th}}$ monster.

The objective is to compute `[5, 16, 10]` from `{"heroes": [1, 4, 2], "monsters": [1, 1, 5, 2, 3], "coins": [2, 3, 4, 5, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

**Every hero wants the sum of a power prefix.** A hero with power `h` can defeat every monster whose power is at most `h`. Coins are all positive, the hero loses no health, and defeating one monster does not prevent another hero from defeating it. Therefore, each hero should defeat every eligible monster.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heroes": [1, 4, 2], "monsters": [1, 1, 5, 2, 3], "coins": [2, 3, 4, 5, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The question for each hero is simply: after ordering monsters by power, how many monsters lie at or below `h`, and what is the sum of their corresponding coin rewards?

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Sort indices to preserve the monster-coin pairing.** The source builds

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 16, 10]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heroes": [1, 4, 2], "monsters": [1, 1, 5, 2, 3], "coins": [2, 3, 4, 5, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 16, 10]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort heroes with original indices and sweep:** As hero power rises, add newly defeatable monster coins once and write the running total to the hero's original position. This matches the manifest and replaces $n$ binary searches with one linear merge after sorting.
- **Sort monster-coin tuples:** This is more explicit than sorting indices and has the same asymptotic cost, at the price of allocating tuple pairs.
- **Brute force per hero:** Testing all monsters takes $O(nm)$ time and is too slow at $10^5$ by $10^5$.
- **No defeatable monster:** Upper bound returns zero, and prefix sum `s[0]` is zero.
- **Hero matches a monster exactly:** `bisect_right` includes all monsters with that power.
- **Hero defeats every monster:** The boundary is $m$, and `s[m]` is the total coin sum.
- **Duplicate monster powers:** All equal-power monsters are included together when the threshold reaches that power.
- **Duplicate hero powers:** They independently receive the same prefix total without interfering.
- **Large coin sum:** Python's arbitrary-precision integers preserve the full result.
- **Input preservation:** Sorting the index list leaves `heroes`, `monsters`, and `coins` unchanged.
- **Keyed bisect availability:** The exact code relies on a Python version whose `bisect_right` supports `key`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m\log m+n\log m)$. Let $m$ be the number of monsters and $n$ the number of heroes. Sorting the $m$ indices costs $O(m\log m)$. Building prefix sums costs $O(m)$.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
