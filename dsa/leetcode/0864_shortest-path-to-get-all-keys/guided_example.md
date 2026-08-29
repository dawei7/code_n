# Guided Example: Shortest Path to Get All Keys

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": ["@.a..", "###.#", "b.A.B"]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` grid `grid` where:

The objective is to compute `8` from `{"grid": ["@.a..", "###.#", "b.A.B"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Location alone is not enough state

Reaching the same cell with different keys creates different possibilities. A lock may be blocked on the first visit but passable after its key is collected.

Therefore, a BFS state contains:

- row `i`;
- column `j`;
- bitmask `state` of collected keys.

The visited set must include all three components. Marking only coordinates would incorrectly discard useful revisits after obtaining new keys.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": ["@.a..", "###.#", "b.A.B"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map keys to bits

The grid contains the first `k` lowercase letters, so:

- key `a` uses bit 0;
- key `b` uses bit 1;
- and so on.

For lowercase character `c`, its bit is:

`1 << (ord(c) - ord('a'))`.

Collecting it applies bitwise OR, which sets the bit without losing earlier keys.

The all-keys target mask is:

`(1 << k) - 1`.

Because keys are exactly the first `k` letters, this mask has precisely all required bits set.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the start and key count

A generator search locates the unique `@` coordinate.

The key count sums `v.islower()` across all cells. Booleans add as one or zero, and only lowercase key cells satisfy the test under the grid alphabet.

The initial state is the start coordinate with mask zero, placed in both queue and visited set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": ["@.a..", "###.#", "b.A.B"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **BFS by coordinate only:** Incorrect because returning with more keys can unlock new movement.
- **Permute key orders:** Trying all `c!` orders and pathfinding between keys repeats work and complicates lock constraints.
- **Compress points of interest and use Dijkstra:** Useful for some variants, but direct state BFS is clear with only 64 masks.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn2^c)$. Let the grid have `m n` cells and `c` keys.
- **Auxiliary Space Complexity:** $O(mn2^c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
