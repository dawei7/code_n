# Guided Example: Bricks Falling When Hit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[1, 0, 0, 0], [1, 1, 1, 0]], "hits": [[1, 0]]}`
- **Required output:** `[2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary `grid`, where each `1` represents a brick and `0` represents an empty space. A brick is **stable** if:

The objective is to compute `[2]` from `{"grid": [[1, 0, 0, 0], [1, 1, 1, 0]], "hits": [[1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse deletions into additions

Disjoint-set union efficiently merges connected components, but it does not efficiently split a component when a brick is removed.

Process the hits backward. In reverse time, each meaningful hit restores one brick. Components only merge, which is exactly the operation union-find supports.

The forward question “how many stable bricks lose their roof connection after this deletion?” becomes the reverse question “how many bricks gain a roof connection when this brick is restored?”

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[1, 0, 0, 0], [1, 1, 1, 0]], "hits": [[1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create the grid after all requested hits

The method deep-copies `grid` into `g` so the original remains available for deciding whether a hit location originally held a brick.

For every hit `(i,j)`, it sets:

`g[i][j] = 0`.

Hits are unique, so each requested position is removed at most once.

This `g` is the board on which reverse processing begins. It may contain brick components not connected to the top. Those components are deliberately retained in union-find as unstable groups; if a later restoration connects them to the roof, their entire size becomes relevant.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Represent the roof with a virtual node

Flatten cell `(i,j)` to index:

`i * n + j`.

Indices zero through `m*n-1` represent grid cells. Extra index `m*n` is a virtual roof.

Every brick in row zero is united with this virtual node. A brick is stable exactly when its flattened index belongs to the roof node's component.

The roof component's stored size includes the virtual node itself. Differences of roof sizes cancel that constant, so no special subtraction is needed until counting the restored brick.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[1, 0, 0, 0], [1, 1, 1, 0]], "hits": [[1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Add union by size or rank:** Choose the smaller/ranked root as the child while updating sizes. Together with path compression, this supports the manifest's inverse-Ackermann bound.
- **Forward flood fill after every hit:** Recomputing roof reachability costs up to $O(HN)$.
- **Delete from DSU directly:** Standard union-find cannot split components efficiently, which motivates reverse time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((r \cdot c + h) \cdot \alpha(r \cdot c))$. Let $N = m\cdot n$ be the number of cells and $H$ the number of hits. Copying and scanning the grid costs $O(N)$, and each brick/hit causes only a constant number of union/find operations.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
