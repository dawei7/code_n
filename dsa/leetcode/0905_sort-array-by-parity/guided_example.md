# Guided Example: Sort Array By Parity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1, 2, 4]}`
- **Required output:** `[2, 4, 3, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

The objective is to compute `[2, 4, 3, 1]` from `{"nums": [3, 1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

The required output has one partition boundary: every even value must appear before every odd value. Relative order inside the even group and inside the odd group is irrelevant because any satisfying array is accepted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution partitions in place with two pointers:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution partitions in place with two pointers:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `i` searches from the left for a misplaced odd value.
- `j` searches from the right for a misplaced even value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 4, 3, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 4, 3, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two output lists:** Collect evens and odds sep:** - **Two output lists:** Collect evens and odds separately, then concatenate. This is easy but uses $O(n)$ extra space.
- **Stable in-place partition:** Preserving relative order generally requires shifting elements and can cost $O(n^2)$ without extra storage. Stability is not required.
- **Sort by parity key:** It works but usually costs $O(n\log n)$ and may use sorting workspace.
- **Single write pointer:** Scan for evens and swap each into the next left slot. This is another $O(n)$, $O(1)$ partition.
- **All even:** The left pointer advances across the array, and the order remains unchanged.
- **All odd:** The right pointer retreats across the array, and the order remains unchanged.
- **One value:** The loop never runs; either parity already satisfies the condition.
- **Zero:** Zero is even because `0 % 2 == 0` and belongs in the front group.
- **Alternating parity:** Several swaps may occur, but each fixes boundary positions permanently.
- **Duplicate values:** Parity, not uniqueness, determines placement.
- **Any accepted order:** The algorithm is free to reverse or rearrange members within a parity group.
- **Input mutation:** Callers needing the original order should pass a copy.
- **Pointer meeting:** The single middle value needs no classification action because verified groups on either side cannot be inverted through one cell.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. In every loop iteration, `i` increases, `j` decreases, or both. The unresolved interval strictly shrinks, so total iterations are $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
