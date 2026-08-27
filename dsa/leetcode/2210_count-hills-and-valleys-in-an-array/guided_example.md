# Guided Example: Count Hills and Valleys in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 1, 1, 6, 5]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. An index `i` is part of a **hill** in `nums` if the closest non-equal neighbors of `i` are smaller than $\text{nums}[i]$. Similarly, an index `i` is part of a **valley** in `nums` if the closest non-equal neighbors of `i` are larger than $\text{nums}[i]$. Adjacent indices `i` and `j` are part of the **same** hill or valley if $\text{nums}[i] = \text{nums}[j]$.

The objective is to compute `3` from `{"nums": [2, 4, 1, 1, 6, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why plateaus can be compressed

Every index inside one equal run has the same value and the same closest non-equal values outside that run.

Therefore all of those indices are part of the same hill, the same valley, or neither. Counting more than one index from the run would double-count the same feature.

The algorithm chooses the run's final index as its one representative because the next array position is then immediately available as the right non-equal neighbor.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 1, 1, 6, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Skip an index that is not the plateau end

When `nums[i] == nums[i + 1]`, the equal run continues to the right. Index `i` cannot yet identify the closest non-equal right neighbor.

The code continues without changing `j`. This preserves the previous distinct plateau until the current run reaches its final position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When `nums[i] == nums[i + 1]`, the equal run continues to th... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Interpret `j` as the left distinct reference

Initially `j = 0`. Each time a plateau end is processed, the code sets `j = i`.

For a normal internal plateau, this makes `nums[j]` the value of the immediately preceding distinct run when the next plateau end is reached. Any equal values between `j` and that later `i` belong to the later plateau and were skipped.

At the starting plateau, `j` may point to an equal value rather than a non-equal left neighbor. Both strict comparisons then fail, correctly preventing the boundary plateau from being counted when no left non-equal neighbor exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 1, 1, 6, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicitly compress duplicates:** Build a new :** - **Explicitly compress duplicates:** Build a new array containing one value per plateau, then count strict local extrema. It is conceptually simple but uses $O(n)$ extra space.
- **Scan for neighbors per index:** Searching left and right works but can cost $O(n^2)$ across long plateaus.
- **All values equal:** Every internal index is skipped, and the answer is zero.
- **Strictly increasing array:** Every internal value lies between its neighbors, so there are no hills or valleys.
- **Strictly decreasing array:** The same reasoning gives zero.
- **Starting plateau:** It lacks a distinct left neighbor and is not counted.
- **Ending plateau:** It lacks a distinct right neighbor and is not counted.
- **Single-element plateau:** It is processed immediately when its next value differs.
- **Long internal plateau:** Only its final index is evaluated.
- **Alternating values:** Every internal singleton may alternate between hill and valley.
- **Strict comparisons:** Equal neighboring plateau values are compressed rather than treated as higher or lower.
- **Two independent conditions:** Mutual exclusivity prevents double increment.
- **Input preservation:** The array remains unchanged; compression is logical through pointer `j`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop visits each internal index once and performs constant work. No backward or forward searches are repeated, so time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
