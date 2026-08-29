# Guided Example: Happy Students

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of length `n` where `n` is the total number of students in the class. The class teacher tries to select a group of students so that all the students remain happy.

The objective is to compute `2` from `{"nums": [1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Fix the number selected before deciding who they are.** Suppose exactly $i$ students are selected. A student with threshold `nums[p]` is happy in the selected group only when $i>\text{nums}[p]$. A student left out is happy only when $i<\text{nums}[p]$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

These strict inequalities force membership. Every student with threshold less than $i$ must be selected, because leaving that student out would require $i$ to be smaller than their threshold. Every student with threshold greater than $i$ must be unselected, because selecting that student would require $i$ to be greater than their threshold. A student with threshold exactly $i$ can never be happy: selected would need $i>i$, while unselected would need $i<i$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Consequently, once the group size $i$ is fixed, there is at most one possible happy group: it consists of exactly the students whose thresholds are smaller than $i$. The problem becomes counting which sizes are self-consistent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Frequency array:** Count each threshold, sweep possible sizes, and track how many thresholds are smaller than the current size. This avoids comparison sorting and runs in $O(n)$ time with $O(n)$ space.
- **Trying arbitrary subsets:** Exponential subset enumeration is unnecessary because a fixed valid size uniquely forces membership by threshold.
- **Empty group:** It is valid only when the minimum threshold is strictly greater than `0`; any threshold-`0` student would be unhappy while unselected.
- **Full group:** It is always valid under `nums[i] < n`, because selecting $n$ students makes $n$ strictly greater than every threshold.
- **Threshold equal to group size:** Such a student cannot be happy either selected or unselected, so the entire candidate size must be rejected.
- **Duplicate thresholds:** Sorting and boundary checks handle them naturally. A block equal to the cut size makes that cut invalid.
- **Input mutation:** `nums.sort()` changes the input order. That does not affect the returned count, but callers that need the original order would have to sort a copy.
- **Strict inequality trap:** Selected students require threshold $<i$, while unselected students require threshold $>i$; equality is never permitted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Sorting dominates the running time at $O(n\log n)$. The subsequent loop examines `n + 1` possible cuts and does constant work for each, adding $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
