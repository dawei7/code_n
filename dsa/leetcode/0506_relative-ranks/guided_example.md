# Guided Example: Relative Ranks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"score": [1]}`
- **Required output:** `["Gold Medal"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `score` of size `n`, where $\text{score}[i]$ is the score of the $i^{\text{th}}$ athlete in a competition. All the scores are guaranteed to be **unique**.

The objective is to compute `["Gold Medal"]` from `{"score": [1]}` while avoiding redundant calculations and unnecessary overhead.

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

Rank depends on score order, but the returned strings must appear in the athletes' original input order. The solution separates those two concerns:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"score": [1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. sort original indices by their athletes' scores;
2. assign each placement back into an answer cell at the original index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`idx = list(range(n))` creates `[0, 1, ..., n - 1]`. Each value is an athlete's original position. Sorting this index list rather than `score` itself preserves the input and permanently carries the information needed to place the final label.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["Gold Medal"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"score": [1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["Gold Medal"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort score-index pairs:** Build `(score, original_index)` tuples and sort descending. It is equivalent but stores both fields explicitly rather than sorting lightweight indices.
- **Score-to-index dictionary plus sorted score copy:** Unique scores make this valid, but the index list already preserves the mapping without an additional hash table.
- **Max-heap:** Pop athletes from highest score to lowest and assign increasing placements. It also costs $O(n\log n)$.
- **Direct score-range array:** With bounded nonnegative scores, map score to index and scan downward. It can take $O(n+M)$ time and $O(M)$ space where `M` is the maximum score, which is wasteful when scores are sparse.
- **One athlete:** The only athlete receives `"Gold Medal"`.
- **Two athletes:** They receive gold and silver; no bronze athlete exists.
- **Exactly three athletes:** Every output is a medal name and no numeric placement is used.
- **Unique-score guarantee:** It removes ties. If ties were allowed, the placement policy would need to be specified before this sort could assign ranks.
- **Preserve input:** Only `idx` is sorted; `score` remains unchanged.
- **Original output order:** Writing to `ans[j]` is essential. Appending labels in sorted order would return placement order instead of athlete order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of athletes. Creating `idx` takes $O(n)$ time. Sorting it dominates at $O(n\log n)$ time, and assigning all labels takes another $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
