# Guided Example: Maximum Containers on a Ship

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "w": 3, "maxWeight": 15}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n` representing an `n x n` cargo deck on a ship. Each cell on the deck can hold one container with a weight of **exactly** `w`.

The objective is to compute `4` from `{"n": 2, "w": 3, "maxWeight": 15}` while avoiding redundant calculations and unnecessary overhead.

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

**Two independent limits bound the container count.** An $n\times n$ deck has exactly

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "w": 3, "maxWeight": 15}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

cells, and each cell can hold at most one container. Therefore, no loading plan can use more than $n^2$ containers.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | cells, and each cell can hold at most one container.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Every container weighs exactly $w$. If $c$ containers are loaded, the weight constraint is

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "w": 3, "maxWeight": 15}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate filling cells:** Repeating up to $n^2:** - **Simulate filling cells:** Repeating up to $n^2$ placements produces the same minimum but wastes $O(n^2)$ time.
- **Binary-search the number of containers:** Feasibility is monotone, but the exact quotient gives the boundary directly.
- **Use only `maxWeight // w`:** This can exceed the number of deck cells when the ship has large weight capacity.
- **Use only `n * n`:** This can violate the ship's weight limit.
- **Capacity not divisible by weight:** Floor division correctly leaves unusable remainder capacity.
- **Capacity below one container weight:** The result is zero even though the deck has cells.
- **Exactly full-deck weight:** Both limits agree and every cell is filled.
- **Capacity greater than full-deck weight:** Extra ship capacity cannot create more cells, so the deck limit wins.
- **One-cell deck:** The answer is one if capacity reaches $w$, otherwise zero.
- **Identical container weights:** This uniformity is why only the count matters; varying weights would require a selection problem.
- **Positive inputs:** They guarantee meaningful cell count, weight, and safe division.
- **Equivalent formula:** `min(n*n, maxWeight//w)` may look more direct, while the protected source takes the minimum in weight units before dividing.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The source performs a fixed number of integer multiplications, one comparison through `min`, and one integer division. Time complexity is $O(1)$ and auxiliary space is $O(1)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
