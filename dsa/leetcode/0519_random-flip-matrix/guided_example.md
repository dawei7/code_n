# Guided Example: Random Flip Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 2, "n": 2, "random_values": [0], "operations": ["flip", "flip", "reset", "flip"]}`
- **Required output:** `[[0, 0], [1, 1], null, [0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `m x n` binary grid `matrix` with all the values set `0` initially. Design an algorithm to randomly pick an index `(i, j)` where $\text{matrix}[i][j] = 0$ and flips it to `1`. All the indices `(i, j)` where $\text{matrix}[i][j] = 0$ should be equally likely to be returned.

The objective is to compute `[[0, 0], [1, 1], null, [0, 0]]` from `{"m": 2, "n": 2, "random_values": [0], "operations": ["flip", "flip", "reset", "flip"]}` while avoiding redundant calculations and unnecessary overhead.

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

Materializing an `m` by `n` matrix would be wasteful because each dimension may be as large as $10^4$, while at most 1000 operations are performed. The solution instead treats every cell as one number in a flattened range and stores only the positions whose virtual meaning has changed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 2, "n": 2, "random_values": [0], "operations": ["flip", "flip", "reset", "flip"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For a zero-based flattened index `idx`, the corresponding coordinates are:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a zero-based flattened index `idx`, the corresponding co... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

This mapping is a bijection between integers from zero through `m * n - 1` and all matrix cells. Selecting a uniformly random available flat index is therefore equivalent to selecting a uniformly random available cell.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0], [1, 1], null, [0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 2, "n": 2, "random_values": [0], "operations": ["flip", "flip", "reset", "flip"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0], [1, 1], null, [0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Materialized list plus Fisher–Yates:** Store a:** - **Materialized list plus Fisher–Yates:** Store all $N$ flattened indices and swap selected values with the tail. It gives the same uniform process but requires $O(N)$ initialization and memory.
- **Rejection sampling:** Randomly choose cells until an unflipped one appears. It is simple, but calls to randomness and running time grow badly when few cells remain.
- **Store a set of flipped cells:** This still needs rejection sampling unless an additional searchable structure is used, so it does not guarantee one random call per flip.
- **Sparse virtual swaps:** The implemented dictionary records only positions changed by removals, giving expected constant-time flips with memory proportional to performed flips.
- **Last free cell:** After decrement, `total` is zero and `randint(0, 0)` deterministically selects the sole active slot.
- **Selecting the tail slot:** The returned tail value is removed directly; the self-mapping written at an inactive key cannot be sampled.
- **One-row or one-column matrix:** Flat division and remainder still produce correct coordinates.
- **Repeated flips without reset:** The active-prefix invariant ensures a cell cannot be returned twice.
- **Flip after reset:** Clearing `mp` removes every stale virtual swap, so all $mn$ cells are equally eligible again.
- **Operation guarantee:** The source promises a free cell before every `flip`, so the code never calls `randint` with an invalid empty interval.
- **Large dimensions:** Only `m * n` and sparse mappings are stored; Python integers safely hold the product.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $N = mn$ be the number of matrix cells and let $f$ be the number of flips since the most recent reset. Construction stores four scalar fields and an empty dictionary, so it takes $O(1)$ time and space beyond the object.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
